import streamlit as st
from streamlit_option_menu import option_menu
import prediction_page
import dashboard_page
import about_page
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    # Define the menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "Prediction", "Dashboard", "About"],
            icons=["house", "clipboard-data", "bar-chart", "info-circle"],
            menu_icon="cast",
            default_index=0,
            styles={
                "nav-link": {
                    "font-size": "17px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#7D97D0"},
            }
        )

    # Encode the local image to base64
    img_file_path = "image/background.png"  # Path to your image in the image folder
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

    # Display the selected page content
    if selected == "Home":
        st.markdown("""
            <div class="main-header">
                WELCOME TO LUMINARYHOMESKL
            </div>
            <div class="main-content">
                <p>
                    Introducing LuminaryHomesKL.com, where innovation meets real estate. Our House Price Prediction System is revolutionizing the way you navigate Kuala Lumpur's vibrant property market. Powered by cutting-edge technology, our platform provides accurate predictions that empower you with invaluable insights for informed decision-making.
                </p>
                <p>
                    Gone are the days of uncertainty when it comes to property investments. With LuminaryHomesKL.com, you can confidently anticipate market trends and make strategic choices backed by data-driven forecasts. Whether you're buying, selling, or investing, our state-of-the-art system equips you with the knowledge you need to stay ahead in Kuala Lumpur's dynamic real estate landscape.
                </p>
                <p>
                    Experience the future of property prediction with LuminaryHomesKL.com. Unlock the potential of Kuala Lumpur's property market like never before.
                </p>
                <p>
                    Use the navigation menu to access different pages:
                </p>
                <ul>
                    <li><b>Home</b>: This main page.</li>
                    <li><b>Prediction</b>: Navigate to the prediction page to input house details and get a price prediction.</li>
                    <li><b>Dashboard</b>: View various statistics and visualizations.</li>
                    <li><b>About</b>: Learn more about this system.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    elif selected == "Prediction":
        prediction_page.main()
    elif selected == "Dashboard":
        dashboard_page.main()
    elif selected == "About":
        about_page.main()

if __name__ == '__main__':
    main()
