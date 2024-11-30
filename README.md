**final_project** 
from PIL import Image, ImageFilter
import os

class ImageFilterLibrary:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.filters = {
            "blur": self.apply_blur,
            "contour": self.apply_contour,
            "sharpen": self.apply_sharpen,
        }

    def apply_filter(self, filter_name):
        if filter_name not in self.filters:
            raise ValueError(f"Filter '{filter_name}' is not available.")
        self.image = self.filters[filter_name]()
        return self.image

    def apply_blur(self):
        return self.image.filter(ImageFilter.BLUR)

    def apply_contour(self):
        return self.image.filter(ImageFilter.CONTOUR)

    def apply_sharpen(self):
        return self.image.filter(ImageFilter.SHARPEN)

    def save_image(self, save_path):
        self.image.save(save_path)
        print(f"Image saved to {save_path}")

# Command-line interface example
def main():
    def main():
    print("Welcome to Image Filter Library")
    image_path = input("Enter the path of the image: ")
    if not os.path.exists(image_path):
        print("File does not exist.")
        return
    
    library = ImageFilterLibrary(image_path)
    print("Available filters:", ", ".join(library.filters.keys()))
    
    while True:
        filter_name = input("Enter the filter you want to apply: ")
        try:
            filtered_image = library.apply_filter(filter_name)
            filtered_image.show()
            break
        except ValueError as e:
            print(e)

    while True:
        save_path = input("Enter the path to save the filtered image: ")
        try:
            library.save_image(save_path)
            break  # 저장이 성공하면 반복 종료
        except IOError as e:
            print(f"Error saving file: {e}")
            print("Please enter a valid path.")

if __name__ == "__main__":
    main()
