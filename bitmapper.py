import os
from PIL import Image

def convert_to_bitmap(image_path, output_folder):
    try:
        img = Image.open(image_path)
        img = img.resize((32, 32))  # Resize image to 32x32 pixels
        file_name = os.path.splitext(os.path.basename(image_path))[0] + '.bmp'
        output_path = os.path.join(output_folder, file_name)
        img.save(output_path, format='BMP')
        print(f"Converted {image_path} to {output_path}")
    except Exception as e:
        print(f"Failed to convert {image_path}: {e}")

def convert_images_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')):
            image_path = os.path.join(input_folder, file_name)
            convert_to_bitmap(image_path, output_folder)

# Example usage
if __name__ == '__main__':
    input_folder = 'data/images'  # Folder containing the original images
    output_folder = 'data/visual_data'  # Folder to save the bitmap images

    convert_images_in_folder(input_folder, output_folder)
