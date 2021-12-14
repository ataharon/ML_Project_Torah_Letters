# label contours as Hebrew letter
import os
from PIL import Image
from csv import writer

#process contours of one image at a time
def label_contours(image):
    n = int(input("Enter number of contour you're up to: "))

    with open("contour_labels.csv", 'a') as f:
        writer_object = writer(f)

        path = f"Cropped_Contours/{image}"
        image_list = os.listdir(path)
        # image_list.sort()
        # print(image_list)
        num_images = len(image_list)
        for i in range(n, num_images):
            contour_path = f"contour{i}.png"
            img = Image.open(f"{path}/{contour_path}")
            img = img.resize((200, 200))
            img.show()
            img.close()

            while True:
                label = input("Enter label: ")

                try:
                    label = int(label)
                except:
                    label = -2

                #-1 = skip this contour
                if label < -1 or label > 26:
                    print("Invalid input. Try again")
                elif label != -1:
                    writer_object.writerow([f"{image}/{contour_path}", label])
                    break
                else:
                    break

            img.close()

label_contours("MOTB002")