# PNG Background Increaser

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

PNG Background Increaser is a command-line utility designed to increase the transparent background area of PNG images without altering the main design. It ensures that the output images are square and can handle both single files and bulk processing within folders.

## Features

- Increase the transparent background of PNG images.
- Maintain the original design without scaling.
- Process single images or entire folders.
- Save processed images in an `output` folder.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/OCEANOFANYTHINGOFFICIAL/python-png-background-increaser.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-png-background-increaser
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Single File

To process a single PNG file and increase its background:

```bash
python png_background_increaser.py path/to/image.png -p 50
```

### Folder

To process all PNG files in a folder:

```bash
python png_background_increaser.py path/to/folder -f -p 50
```

## Options

- `-f`, `--folder`: Indicates the input is a folder.
- `-p`, `--pixels`: Number of pixels to increase the background area.

## Example

```bash
# Increase background of a single image by 50 pixels
python png_background_increaser.py my_image.png -p 50

# Increase background of all images in a folder by 100 pixels
python png_background_increaser.py my_folder -f -p 100
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
