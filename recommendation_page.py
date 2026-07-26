import streamlit as st
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    # Define background image and additional styling for the Recommendations page
    img_file_path = "image/blue_house.jpg"  # Path to your image in the image folder
    img_base64 = get_img_as_base64(img_file_path)

    page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background-color: rgba(0, 0, 0, 0);
        }}

        [data-testid="stSidebar"] {{
            background: rgba(255, 255, 255, 0.7);
        }}

        [data-testid="stSidebarNav"]::before {{
            content: "LuminaryHomesKL";
            font-size: 20px;
            color: #ffffff;
            margin-left: 20px;
            margin-top: 20px;
            display: block;
        }}

        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
        
        .main-header {{
            font-size: 32px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }}

        .main-content {{
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            margin-top: 20px;
        }}

        .main-content p {{
            font-size: 18px;
            color: #333333;
            line-height: 1.6;
        }}

        .main-content ul {{
            font-size: 18px;
            color: #333333;
            line-height: 1.6;
            list-style-type: disc;
            margin-left: 20px;
        }}

        .main-content ul li {{
            margin-bottom: 10px;
        }}
    </style>
    """

    # Apply background image style
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-header">
            RECOMMENDATIONS
        </div>
        <div class="main-content">
            <p>
                Welcome to the Recommendations page! Here, you can get personalized recommendations based on your preferences and inputs.
            </p>
            <p>
                Please fill out the form below to receive your recommendations:
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Form for user inputs
    with st.form(key='recommendation_form'):
        location = st.selectbox('Select Location', ['Kuala Lumpur', 'Petaling Jaya', 'Shah Alam', 'Subang Jaya'])
        budget = st.slider('Select Your Budget (in MYR)', 100000, 1000000, step=50000)
        property_type = st.selectbox('Select Property Type', ['Apartment', 'Condominium', 'Terrace House', 'Semi-Detached House', 'Bungalow'])
        submit_button = st.form_submit_button(label='Get Recommendations')

    if submit_button:
        st.markdown(f"""
            <div class="main-content">
                <p>
                    Based on your inputs, here are some recommendations:
                </p>
                <ul>
                    <li><b>Location</b>: {location}</li>
                    <li><b>Budget</b>: MYR {budget}</li>
                    <li><b>Property Type</b>: {property_type}</li>
                </ul>
                <p>
                    Please contact our agents for more detailed recommendations and property listings.
                </p>
            </div>
        """, unsafe_allow_html=True)