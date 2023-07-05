from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = tf.keras.models.load_model('Pnemonia.h5')
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['Oneapi_1.ipynb']
        # Perform prediction with the model
        result = predict_image(file)
        return render_template('result.html', result=result)
    return render_template('disease.html')

def predict_image(file):
    img = tf.keras.preprocessing.image.load_img(file, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.resnet.preprocess_input(img)
    prediction = model.predict(img)
    result = np.argmax(prediction, axis=1)
    return result

if __name__ == '__main__':
    app.run()

