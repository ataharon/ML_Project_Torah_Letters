# label contours as Hebrew letter
import os
from PIL import Image
from csv import writer
import matplotlib.pyplot as plt

#process contours of one image at a time
def label_contours(image):
    n = int(input("Enter number of contour you're up to: "))

    with open(f"contour_labels_{image}.csv", 'a') as f:
        writer_object = writer(f)

        path = f"Cropped_Contours/{image}"
        image_list = os.listdir(path)
        num_images = len(image_list)
        for i in range(n, num_images):
            contour_path = f"contour{i}.png"
            img = Image.open(f"{path}/{contour_path}")
            plt.imshow(img)
            plt.show()

            while True:
                label = input("Enter label: ")

                try:
                    label = int(label)
                except:
                    label = -2

                if label < -1 or label > 26:
                    print("Invalid input. Try again")

                # -1 = skip this contour and delete image
                elif label == -1:
                    os.remove(f"{path}/{contour_path}")
                    break

                #valid input: add to csv
                else:
                    writer_object.writerow([f"{image}/{contour_path}", label])
                    break

label_contours("MOTB002")