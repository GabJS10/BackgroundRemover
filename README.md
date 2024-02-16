# Background Remover

Background Remover is a Python application designed to remove backgrounds from images using the rembg library.

## Features

- **Background Removal**: Removes backgrounds from images in JPEG and PNG formats.
- **Batch Processing**: Processes multiple images in a specified input folder and saves the processed images in an output folder.
- **Original Image Backup**: Moves original images to a separate folder for backup.

## Technologies Used

- Python
- rembg library

## Installation

1. Clone this repository: `git clone <repository URL>`
2. Install dependencies: `pip install rembg`

## Usage

1. Place the images you want to process in the `input` folder.
2. Run the script `background_remover.py`.
3. The processed images with removed backgrounds will be saved in the `output` folder.
4. Original images will be backed up in the `output/originals` folder.

## Example

Suppose you have the following directory structure:

.
├── background_remover.py
├── input
│ ├── image1.jpg
│ ├── image2.png
│ └── ...
└── output
└── ...


After running the script, the `output` folder will contain the processed images with removed backgrounds in the `2024-02-16 12-00-00` subfolder, and the original images will be backed up in the `originals` subfolder.

