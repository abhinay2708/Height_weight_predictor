import pickle
import numpy as np
import streamlit as st 

filename='final_model.pkl'
with open(filename,'rb') as file:
    loaded_model=pickle.load(file)

st.markdown(
    """
    <style>
    .title {
        color: #FF5733;
        text-align: center;
        font-size: 32px;
    }
    .text {
        color: #7D3C98;
        text-align: center;
        font-size: 18px;
    }
    .prediction {
        color: #6C3483;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">Weight Prediction App</p>',unsafe_allow_html=True)
st.markdown('<p class="text">Enter your height in feet to predict your weight.</p>',unsafe_allow_html=True)

default_height=5.6

height_input=st.number_input("Enter the height in feet:",value=default_height,min_value=0.0)

if st.button('predict'):
    height_input_2d=np.array(height_input).reshape(1,-1)
    predict_weight=loaded_model.predict(height_input_2d)
    st.markdown(f'<p class="Prediction">predicted weight: {predict_weight[0,0]} kg</p>',unsafe_allow_html=True)


