import streamlit as st
import cv2
import numpy as np
import keras

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
	st.title("Hello Sannamyr!")
	st.markdown(html, unsafe_allow_html=True)
	uploaded_file = st.file_uploader("Choose a image file", type="jpg")
	if uploaded_file is not None:
    		# Convert the file to an opencv image.
    		file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    		opencv_image = cv2.imdecode(file_bytes, 1)

    		# Now do something with the image! For example, let's display it:
    		st.image(opencv_image, channels="BGR")
		st.text(new_model)

if __name__ == '__main__':
	main()

