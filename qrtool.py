from PIL import Image
from pyzbar.pyzbar import decode
import qrcode
import os

def decode_qrcode(image_path):
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)

        if not decoded_objects:
            print("No QR code found in the image.")
            return

        for i, obj in enumerate(decoded_objects):
            data = obj.data.decode("utf-8")
            print(f"{data}")

    except Exception as e:
        print(f"Failed to decode image: {e}")

def generate_qrcode(data, output_path="generated_qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    print(f"QR Code generated and saved to: {output_path}")

def main():
    action = input("What do you want to do? (1 = decode QRcode / 2 = generate QRcode): ").strip().lower()

    if action == "1":
        image_path = input("Enter the image path: ").strip()
        if not os.path.isfile(image_path):
            print("File not found.")
            return
        decode_qrcode(image_path)

    elif action == "2":
        data = input("Enter the text or URL to encode: ").strip()
        output_path = input("Enter output file name (or press Enter for default): ").strip()
        if output_path == "":
            generate_qrcode(data)
        else:
            generate_qrcode(data, output_path)

    else:
        print("Invalid action. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
