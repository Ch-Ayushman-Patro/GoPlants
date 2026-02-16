<div align="center">

# 🌿 GoPlants - Plant Image Classifier

### AI-Powered Plant Recognition Using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red.svg)](https://keras.io/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)

[Overview](#-overview) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Model Details](#-model-details) • [Contact](#-contact)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Supported Plants](#-supported-plants)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Contributing](#-contributing)
- [Contact](#-contact)

---

## 🎯 Overview

**GoPlants** is an intelligent plant classification application that uses deep learning to identify **30 different plant species** from images. Built with a custom-trained Convolutional Neural Network (CNN), the application provides a user-friendly desktop interface for quick and accurate plant identification.

### Key Highlights:
- 🧠 **Deep Learning Model** trained on 30,000+ images
- 🎨 **Beautiful GUI** with gradient backgrounds and smooth animations
- ⚡ **Real-time Classification** with confidence scoring
- 📊 **High Accuracy** with comprehensive data augmentation
- 🔄 **Responsive Design** with threading for smooth user experience

---

## ✨ Features

### 🖼️ Image Upload & Classification
- Upload plant images in common formats (JPG, PNG, etc.)
- Instant preview of uploaded images
- One-click classification with visual feedback

### 🎯 Intelligent Prediction
- **Confidence-based results**: Only shows predictions with >40% confidence
- **30 plant species** recognition capability
- **Uncertainty handling**: Alerts when classification is unreliable

### 🎨 Modern User Interface
- **Gradient background** with teal color scheme
- **Hover effects** on buttons for better interactivity
- **Responsive layout** that adapts to window resizing
- **Clean design** with custom fonts and styling

### ⚙️ Technical Features
- **Multi-threaded processing** for responsive UI
- **Image preprocessing** with normalization
- **Data augmentation** for robust model training
- **Batch normalization** and dropout for better generalization

---

## 🌱 Supported Plants

The model can identify the following **30 plant species**:

| Category | Plants |
|----------|--------|
| **Vegetables** | Eggplant, Corn, Cucumber, Kale, Long Beans, Spinach, Sweet Potatoes, Peper Chili, Shallot |
| **Fruits** | Banana, Cantaloupe, Guava, Mango, Melon, Orange, Papaya, Pineapple, Pomelo, Water Apple, Watermelon |
| **Herbs & Spices** | Ginger, Galangal, Curcuma |
| **Crops** | Paddy, Soybeans, Cassava, Tobacco |
| **Others** | Aloe Vera, Bilimbi, Coconut |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) |
| **Deep Learning** | TensorFlow 2.x, Keras |
| **GUI Framework** | Tkinter |
| **Image Processing** | PIL (Pillow), NumPy |
| **Model Architecture** | Custom CNN with VGG-style blocks |
| **Data Augmentation** | ImageDataGenerator |

---

## 💻 Installation

### Prerequisites
- Python 3.11
- pip package manager
- At least 4GB RAM (for model loading)

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/GoPlants.git
cd GoPlants
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Ensure model file exists:**
   - The application requires `model2.keras` in the project directory
   - If missing, train the model using `model-creation.ipynb`

---

## 🚀 Usage

### Running the Application

1. **Launch the GUI application:**
```bash
python app.py
```

2. **Using the classifier:**
   - Click **"Upload Image"** to select a plant image from your computer
   - The image will be displayed in the preview area
   - Click **"Classify Image"** to identify the plant
   - View the prediction result with confidence level

### Expected Output

**High Confidence (≥40%):**
```
🌿 Predicted Class: mango
Confidence Level: 0.87
```

**Low Confidence (<40%):**
```
⚠️ Unpredictable: The uploaded item cannot be reliably classified.
```

---

## 🧠 Model Details

### Architecture

The model uses a **custom CNN architecture** with the following components:

- **Convolutional Blocks**: Multiple Conv2D layers with ReLU activation
- **Batch Normalization**: For stable training and faster convergence
- **Max Pooling**: For spatial dimension reduction
- **Dropout Layers**: To prevent overfitting (rate: 0.5)
- **Dense Layers**: Fully connected layers with 512 and 256 neurons
- **Output Layer**: 30-class softmax for plant classification

### Training Details

| Parameter | Value |
|-----------|-------|
| **Input Size** | 150 x 150 pixels |
| **Training Images** | 23,972 images |
| **Validation Images** | 3,030 images |
| **Test Images** | 2,998 images |
| **Batch Size** | 32 |
| **Classes** | 30 plant species |
| **Trainable Parameters** | ~11.4M |
| **Non-trainable Parameters** | ~7.6M |

### Data Augmentation

To improve model robustness, the following augmentations were applied:

- **Rotation**: ±20 degrees
- **Width/Height Shift**: ±20%
- **Shear Transformation**: 20%
- **Zoom**: ±20%
- **Horizontal Flip**: Random
- **Fill Mode**: Nearest neighbor

---

## 📁 Project Structure

```
GoPlants/
├── app.py                      # Main GUI application
├── model2.keras                # Trained deep learning model
├── model-creation.ipynb        # Notebook for model training
├── model-testing.ipynb         # Notebook for model evaluation
├── requirements.txt            # Python dependencies
└── dataset/                    # Dataset directory (not included)
    ├── train/                  # Training images             
    ├── validation/             # Validation images
    └── test/                   # Test images
```

---

## 🔍 How It Works

### 1. **Image Upload**
   - User selects an image through the file dialog
   - Image is displayed in the GUI (resized to 200x200 for preview)

### 2. **Image Preprocessing**
   - Image is resized to 150x150 pixels (model input size)
   - Pixel values are normalized to [0, 1] range
   - Image is converted to a batch format (1, 150, 150, 3)

### 3. **Model Prediction**
   - Preprocessed image is fed to the CNN model
   - Model outputs probability distribution across 30 classes
   - Highest probability class is selected as prediction

### 4. **Confidence Check**
   - If confidence < 40%: Display uncertainty warning
   - If confidence ≥ 40%: Display predicted class and confidence

### 5. **Result Display**
   - Results are shown in the GUI with appropriate formatting
   - Threading ensures the UI remains responsive during classification

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/AmazingFeature`
3. **Commit your changes:** `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch:** `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Contribution Ideas:
- 🌿 Add support for more plant species
- 📱 Create a mobile version of the app
- 🌐 Build a web-based interface
- 📊 Improve model accuracy with advanced architectures
- 🎨 Enhance UI/UX design
- 📝 Add plant information and care tips

---

## 📬 Contact

**Developed by Ch Ayushman Patro**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/ch-ayushman-patro) [![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Ch-Ayushman-Patro)

For questions, suggestions, or collaboration opportunities, feel free to reach out!
