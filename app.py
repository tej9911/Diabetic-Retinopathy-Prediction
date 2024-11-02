import streamlit as st
from model import predict
from PIL import Image
import base64

# Convert image to Base64 to use as background
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the background image
image_path = "C:/Users/USER/Downloads/WhatsApp Image 2024-10-28 at 14.34.50_a6278d74.jpg"
base64_image = get_base64_image(image_path)

# Function to display the home page content
def display_home():
    st.title("Diabetic Retinopathy Detection")
    st.markdown("""
    <h2 style='color: grey; font-weight: bold;'>What is Diabetic Retinopathy?</h2>
    <p style='color: white;'>Diabetic Retinopathy is a diabetes complication that affects the eyes. It can cause vision loss and blindness.</p>
    <p style='color: white; font-weight: bold;'>Stay informed and take care of your vision!</p>
    """, unsafe_allow_html=True)

# Set the layout for the sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["Home", "Upload Image", "About"])

# Define page content
if page == "Home":
    display_home()

elif page == "Upload Image":
    st.header("Upload an Image for Prediction")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Save the uploaded image temporarily
        image_path = f"images/{uploaded_file.name}"
        image.save(image_path)
        
        # Prediction
        label, confidence = predict(image_path)
        st.write(f"Prediction: **{label}**")
        st.write(f"Confidence: **{confidence}**")

elif page == "About":
    st.header("About Diabetic Retinopathy Detection App")
    st.write("""
        This application leverages a convolutional neural network (CNN) 
        to detect diabetic retinopathy from retinal images. It aims to provide 
        accurate and timely predictions to assist healthcare professionals and patients.

        **Developer:** Your Name
        **Version:** 1.0
        **Contact:** your.email@example.com
    """)

# Customizing the appearance with CSS for background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/jpg;base64,{base64_image}") no-repeat center center fixed;
        background-size: cover;
    }}
    .overlay {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5); /* Dark overlay for better text contrast */
        z-index: -1;
    }}
    .css-1d391kg {{
        color: black; /* Change sidebar text color to black */
    }}
    h1 {{
        color: #FFD700;  /* Gold color for main title */
        font-size: 3em;  /* Larger font size */
        font-weight: bold;
    }}
    h2 {{
        color: #FFFAFA;  /* Snow color for subtitles */
        font-size: 2.5em;  /* Slightly larger font size */
    }}
    p {{
        color: #00008B;  /* Dark blue color for explanation text */
        font-size: 1.5em;  /* Increased font size */
    }}
    </style>
    <div class="overlay"></div>
    """,
    unsafe_allow_html=True
)
