# 🌿 Plant Disease Prediction System using Deep Learning

A deep learning-based web application that detects plant diseases from leaf images using a Convolutional Neural Network (CNN). The system classifies plant leaf images into 38 different disease categories and provides real-time predictions through a Streamlit web interface.

---

# 📌 Project Overview

Plant diseases can significantly affect crop quality and agricultural productivity. Early detection helps farmers take preventive action and reduce crop loss.

This project uses a CNN-based image classification model trained on a large dataset of plant leaf images to automatically identify diseases from uploaded images.

---

# 🚀 Features

* 🌱 Detects plant diseases from leaf images
* 🧠 CNN-based deep learning model
* 📊 Supports 38 disease categories
* 🔄 Image preprocessing and augmentation
* 📈 Achieved approximately 95% validation accuracy
* 🌐 Real-time prediction using Streamlit
* ⚡ Simple and user-friendly interface

---

# 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Scikit-learn
* Streamlit

---

# 📂 Dataset

* Dataset Source: Kaggle Plant Disease Dataset
* Total Images: 87,000+
* Number of Classes: 38

The dataset contains images of healthy and diseased plant leaves organized into class-wise folders.

---

# 🧠 Model Architecture

The model uses a Convolutional Neural Network (CNN) consisting of:

* Input Layer
* Convolutional Layers
* MaxPooling Layers
* Flatten Layer
* Dense Layers
* Softmax Output Layer

---

# 🔄 Project Workflow

```text
Dataset → Preprocessing → CNN Model → Training → Evaluation → Deployment
```

---

# ⚙️ Image Preprocessing

The following preprocessing techniques were applied:

* Rescaling
* Normalization
* Horizontal Flipping
* Zoom Augmentation
* Shearing

These techniques help improve model generalization and reduce overfitting.

---

# 📊 Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Results

* Training Accuracy: ~98%
* Validation Accuracy: ~95%

---

# 🌐 Streamlit Deployment

The trained model was deployed using Streamlit.

### Application Flow

1. Upload a plant leaf image
2. Image preprocessing
3. CNN model prediction
4. Display predicted disease

---

# 📁 Project Structure

```text
Plant-Disease-Prediction/
│
├── app.py
├── trained_plant_disease_model.keras
├── requirements.txt
├── README.md
├── dataset/
├── notebooks/
└── images/
```

---

# ▶️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/seetharam001/Plant-Disease-Prediction.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Plant-Disease-Prediction
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```text
streamlit==1.35.0
tensorflow==2.10.0
numpy==1.24.3
scikit-learn==1.3.0
pandas==2.1.0
pillow
```

---

# 🔮 Future Improvements

* Add more disease classes
* Improve accuracy using transfer learning
* Mobile application deployment
* Cloud deployment
* Unknown disease detection

---

# 👨‍💻 Author

**Seetha Ram Poola**

* LinkedIn: [https://www.linkedin.com/in/seetharam-poola](https://www.linkedin.com/in/seetharam-poola)
* GitHub: [https://github.com/seetharam001](https://github.com/seetharam001)

---
