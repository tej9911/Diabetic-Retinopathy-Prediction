import streamlit as st

def app():
    st.title("Model Information")
    st.write("### Model Architecture")
    # Display model summary (or static info) here
    st.write("Convolutional Neural Network with several Conv2D and MaxPooling layers.")
