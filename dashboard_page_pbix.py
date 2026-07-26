import streamlit as st
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    # Encode the local image to base64
    img_file_path = "image/blue_house.jpg"  # Replace with the path to your background image
    img_base64 = get_img_as_base64(img_file_path)

    # Define background image and additional styling
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

    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.7);
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

    .iframe-container {{
        margin-top: 20px;
        margin-bottom: 20px;
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }}
    </style>
    """

    # Apply background image style
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-header">
            Dashboard: History of Kuala Lumpur Housing Prices
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="iframe-container">
           <iframe title="history housing data" width="100%" height="470" src="https://app.powerbi.com/links/IOwYunoSNc?ctid=9f149706-5dbb-4a20-947e-b92fdca3ae58&pbi_source=linkShare" frameborder="0" allowFullScreen="true"></iframe>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
