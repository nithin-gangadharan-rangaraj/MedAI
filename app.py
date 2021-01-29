import streamlit as st
import cv2
import numpy as np
import keras
from tensorflow.keras.preprocessing import image
import tensorflow as tf

PAGE_CONFIG = {"page_title":"Arsya.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

html = '''
<style>
body {
background-image: url("https://img.freepik.com/free-vector/white-elegant-texture-wallpaper_23-2148421854.jpg?size=626&ext=jpg&ga=GA1.2.145878890.1611360000");
background-size: cover;
}
</style>
'''
new_model = keras.models.load_model("haemorrhage_model.h5")

def main():
	st.title("MedAI")
	st.markdown(html,unsafe_allow_html=True)
	uploaded_file=st.file_uploader("Choose a image file",type="png")
	if uploaded_file is not None:
		ba=bytearray(uploaded_file.read())
		file_bytes=np.asarray(ba,dtype=np.uint8)
		opencv_image=cv2.imdecode(file_bytes,1)
		st.image(opencv_image,channels="BGR")
		imagee(file_bytes)    		


def imagee(file_bytes):
	images = image.load_img(file_bytes, target_size=(128, 128))    
	x = image.img_to_array(images)
	x = tf.image.rgb_to_grayscale(x)
	x = np.expand_dims(x, axis=0)
	x = x/255.0
	if(model.predict_classes(x)[0][0] == 1):
  		st.text(Haemorrhage)
	else:
  		st.text(Normal)

if __name__ == '__main__':
	main()

