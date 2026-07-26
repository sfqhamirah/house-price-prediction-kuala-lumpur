import streamlit as st
import base64

# Function to convert image to base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
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

        .main-content h4 {{
            font-size: 24px;
            color: #333333;
            margin-top: 20px;
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

    # About Page Content
    st.markdown("""
        <div class="main-header">
            About
        </div>
        <div class="main-content">
            <p>Welcome to the House Price Prediction System!</p>
            <p>This application allows users to predict house prices based on various input features. It also provides a comprehensive dashboard to view statistics and visualizations related to the housing market.</p>
            <h4>Features:</h4>
            <ul>
                <li><b>Prediction Page</b>: Input house details such as size, location, number of bedrooms, and more to get an estimated price.</li>
                <li><b>Dashboard</b>: View interactive visualizations and statistics about the housing market.</li>
                <li><b>User-Friendly Interface</b>: Easy navigation through different pages using the menu.</li>
            </ul>
            <h4>Technologies Used:</h4>
            <ul>
                <li><b>Streamlit</b>: For building the web application.</li>
                <li><b>Power BI</b>: For creating the interactive dashboard.</li>
                <li><b>Python</b>: For backend logic and predictions.</li>
            </ul>
            <h4>How to Use:</h4>
            <ul>
                <li>Navigate through the different pages using the menu.</li>
                <li>Use the Prediction page to input details and get price predictions.</li>
                <li>View detailed statistics and visualizations on the Dashboard page.</li>
            </ul>
            <h4>Contact:</h4>
            <p>For any inquiries or feedback, please contact us at: 2021610192@student.uitm.edu.my</p>
            <p>Thank you for using our app!</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
