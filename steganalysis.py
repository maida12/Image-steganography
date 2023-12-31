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