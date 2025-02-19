# 🏥 Diabetic Retinopathy Detection

## 📌 Overview
This project is a **Diabetic Retinopathy Detection System** that uses a **Convolutional Neural Network (CNN)** to classify retinal images into two categories:
- ✅ **Diabetic Retinopathy**
- ❌ **Non-Diabetic Retinopathy**

The model is built using **TensorFlow** and **Keras**, and the web interface is developed using **Streamlit**. 📊

---

## 🚀 Features
- 🖼️ **Image Upload**: Users can upload retinal images for prediction.
- 🧠 **Deep Learning Model**: Uses CNN to classify images with high accuracy.
- 📊 **Model Information**: Displays model details and architecture.
- 🌐 **Web Interface**: Easy-to-use **Streamlit** application.

---

## 🛠️ Installation
Ensure you have **Python 3.8+** installed. Then, install the required dependencies:
```bash
pip install tensorflow numpy streamlit pillow
```

---

## 🎯 How to Use
1. **Run the Streamlit App** 📢
```bash
streamlit run app.py
```
2. **Upload an Image** 📸
3. **Get Prediction** 🔍
4. **View Model Info** 🏗️

---

## 📜 Code Structure
```
📂 hackathon
│── 📄 app.py  # Streamlit web app
│── 📄 model.py  # Model loading and prediction function
│── 📄 Diabetic Retinopathy.keras  # Pre-trained model file
```

---

## 🖥️ Prediction Function
```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array, load_img

def predict(image_path):
    model = load_model('Diabetic Retinopathy.keras')
    data_cat = ['Diabetic Retinopathy', 'Non-Diabetic Retinopathy']
    
    image = load_img(image_path, target_size=(180, 180))
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    return data_cat[np.argmax(score)], np.max(score) * 100
```

---

## 🎨 Web App Structure
```python
import streamlit as st

def app():
    st.title("Model Information")
    st.write("### Model Architecture")
    st.write("Convolutional Neural Network with Conv2D and MaxPooling layers.")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.sidebar.title("Navigation")
        app = st.sidebar.radio("Go to", self.apps, format_func=lambda app: app['title'])
        app['function']()
```

---

## 🤖 Technologies Used
- 🐍 **Python**
- 🧠 **TensorFlow & Keras**
- 🎨 **Streamlit**
- 📷 **OpenCV & Pillow**

---

## 🤝 Contributing
Feel free to contribute to this project by submitting issues or pull requests. Let's make **AI-driven healthcare** better! 🚀

---

## 📧 Contact
📩 **Email**: nimmanirishik@gmail.com  
🔗 **LinkedIn**: [Nimmani Rishik](https://linkedin.com/in/nimmani-rishik-66b632287)  
📸 **Instagram**: [rishik_3142](https://instagram.com/rishik_3142)

---

## ⭐ Acknowledgment
Special thanks to **AI and Deep Learning** for enabling breakthroughs in **medical diagnostics**. ❤️

