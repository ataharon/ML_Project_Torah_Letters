#change directory format to work with keras
#subdirectories = labels
import os
import shutil

def copy_images(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            image_path, label = line.split(",")
            folder, file = image_path.split('/')
            old_path = f"Cropped_Contours/{image_path}"
            new_path = f"Images_By_Label/{label}"
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            shutil.copy(old_path, f'{new_path}/{folder}_{file}')


copy_images("contour_labels_MOTB009.csv")
