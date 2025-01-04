# Image Viewer Application

## Project Name: Image Viewer

This Python-based Image Viewer allows users to browse through images with various functionalities, such as forward/backward navigation, shuffle, slideshow, saving and retrieving collections of images. The application is built using **Tkinter** for the GUI and **Pillow** (PIL) for handling image operations.

---

## Repository

- GitHub: [Image Viewer on GitHub](https://github.com/jeet0474/Image_Viewer_Application)

---

## Related Documentation

- **Tkinter Documentation**: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- **Pillow (PIL) Documentation**: [https://pillow.readthedocs.io/en/stable/](https://pillow.readthedocs.io/en/stable/)
- **PyInstaller Documentation**: [https://pyinstaller.readthedocs.io/en/stable/](https://pyinstaller.readthedocs.io/en/stable/)

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Features

### Core Features
1. **Image Navigation**: Move forward and backward through the loaded images.
2. **Shuffle Images**: Shuffle the order of images.
3. **Slideshow Mode**: Display images in full-screen slideshow mode with customizable intervals.
4. **Keyboard Shortcuts**:
   - Left Arrow: Show the previous image.
   - Right Arrow: Show the next image.
   - Escape Key: Exit slideshow mode.
5. **Menu Options**:
   - **New**: Reset the image list.
   - **Open**: Add images to the current image list.
   - **Slideshow**: Start the slideshow with the loaded images.

### Advanced Features
1. **Save Collections**:
   - Users can save the current image paths as a named collection in a specified directory (`saved_collection`).
   - Saved collections are stored in text files, and users can name them during the saving process.
   - Existing collections are listed for reference in the save dialog.

2. **Retrieve Collections**:
   - Users can retrieve and reload image paths from previously saved collections.
   - A dialog displays all available collections for easy selection.
   - Once a collection is loaded, the images can be navigated, shuffled, or displayed in a slideshow.

---

## Requirements

Before running the application, ensure that the following Python packages are installed:

- **Tkinter**: GUI toolkit (usually comes pre-installed with Python).
- **Pillow**: Python Imaging Library (PIL fork) for image handling.

You can install Pillow using pip:
```bash
pip install pillow
```

---

## How to Run the Application

### 1. Clone the repository or download the Python script (`image_viewer.py`).

### 2. Install the necessary dependencies.
If you haven't installed **Pillow**, use the following command:
```bash
pip install pillow
```

### 3. Run the Application
You can run the application directly using Python:
```bash
python image_viewer.py
```
This will open a window with the image viewer and allow you to interact with it.

---

## How to Build an Executable with PyInstaller

To convert the Python script into a standalone executable, use **PyInstaller**. This will package the application into a `.exe` file (on Windows) or the appropriate executable for your operating system.

### 1. Install PyInstaller

If you don't have **PyInstaller** installed, install it using pip:
```bash
pip install pyinstaller
```

### 2. Generate the Executable

Run the following command in your terminal or command prompt to generate a single executable file:
```bash
pyinstaller --onefile --clean --noconsole --icon=view.ico --exclude-module numpy image_viewer.py
```

#### Explanation of the command:
- `--onefile`: Package the entire application into a single executable file.
- `--clean`: Clean temporary files before building the executable.
- `--noconsole`: Run the application without opening a console window (useful for GUI applications).
- `--icon=view.ico`: Set a custom icon for the application. Replace `view.ico` with the path to your icon file.
- `--exclude-module numpy`: Exclude the `numpy` module (if not needed), but if users need it for future updates, they can remove the this part.

### 3. Locate the Executable

After running the above command, PyInstaller will generate the executable in the `dist` directory inside your project folder.

- **Windows**: The executable will be in the `dist` folder as `image_viewer.exe`.
- **macOS/Linux**: The executable will be in the `dist` folder with no file extension (`image_viewer`).

### 4. Run the Executable

Navigate to the `dist` directory and double-click on the executable to run the Image Viewer application.

---

## `.gitignore` Configuration

Add the following `.gitignore` to your project for better repository hygiene:

```
# Byte-compiled files
__pycache__/
*.py[cod]

# PyInstaller specific files
dist/
build/
*.spec

# Virtual environment (if any)
venv/
.env/

# Logs
*.log

# OS generated files
.DS_Store
Thumbs.db

# PyCharm/IDE files
.idea/
.vscode/

# Jupyter notebook checkpoints
.ipynb_checkpoints/
```

---

## Troubleshooting

Refer to the original README for troubleshooting common issues.

---

## Contact

For questions, feel free to reach out to me at [jeet.patel0474@gmail.com].

---

## Example Directory Structure:

```
ImageViewerApp/
│
├── image_viewer.py        # Main Python script
├── view.ico               # Icon file for the application
├── saved_collection/      # Directory to store saved collections
├── dist/                  # Directory where the executable is saved
├── build/                 # Temporary build files generated by PyInstaller
├── .gitignore             # Git ignore file to exclude unnecessary files
└── README.md              # This file
```

---

## Conclusion

With this Image Viewer, you can navigate, shuffle, and view images in a slideshow mode. Additionally, you can now save and retrieve collections of images for later use, making it more versatile. Converting the application into an executable allows for easy sharing without requiring a Python installation. Enjoy!