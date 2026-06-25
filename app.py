import streamlit as st
from PIL import Image
import numpy as np

def predict_tumor(image_array):
    return "Tumor Detected" if np.mean(image_array) < 100 else "No Tumor Detected"

st.title("Liver Cancer Detection from CT Scans")
st.write("Upload a CT scan image to detect presence of liver tumor.")

uploaded_file = st.file_uploader("Choose a CT scan image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # grayscale
    st.image(image, caption="Uploaded CT Image", use_container_width=True)

    image_resized = image.resize((224, 224))
    image_array = np.array(image_resized)

    prediction = predict_tumor(image_array)
    st.subheader("Prediction:")
    st.success(prediction)
