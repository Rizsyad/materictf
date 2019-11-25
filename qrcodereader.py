# brew install zbar for macos
# sudo apt-get install libzbar0 for linux
# pip install pyzbar
# pip install pyzbar[scripts]

from pyzbar.pyzbar import decode
from PIL import Image
import time

def main():
    src_image = raw_input("Masukan file gambar barcode: ")
    time.sleep(2)
    try:
        start_decode = decode(Image.open(src_image))
        for barcode in start_decode:
            barcodeData = barcode.data
            print("Message is", barcodeData)
    except:
        print("cannot be decoded")

if __name__ == '__main__':
    main()
