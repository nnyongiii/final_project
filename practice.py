class ImageFilterLibrary:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.filters = {
            "blur": self.apply_blur,
            "contour": self.apply_contour,
            "sharpen": self.apply_sharpen,
        }


      def save_image(self, save_path):
            self.image.save(save_path)
            print(f"Image saved to {save_path}")

def main():
    print("Welcome to Image Filter Library")
    image_path = input("Enter the path of the image: ")
    if not os.path.exists(image_path):
        print("File does not exist.")
        return
    
    library = ImageFilterLibrary(image_path)
    print("Available filters:", ", ".join(library.filters.keys()))
    filter_name = input("Enter the filter you want to apply: ")

    try:
        filtered_image = library.apply_filter(filter_name)
        filtered_image.show()
        save_path = input("Enter the path to save the filtered image: ")
        library.save_image(save_path)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
