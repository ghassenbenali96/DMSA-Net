# DMSA-Net
DNN-based diagnosis for 99m-Tc DMSA renal scintigraphy

**Overview:**
This Python-based project performs classification of 99m-Tc DMSA renal scintigraphy images using advanced image processing techniques and a custom Convolutional Neural Network (CNN). The system processes renal scintigraphy test images through preprocessing pipelines, trains a deep learning model, and provides a user-friendly interface for deployment.

**Key Features:**
- Image Preprocessing: Utilizes automatic cropping, Crimmins filtering for image enhancement, and augmentation for variability
- Deep Learning Model: Custom CNN architecture designed for renal scintigraphy classification
- Web Deployment: Streamlit-based interactive web application for model inference

**Project Structure:**
DMSA_Net/
├── colabs/            # Google Colab notebooks for preprocessing and training
│   ├── 1_PreProcessing.ipynb     # Image preprocessing pipeline
│   └── 2_Modeling.ipynb    # CNN training and evaluation
├── streamlit_app/              # Deployment application
│   ├── app.py                  # Main Streamlit application
├── models/                     # Trained model weights
├── data/                       # Dataset (not included in repo)
│   ├── raw/                   # Original images
│   └── processed/             # Preprocessed images
├── requirements.txt            # Python dependencies
└── README.md                   # This file

