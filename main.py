import streamlit as st
import tensorflow as tf
import numpy as np

# ==============================
# Load Model (load once for speed)
# ==============================
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("trained_plant_disease_model.keras")

model = load_model()

# ==============================
# Prediction Function
# ==============================
def model_prediction(test_image):
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)


# ==============================
# Class Labels
# ==============================
class_name = [
    'Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust','Apple___healthy',
    'Blueberry___healthy','Cherry_(including_sour)___Powdery_mildew','Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight','Corn_(maize)___healthy','Grape___Black_rot',
    'Grape___Esca_(Black_Measles)','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)','Peach___Bacterial_spot','Peach___healthy',
    'Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy','Potato___Early_blight',
    'Potato___Late_blight','Potato___healthy','Raspberry___healthy','Soybean___healthy',
    'Squash___Powdery_mildew','Strawberry___Leaf_scorch','Strawberry___healthy',
    'Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight',
    'Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite','Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus','Tomato___Tomato_mosaic_virus','Tomato___healthy'
]

# ==============================
# Sidebar
# ==============================
st.sidebar.title("🌿 Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# ==============================
# Home Page
# ==============================
if app_mode == "Home":
    st.title("🌿 Plant Disease Recognition System")
    st.image("home_page.jpeg", use_column_width=True)

    st.markdown("""
    Welcome to the Plant Disease Recognition System 🌱

    ### How It Works:
    1. Upload a plant leaf image
    2. Model analyzes the image
    3. Get disease prediction instantly

    ### Features:
    ✔ Deep Learning based prediction  
    ✔ Fast and accurate  
    ✔ Easy to use  
    """)

# ==============================
# About Page
# ==============================
elif app_mode == "About":
    st.title("📊 About Project")

    st.markdown("""
    - Dataset: ~87K images  
    - Classes: 38 plant diseases  
    - Model: CNN (Convolutional Neural Network)  
    - Accuracy: ~94–95%  

    This system helps in early detection of plant diseases.
    """)

# ==============================
# Prediction Page
# ==============================
elif app_mode == "Disease Recognition":
    st.title("🔍 Disease Recognition")

    test_image = st.file_uploader("Upload a Leaf Image")

    if test_image is not None:
        st.image(test_image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        if test_image is None:
            st.warning("Please upload an image first!")
        else:
            st.write("🔍 Predicting...")
            result_index = model_prediction(test_image)

            result = class_name[result_index]
            st.success(f"🌿 Prediction: {result}")