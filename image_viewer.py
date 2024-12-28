import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import random
import base64
from io import BytesIO
import os
import sys


class Slideshow:
    def __init__(self, root, images):
        # Initialize slideshow window
        self.root = tk.Toplevel(root)
        self.root.attributes("-fullscreen", True)  # Make it fullscreen
        self.images = images
        self.current_index = 0
        self.running = True
        self.parent = root  # Reference to the main window

        # Label to display images in the slideshow
        self.image_area = tk.Label(self.root, bg="black")
        self.image_area.pack(fill=tk.BOTH, expand=True)

        # Ensure the slideshow window is in focus
        self.root.focus_set()

        # Ask the user for the slideshow interval (in seconds)
        self.interval = self.get_slideshow_interval()

        # Bind the Escape key to exit fullscreen mode
        self.root.bind("<Escape>", self.exit_fullscreen)

        # Start the slideshow by showing the first image
        self.show_image(self.current_index)
        self.schedule_next_image()

    def get_slideshow_interval(self):
        """Prompt the user to enter the slideshow interval."""
        try:
            # Ask user for the interval in seconds
            interval = simpledialog.askinteger(
                "Slideshow Interval",
                "Enter the time (in seconds) for each slide:",
                minvalue=1,
                maxvalue=60,
                parent=self.root,  # Attach dialog to slideshow window
            )
            return interval if interval else 3  # Default to 3 seconds if no input
        except Exception:
            return 3  # Fallback to default interval

    def show_image(self, index):
        """Display the current image based on index."""
        try:
            image_path = self.images[index]
            image = Image.open(image_path)

            # Get the screen dimensions for resizing the image
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # Resize image to fit screen size
            image.thumbnail((screen_width, screen_height))
            self.current_image = ImageTk.PhotoImage(image)

            # Update the label with the image
            self.image_area.config(image=self.current_image)
        except Exception as e:
            # Display error if the image can't be loaded
            messagebox.showerror("Error", f"Failed to load image: {e}")
            self.exit_fullscreen()

    def schedule_next_image(self):
        """Schedule the next image after the current interval."""
        if self.running and self.images:
            # Update index to show the next image
            self.current_index = (self.current_index + 1) % len(self.images)
            self.root.after(self.interval * 1000, self.show_next_image)  # Delay in ms

    def show_next_image(self):
        """Show the next image and schedule the next frame."""
        if self.running:
            self.show_image(self.current_index)
            self.schedule_next_image()

    def exit_fullscreen(self, event=None):
        """Stop the slideshow and exit fullscreen mode."""
        self.running = False
        self.root.destroy()  # Close the slideshow window
        self.parent.focus_force()  # Return focus to the main window


class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.state("zoomed")  # Start window maximized
        self.root.minsize(800, 600)  # Set minimum window size
        
        # Set the custom window icon
        self.set_window_icon()

        # Initialize image list and index
        self.array_images = []
        self.current_image_index = 0

        # UI Setup
        self.setup_menu()
        self.setup_layout()

        # Bind keyboard shortcuts for navigation
        self.root.bind("<Left>", lambda event: self.show_previous_image())  # Left arrow
        self.root.bind("<Right>", lambda event: self.show_next_image())  # Right arrow
        
    def set_window_icon(self):
        """Set the window icon using an embedded base64 string."""
        icon_base64 = self.get_icon_data()  # Use the icon data from the method

        try:
            # Decode the base64 string to binary data
            icon_data = base64.b64decode(icon_base64)

            # Convert the binary data into an Image object
            icon_image = Image.open(BytesIO(icon_data))
            icon_image = ImageTk.PhotoImage(icon_image)

            # Set the window icon
            self.root.iconphoto(True, icon_image)
        except Exception as e:
            print(f"Error setting window icon: {e}")
    
    def get_icon_data(self):
        """Retrieve the base64 encoded icon data."""
        try:
            # Get the correct path to the icon file, whether running in development or as a packaged app
            if getattr(sys, 'frozen', False):
                # Running in a bundled executable
                icon_path = os.path.join(sys._MEIPASS, 'view.ico')
            else:
                # Running in a script (development mode)
                icon_path = 'view.ico'
            
            # Open the icon file and encode it to base64
            with open(icon_path, 'rb') as icon_file:
                icon_data = base64.b64encode(icon_file.read()).decode('utf-8')
            return icon_data
        except Exception as e:
            print(f"Error loading icon: {e}")
            return None


    def setup_menu(self):
        """Set up the menu bar with options."""
        self.menu_bar = tk.Menu(self.root)

        # Add "New" command to reset the image list
        self.menu_bar.add_command(label="New", command=self.reset_images)

        # Add "Open" command to allow the user to add images
        self.menu_bar.add_command(label="Open", command=self.add_images)

        # Add "Slideshow" command to start the slideshow
        self.menu_bar.add_command(label="Slideshow", command=self.start_slideshow)

        # Configure the root window to use the menu
        self.root.config(menu=self.menu_bar)

    def setup_layout(self):
        """Set up the main layout of the application."""
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Label to display the current image
        self.image_area = tk.Label(
            self.main_frame, text="No Image Loaded", bg="gray", fg="white"
        )
        self.image_area.pack(fill=tk.BOTH, expand=True)

        # Bottom frame to hold navigation buttons
        self.bottom_frame = tk.Frame(self.root, bg="lightgray", height=50)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.setup_bottom_buttons()

    def setup_bottom_buttons(self):
        """Set up navigation buttons at the bottom of the window."""
        # Clear previous buttons if any
        for widget in self.bottom_frame.winfo_children():
            widget.destroy()

        # Navigation buttons: Backward, Forward, Shuffle
        self.back_button = tk.Button(
            self.bottom_frame, text="Backward", command=self.show_previous_image
        )
        self.forward_button = tk.Button(
            self.bottom_frame, text="Forward", command=self.show_next_image
        )
        self.shuffle_button = tk.Button(
            self.bottom_frame, text="Shuffle", command=self.shuffle_images
        )

        # Pack the buttons into the bottom frame
        self.back_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.forward_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.shuffle_button.pack(side=tk.LEFT, padx=5, pady=5)

    def reset_images(self):
        """Clear the image list and reset the display."""
        self.array_images = []
        self.current_image_index = 0
        self.image_area.config(image="", text="No Image Loaded")
        messagebox.showinfo("Reset", "Image list cleared.")

    def add_images(self):
        """Allow the user to add images to the list."""
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")],
        )
        if file_paths:
            # Add selected images to the list
            self.array_images.extend(file_paths)
            messagebox.showinfo(
                "Success", f"{len(file_paths)} images added successfully."
            )
            self.current_image_index = 0
            self.show_image(self.current_image_index)

    def show_image(self, index):
        """Display an image at the given index."""
        if not self.array_images:
            self.image_area.config(image="", text="No Image Loaded")
            return

        try:
            # Open the image and fit it within the available area
            image_path = self.array_images[index]
            image = Image.open(image_path)

            # Get the size of the image area
            area_width = self.image_area.winfo_width()
            area_height = self.image_area.winfo_height() - self.bottom_frame.winfo_height()

            # Resize the image to fit
            image.thumbnail((area_width, area_height))

            # Convert the image to a format tkinter can use
            self.current_image = ImageTk.PhotoImage(image)
            self.image_area.config(image=self.current_image, text="")
        except Exception as e:
            # Show an error if the image fails to load
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def show_next_image(self):
        """Show the next image in the list."""
        if not self.array_images:
            return
        self.current_image_index = (self.current_image_index + 1) % len(self.array_images)
        self.show_image(self.current_image_index)

    def show_previous_image(self):
        """Show the previous image in the list."""
        if not self.array_images:
            return
        self.current_image_index = (self.current_image_index - 1) % len(self.array_images)
        self.show_image(self.current_image_index)

    def shuffle_images(self):
        """Shuffle the image list and display the first image."""
        if self.array_images:
            random.shuffle(self.array_images)
            self.current_image_index = 0
            self.show_image(self.current_image_index)

    def start_slideshow(self):
        """Start the slideshow if images are available."""
        if not self.array_images:
            messagebox.showinfo("No Images", "Please load images to start the slideshow.")
            return
        Slideshow(self.root, self.array_images)


# Main execution block
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
