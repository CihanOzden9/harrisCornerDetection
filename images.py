import os

def get_images():
   
    file_path = r"C:\Users\Cio\Desktop\python\harris_corner_detection\HCD_images"
    image_list = [f for f in os.listdir(file_path)]
    return image_list
    