import cv2
import sys
import pytesseract
from matplotlib import pyplot as plt

if __name__ == '__main__':

  if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)
