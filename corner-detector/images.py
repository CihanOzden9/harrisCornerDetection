import os

def get_images():
   
    file_path = f"{os.path.dirname(os.path.abspath(__file__))}/HCD_images"
    image_list = [f for f in os.listdir(file_path)]
    return image_list
