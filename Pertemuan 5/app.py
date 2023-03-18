import os
import numpy as np
import cv2
import streamlit as st
from tensorflow import keras
from keras.models import load_model
from streamlit_drawable_canvas import st_canvas

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'digit-recognizer')
# if not os.path.isdir(MODEL_DIR):
#     os.system()


model = load_model('digit-recognizer', compile=False)
model.compile()

st.title('Digit Recognizer')

SIZE = 192
mode = st.checkbox('Draw or delete', True)

canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=20,
    stroke_color='#FFFFFF',
    background_color='#000000',
    width=SIZE,
    height=SIZE,
    drawing_mode='freedraw' if mode else 'transform',
    key='canvas'
)

if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'),(28,28))
    rescale = cv2.resize(img, (SIZE,SIZE), interpolation=cv2.INTER_NEAREST)
    st.write('Model input')
    st.image(rescale)

if st.button('Predict'):
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    val = model.predict(test_x.reshape(1,28,28))
    st.write(f'Result : {np.argmax(val[0])}')
    st.bar_chart(val[0])