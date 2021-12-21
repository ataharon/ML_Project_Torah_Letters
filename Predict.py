#make prediction from saved model
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def get_labels():
    #return df of [label, hebrew letter, name] for each letter in order of model
    labels = pd.read_excel("alef_bet_key.xlsx", header=None)
    labels[0] = labels[0].astype(str)
    labels = labels.sort_values(0)
    labels = labels.reset_index(drop=True)
    print(labels)
    return labels

def predict_from_image(model, image_path, labels):
    img = image.load_img(image_path,
                         target_size=(64, 64), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    # img_preprocessed = preprocess_input(img_batch)
    pred = model.predict(img_batch)
    print("prediction:", pred)
    # https://androidkt.com/get-class-labels-from-predict-method-in-keras/
    label = labels[1][np.argmax(pred)]
    return label

def main():
    num_torah = input("Enter number Torah:")
    num_contour = input("Enter number contour:")
    labels = get_labels()
    model = load_model('saved_model')
    image_path = f'Cropped_Contours/MOTB00{num_torah}/contour{num_contour}.png'
    img = Image.open(image_path)
    plt.imshow(img)
    plt.show()
    label = predict_from_image(model, image_path, labels)
    print("letter:", label)

main()