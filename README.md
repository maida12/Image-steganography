# DisguiseGram

The Python Image Steganography project is a GUI based application that enables users to hide a secret message within an image using encoding and decoding functions. The project involves the use of the Tkinter library for creating the GUI and the Pillow module for image manipulation.

## Features


- **Encode**: Embeds text data into an image using both normal and AES encryption methods.
- **Decode**: Extracts hidden text from an encoded image, supporting both normal and AES decryption.
- Password protection
- AES Encrption
- AES dycrption
- Normal Encrption
- Normal dycrption


## Dependencies

- Python 3.x
- Tkinter
- Pillow (PIL)


## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/maida12/Image-steganography.git
    cd Image-Steganography
    ```

2. Install dependencies:

    ```bash
    pip install Pillow
    ```

3. Run the application:

    ```bash
    python main.py
    ```



## Usage

1. Launch the application.
2. Choose between encoding or decoding.
3. Follow the instructions on the GUI to perform the desired operation.
4. Save the resulting image with hidden text.



## Encryption

- Normal Encryption: Simple encoding method.
- AES Encryption: Advanced encryption standard for secure data hiding.




## Screenshots

![App Screenshot](https://github.com/maida12/Image-steganography/assets/81500487/b7254e18-4843-4694-8040-613fc406c66c)

![App Screenshot](https://github.com/maida12/Image-steganography/assets/81500487/6901edef-a575-43a1-8fec-a5673aeaea4c)



## Steganalysis with LSB Detection

This project not only enables you to hide data within images but also provides a Steganalysis feature to detect hidden information. The `show_lsb` function utilizes the LSB method to reveal the n least significant bits of an image.

### Steganalysis Example

You can use the `show_lsb` function by providing the image file path and the number of least significant bits to reveal. 

![three-lotus-steg-with-2LSBs](https://github.com/maida12/Image-steganography/assets/81500487/eba912b3-8e03-49bf-85f4-7fb6d7ed88be)

![flower-purple-lical-blosso](https://github.com/maida12/Image-steganography/assets/81500487/71aa6dd7-b9a6-4b9e-869e-007817d900cb)
![flower-purple-lical-blosso_1LSBs](https://github.com/maida12/Image-steganography/assets/81500487/0f5d57b8-c121-4dcd-b960-57833663bc4c)


## Acknowledgments

- This project was inspired by [DataFlair's Python Image Steganography project](https://data-flair.training/blogs/python-image-steganography-project/).



## License

This project is licensed under the [MIT License](LICENSE).
