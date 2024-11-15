import os
import sys
import argparse
from PIL import Image
from tqdm import tqdm
from colorama import Fore, Style



def increase_background_area(image_path, output_path, increase_pixels):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            max_dim = max(width, height)
            if increase_pixels is None:
                increase_pixels = max_dim - min(width, height)

            # Determine the new dimension to make the image square
            new_dim = max(width, height)
            if width != height:
                square_img = Image.new("RGBA", (new_dim, new_dim), (255, 255, 255, 0))
                offset = ((new_dim - width) // 2, (new_dim - height) // 2)
                square_img.paste(img, offset)
            else:
                square_img = img

            # Add the specified pixels to the background
            new_size = new_dim + increase_pixels
            final_img = Image.new("RGBA", (new_size, new_size), (255, 255, 255, 0))
            offset = ((new_size - square_img.width) // 2, (new_size - square_img.height) // 2)
            final_img.paste(square_img, offset)

            final_img.save(output_path)
            print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Processed image saved as {output_path}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to process {image_path}: {e}")


def process_images(input_folder, increase_pixels):
    if not os.path.exists(input_folder):
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} The folder {input_folder} does not exist.")
        return

    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    if not png_files:
        print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} No PNG files found in {input_folder}.")
        return

    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Starting image processing...")
    
    for file_name in tqdm(png_files, desc="Processing images", unit="image", total=len(png_files)):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"processed_{file_name}")
        increase_background_area(input_path, output_path, increase_pixels)
    
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Image processing completed.")


def main():
    parser = argparse.ArgumentParser(
        description="""
        PNG Background Increaser
        ------------------------
        A command-line utility to increase the transparent background area of PNG images.
        
        Usage Examples:
        ---------------
        1. Process a single PNG file:
           python png_background_increaser.py input.png -p 50
           
        2. Process all PNG files in a folder:
           python png_background_increaser.py input_folder -f -p 50
        
        Options:
        --------
        -f, --folder   : Indicates that the input is a folder containing PNG files.
        -p, --pixels   : Number of pixels to increase the background area.
        
        Notes:
        ------
        - The output images are saved in an 'output' folder within the input directory.
        - The program ensures the main design remains unchanged while increasing the background.
        
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help="Path to a PNG file or a folder containing PNG files")
    parser.add_argument('-f', '--folder', action='store_true', help="Indicate that the input is a folder")
    parser.add_argument('-p', '--pixels', type=int, help="Number of pixels to increase the background area")
    args = parser.parse_args()

    if args.folder:
        process_images(args.input, args.pixels)
    else:
        if not args.pixels:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Pixel value is required for a single file.")
            sys.exit(1)
        output_file = os.path.join(os.path.dirname(args.input), f"processed_{os.path.basename(args.input)}")
        increase_background_area(args.input, output_file, args.pixels)


if __name__ == "__main__":
    main()
