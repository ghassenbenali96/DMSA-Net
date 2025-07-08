#  DMSA-Net
DNN-based diagnosis for 99m-Tc DMSA renal scintigraphy

## Overview
This Python-based project performs classification of 99m-Tc DMSA renal scintigraphy images using multiple image processing techniques and a custom Convolutional Neural Network (CNN). The system processes renal scintigraphy test images through preprocessing pipelines, trains a deep learning model, and provides a user-friendly interface for deployment.

## Key Features

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
  - Custom 8-layer CNN with residual connections
  - Adaptive learning rate scheduling
  - Class-weighted loss function for imbalanced data

- **Local Development Focus**
  - Virtual environment (venv) configuration
  - Local GPU/CPU compatibility
  - Easy transition to cloud (Colab) when needed

## Project Structure
DMSA_Net/  
├── colab/            *# Google Colab notebooks for preprocessing and training*  
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

