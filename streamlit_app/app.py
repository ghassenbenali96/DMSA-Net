import streamlit as st
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
import os

# --- Preprocessing functions ---
def manual_crop(image, y1, y2, x1, x2, output_size=(224, 224)):
    cropped = image[y1:y2, x1:x2]
    return cv2.resize(cropped, output_size, interpolation=cv2.INTER_AREA)

def isolate_kidneys(image, max_components=2):
    _, thresh = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(thresh, 8)
    sorted_labels = sorted(range(1, num_labels), key=lambda i: stats[i, cv2.CC_STAT_AREA], reverse=True)
    mask = np.zeros_like(image, dtype=np.uint8)
    for i in sorted_labels[:max_components]:
        mask[labels == i] = 255
    inverse_mask = cv2.bitwise_not(mask)
    return cv2.inpaint(image, inverse_mask, 3, cv2.INPAINT_TELEA)

def crimmins_filter(img, iterations=2):
    img = img.astype(np.int16)
    for _ in range(iterations):
        for offset in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
            for direction in [+1, -1]:
                filtered = img.copy()
                for y in range(1, img.shape[0] - 1):
                    for x in range(1, img.shape[1] - 1):
                        neigh = img[y + offset[1], x + offset[0]]
                        if direction * (img[y, x] - neigh) >= 2:
                            filtered[y, x] -= direction
                img = filtered
    return np.clip(img, 0, 255).astype(np.uint8)

# --- Load model ---
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(r"C:\Users\ghass\Desktop\DMSA-Net\models\dmsa_model_91_96.h5")

model = load_model()

# --- Streamlit UI ---
st.title("🧠 Renal DMSA Scan Classifier")
st.markdown("Upload a 99m-Tc DMSA scintigraphy image to classify it as **normal** or **pathological**.")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Original Image", use_container_width=True)
    image = Image.open(uploaded_file).convert("L")
    image = np.array(image)

    # Preprocessing
    y1, y2, x1, x2 = 20, 220, 20, 220  # Customize these values as needed
    cropped = manual_crop(image, y1, y2, x1, x2, output_size=(160, 160))
    kidneys_only = isolate_kidneys(cropped)
    denoised = crimmins_filter(kidneys_only)

    st.image(denoised, caption="Preprocessed Image", width=200)

    # Prepare for prediction
    input_img = cv2.resize(denoised, (224, 224)).reshape(1, 224, 224, 1).astype('float32') / 255.

    pred = model.predict(input_img)[0][0]
    label = "Pathological" if pred > 0.5 else "Normal"
    confidence = pred if pred > 0.5 else 1 - pred

    st.success(f"🩺 Prediction: **{label}** (Confidence: {confidence:.2%})")