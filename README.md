# "Deep Torah Learning:" A deep learning model to detect anomalous letters in Torah scrolls
Ayelet Aharon, COMP 3920 Semester Project

## Background

There is a specialized area of research on the topic of Sifrei Torah (Torah scrolls). 
Ephraim Caspi, an Israeli scholar, is a leading researcher in this field. 
His goal is to classify Sifrei Torah based on unique qualities, such as column layout, letter shapes, and artistic flourishes. 
The work done to classify the Torahs based on these features is largely technological. 
However, to collect these features, each Sefer Torah is analyzed manually by scanning the letters and looking for abnormalities in the text. 
My project was inspired by this issue, and aims to add automation to the process to detect anomalous letters in Torahs faster and perhaps better than a human. 

## Data

I created a labeled dataset from images of Torah scrolls that I received from the Museum of the Bible. 
The data used in this model is from a total of 8 unique Torahs, one image from each. 

Image processing was done with `Image_Segmentation.py`.
First, I transformed the images into black and white. 
Then, I segmented the images into contours, saving each contour into a new image. The created contours can be found in the `Cropped_Contours` folder, organized by Torah.

Then, I labeled the dataset using `Label_Images.py`. 
This code displayed each contour and allowed me to input the label corresponding to the correct letter and eliminate any non-letters.
The labeled datasets are saved by image as `contour_labels_{image_name}.csv`.

Finally, I organized the images into directories by label with `Make_Image_Directories.py` to be easily compatible with the tensorflow method of creating datasets.
The organized images can be found in the `Images_By_Label` folder.

An exploratory data analysis was conducted in `Data_Analysis.ipynb`, illustrating the breakdown of the data. 

## Model

I built a neural network using the keras library. Specifications of the model can be seen in `Model.py`, and functions for prediction in `Predict.py`. The model contains a flattening layer to transform the image pixels to a single dimension, a rescaling layer to normalize the values, a hidden dense layer, and a final layer of 27 neurons corresponding to the 27 possible classes. The class label is chosen based on the neuron with the highest activation.

The model was evaluated in `Model_Metrics.ipynb` based on keras's built in accuracy metric, and the outcome is illustrated by a confusion matrix.

## Product

The final product, `Product.ipynb`, is an interactive notebook where the user can upload an image of a Torah letter. 
The saved model will then predict which letter it is and display a bar graph representing the activations of each label.
If the certainty of the label is below a certain threshold (the letter does not fit well into any category), the output indicates that this may be an anomalous letter.

Recommended images for test use of the product, taken from Torahs outside of the training and validation sets, can be found in `Cropped_Contours/test_contours`, and examples of anomalous letters in `Cropped_Contours/Anomalous_Letters`.



