import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array, load_img

# Load the trained model
model = load_model('C:/Users/USER/Downloads/hackathon/Diabetic Retinopathy.keras')  # Adjust path as necessary
data_cat = ['Diabetic Retinopathy', 'Non-Diabetic Retinopathy']  # Categories

def predict(image_path):
    # Load and preprocess the image
    image = load_img(image_path, target_size=(180, 180))
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)  # Create batch axis

    # Make prediction
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    # Get the result
    return data_cat[np.argmax(score)], np.max(score) * 100
