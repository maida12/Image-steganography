# import tkinter as tk
# from tkinter import filedialog, messagebox
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from PIL import Image, ImageTk

# class SteganalysisApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Steganalysis App")

#         # Create buttons
#         self.open_button = tk.Button(master, text="Open Image", command=self.open_image)
#         self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_image)

#         # Create canvas for displaying images
#         self.canvas = tk.Canvas(master, width=400, height=400)
#         self.canvas.grid(row=0, column=0, rowspan=3, padx=10)

#         # Place buttons on the window
#         self.open_button.grid(row=0, column=1, pady=10)
#         self.analyze_button.grid(row=1, column=1, pady=10)

#         # Initialize variables
#         self.image_path = None
#         self.image = None

#     def open_image(self):
#         self.image_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg')])
#         if self.image_path:
#             self.image = cv2.imread(self.image_path)
#             self.display_image(self.image)

#     def analyze_image(self):
#         if self.image is not None:
#             histogram = self.calculate_histogram(self.image)
#             self.display_histogram(histogram)
#         else:
#             messagebox.showinfo("Error", "Please open an image first.")

#     def calculate_histogram(self, image):
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         histogram, _ = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])
#         return histogram

#     def display_image(self, image):
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         img_tk = self.convert_image_to_tkinter(image)
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

#     def display_histogram(self, histogram):
#         fig, ax = plt.subplots(figsize=(5, 3), tight_layout=True)
#         ax.plot(histogram, color='black')
#         ax.set_title('Image Histogram')
#         ax.set_xlabel('Pixel Value')
#         ax.set_ylabel('Frequency')

#         canvas = FigureCanvasTkAgg(fig, master=self.master)
#         canvas_widget = canvas.get_tk_widget()
#         canvas_widget.grid(row=2, column=0, columnspan=2, pady=10)

#     @staticmethod
#     def convert_image_to_tkinter(image):
#         image = Image.fromarray(image)
#         img_tk = ImageTk.PhotoImage(image=image)
#         return img_tk


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SteganalysisApp(root)
#     root.mainloop()



from PIL import Image
from time import time
from typing import cast, Tuple, Iterable
import logging
import os

log = logging.getLogger(__name__)


def show_lsb(image_path: str, n: int) -> None:
    """Shows the n least significant bits of image"""
    if image_path is None:
        raise ValueError("StegDetect requires an input image file path")

    start = time()
    with Image.open(image_path) as image:
        # Used to set everything but the least significant n bits to 0 when
        # using bitwise AND on an integer
        mask = (1 << n) - 1

        image_data = cast(Iterable[Tuple[int, int, int]], image.getdata())
        color_data = [
            (255 * ((rgb[0] & mask) + (rgb[1] & mask) + (rgb[2] & mask)) // (3 * mask),) * 3
            for rgb in image_data
        ]

        # TODO: image.putdata() appears to have buggy typing?
        image.putdata(color_data)  # type: ignore
        log.debug(f"Runtime: {time() - start:.2f}s")
        file_name, file_extension = os.path.splitext(image_path)
        image.save(f"{file_name}_{n}LSBs{file_extension}")
        image.show()

# call the function
# show_lsb("C:/Users/fatim/Downloads/Trees-22.png", 1)
# show_lsb("C:/Users/fatim/Desktop/Trees-22.png", 1)
# show_lsb("C:/Users/fatim/Downloads/flower-purple-lical-blosso.jpg", 1)
show_lsb("C:/Users/fatim/Downloads/flower-purple-lical-blosso_encoded.png", 1)