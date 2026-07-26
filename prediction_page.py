import numpy as np
import pickle
import streamlit as st
import base64
import os

# =========================
# LOAD MODEL (SAFE VERSION)
# =========================
@st.cache_resource
def load_model():
    try:
        model_path = os.path.join(
            os.path.dirname(__file__),
            "house_price_prediction_model.sav"
        )

        with open(model_path, "rb") as model_file:
            model = pickle.load(model_file)

        return model

    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None


loaded_model = load_model()

if loaded_model is None:
    st.stop()


# =========================
# PREDICTION FUNCTION
# =========================
def house_price_prediction(input_data):
    try:
        input_data = np.asarray(input_data).reshape(1, -1)

        prediction = loaded_model.predict(input_data)

        return prediction[0] * 1_000_000  # scale back if needed

    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None


# =========================
# IMAGE BASE64 FUNCTION
# =========================
def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()


# =========================
# MAIN APP
# =========================
def main():

    img_file_path = "image/blue_house.jpg"

    try:
        img_base64 = get_img_as_base64(img_file_path)
    except:
        img_base64 = ""

    page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background-color: rgba(0, 0, 0, 0);
        }}

        .main-header {{
            font-size: 32px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 40px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}

        .predicted-price {{
            font-size: 24px;
            font-weight: bold;
            color: white;
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
        }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-header">
            House Price Prediction
        </div>
    """, unsafe_allow_html=True)


    # =========================
    # INPUT DATA
    # =========================
    locations = [
        "ADIVA Desa ParkCity", "Alam Damai", "Ampang", "Ampang Hilir", "Bandar Damai Perdana",
        "Bandar Menjalara", "Bandar Sri Damansara", "Bandar Tasik Selatan", "Bangsar"
    ]

    property_type = [
        "Apartment", "Condominium", "Bungalow", "Semi-D House", "Terrace House"
    ]

    col1, col2, col3 = st.columns(3)

    with col1:
        Location = st.selectbox("Location", locations)
        NumberOfRooms = st.number_input("Rooms", min_value=0, step=1)
        NumberOfCarParks = st.number_input("Car Parks", min_value=0, step=1)

    with col2:
        NumberOfBathroom = st.number_input("Bathrooms", min_value=0, step=1)
        PropertyType = st.selectbox("Property Type", property_type)
        Furnishing = st.selectbox("Furnishing", ["Fully Furnished", "Partially Furnished", "Unfurnished"])

    with col3:
        SizeType = st.selectbox("Size Type", ["Built-up", "Land Area"])
        SizeValue = st.number_input("Size (sq ft)", min_value=0.0, step=1.0)


    # =========================
    # PREDICTION BUTTON
    # =========================
    if st.button("Predict House Price"):

        input_data = (
            locations.index(Location),
            NumberOfRooms,
            NumberOfBathroom,
            NumberOfCarParks,
            property_type.index(PropertyType),
            ["Fully Furnished", "Partially Furnished", "Unfurnished"].index(Furnishing),
            ["Built-up", "Land Area"].index(SizeType),
            SizeValue
        )

        price = house_price_prediction(input_data)

        if price is not None:
            st.markdown(
                f'<div class="predicted-price">RM {price:,.2f}</div>',
                unsafe_allow_html=True
            )
        else:
            st.error("Prediction failed.")


if __name__ == "__main__":
    main()