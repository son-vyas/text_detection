import cv2
import sys
import pytesseract
from matplotlib import pyplot as plt

if __name__ == '__main__':


   if len(sys.argv) < 2:


       print('Usage: python ocr_simple.py image.jpg')
       sys.exit(1)
   imPath = sys.argv[1]
   config = ('-l eng --oem 1 --psm 3')

  # Read image from disk
   im = cv2.imread(imPath, cv2.IMREAD_COLOR)
   retval, threshold = cv2.threshold(im,125, 255, cv2.THRESH_BINARY)
   cv2.imshow('threshold',threshold)
   cv2.waitKey(0)

   blur = cv2.bilateralFilter(threshold,9,75,75)
   plt.subplot(122),plt.imshow(threshold)
   plt.xticks([]), plt.yticks([])
   plt.show()

    text = pytesseract.image_to_string(blur, config=config)

  lines=0
  words_dict = {}

  for word in text.split():
      words_dict[word] = words_dict.get(word,0) + 1


  for key in sorted(words_dict):
      print("{} : {}".format(key,words_dict[key]))

  # Print recognized text
  print(text)





