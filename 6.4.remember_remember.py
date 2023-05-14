import os.path


def decode_image(image_path):
    """
    Decodes a message hidden in a black pixel column of a PNG image.
    Args:
    - image_path: The path to the PNG image file.
    Returns:
    - The decoded message as a string.
    """
    # Open the image file with no need to close after
    with Image.open(image_path) as img:
        # Get the width and height of the image
        matrix = img.load()
        width, height = img.size
        black_pixels = []
        for x in range(width):
            for y in range(height):
                pixel = matrix[x, y]
                if pixel == 1:
                    black_pixels.append(y)
                    break
        # Convert the row numbers to characters
        message = ''.join([chr(row) for row in black_pixels])
        return message


def main():
    """
    Main function that loads an image and deciphers the hidden message.

    Prints the deciphered message or an error message if the image file is not found.
    """
    if os.path.exists('resources/code.png'):
        with Image.open('resources/code.png') as image:
            print(decode_image(image))
    else:
        print("Image file not found.")


if __name__ == '__main__':
    main()
