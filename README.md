# 🫘🩺 DMSA-Net
A DNN-based diagnosis tool for 99m-Tc DMSA renal scintigraphy

## 🔍 Overview
This Python-based project performs binary classification of 99m-Tc DMSA (Dimercaptosuccinic Acid) renal scintigraphy images using multiple image processing techniques and a custom Convolutional Neural Network (CNN). The system processes renal scintigraphy test images through preprocessing pipelines, trains a deep learning model, and provides a user-friendly interface for deployment.

## 🏗️ Key Features

- **Advanced Image Processing Pipeline**
  - 🔍 **Automatic Kidney Cropping**: ROI extraction through a fixed window (224x224)
  - 🖼️ **Crimmins Speckle Reduction**: Noise suppression while preserving edges
  - 🔍 **Kidney isolation and inpainting**: Adaptive removal of extra masses in the image (bladder, ureter) and inpainting of newly evacuated regions
  - 🔄 **Comprehensive Augmentation**:
    - Normalization: Rescales pixel values to [0, 1]
    - Geometric Transformations:  
      - Random rotations  
      - Small width/height shifts  
      - Random zoom  
      - Horizontal flipping  
    - Photometric Adjustments:  
      - Brightness variation  
    - Validation Split:  
      - Automatically reserves 20% of data for validation  
      - Uses fill_mode='nearest' to handle edge artifacts during transformations  

- **Deep Learning Architecture**
  -Input: Grayscale scintigraphy images (256×256×1)
  -Feature Extraction:
    - 5 convolutional blocks with decreasing spatial dimensions
    - Progressive filter increase (32 → 128)
    - All layers use same padding and ReLU activation
  - Classification Head:
    - 3 fully-connected layers with dimensionality reduction
    - 50% dropout for regularization
    - Sigmoid output for binary classification

- **Local Development Focus**
  - Virtual environment (venv) configuration
  - Local GPU/CPU compatibility
  - Easy transition to cloud (Colab) when needed

## 🗃️ Dataset
The model is trained on 568 actual 99m-Tc DMSA renal scintigraphy images from Salah Azaiez Institute (Tunisia), the largest dataset collected for this task so far. Due to patient privacy concerns, only a small number of samples is included in the dataset. To use your own dataset:  
- Place images in data/raw/ directory  
- Organize into appropriate class folders  
- Update paths in the Colab notebooks

## 📊 Results

| Metric             | Value                 |
| ----------------- | ----------------------|
| Accuracy |      91.96%       |
| Precision |      91%       |
| Recall |      93%       |
| F1-score |       92%      |


## 📂 Project Structure
DMSA_Net/  
├── notebooks/            *# Google Colab notebooks for preprocessing and training*  
│   ├── 1_PreProcessing.ipynb     *# Image preprocessing pipeline*  
│   └── 2_Modeling.ipynb    *# CNN training and evaluation*  
├── streamlit_app/              *# Deployment application*  
│   ├── app.py                  *# Main Streamlit application*  
├── models/                     *# Trained model weights*  
├── data/                       *# Dataset (not included in repo)*  
│   ├── raw/                   *# Original images*  
│   └── processed/             *# Preprocessed images*  
├── requirements.txt            *# Python dependencies*  
└── README.md                   *# This file*

## 🛠️ Installation
### Prerequisites
- Python 3.8 or higher
- Virtual environment support
- Streamlit (for deployment)

### Setup 
**1-**  Clone the repository: 

```bash
  git clone https://github.com/ghassenbenali96/DMSA-Net.git
  cd DMSA-Net
```

**2-** Create and activate virtual environment  
```bash
python -m venv dmsa
source dmsa/bin/activate  # Linux/Mac
.\dmsa\Scripts\activate   # Windows
```

**3-** Install dependencies  
```bash
pip install -r requirements.txt
```

## 💻 Usage
For direct deployment using Streamlit:  
- Run the Streamlit app:
```bash
cd streamlit_app
streamlit run app.py -- \
    --model_path ../models/dmsa_model_91_96.h5 \
    --preprocess_mode full
```

For modification and experimentation using notebooks:
- Open notebooks directory:
```bash
cd notebooks
```
- Open *1_PreProcessing.ipynb* and run all cells
- Open *2_Modeling.ipynb* and ru all cells


## 📜 License
This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.  
Permissions: 
  - ✅ Commercial use  
  - ✅ Modification  
  - ✅ Distribution  
  - ✅ Private use

Limitations:  
  - ❌ Liability  
  - ❌ Warranty

Conditions:  
  - ©️ Must include original copyright notice
