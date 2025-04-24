import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Set page config - must be the first Streamlit command
st.set_page_config(page_title="Dairy Classifier", page_icon="🧀", layout="centered")

# Load the model
model = load_model('dairy_classifier.h5')

IMG_SIZE = (224, 224)

def predict_image(image):
    image = image.resize(IMG_SIZE).convert('RGB')
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    confidence = prediction[0][0]
    return "Spoiled" if confidence > 0.5 else "Fresh", confidence

# Streamlit App UI
st.title("Dairy Product Classifier")
st.write("Upload an image of a dairy product to predict if it's Fresh or Spoiled.")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    label, score = predict_image(image)
    st.write(f"Prediction: {label}")
    st.write(f"Confidence: {score:.4f}")
