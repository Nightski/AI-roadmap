import cv2
from pyzbar import pyzbar
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help=r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\MLwork\image.jpg")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])

barcodes = pyzbar.decode(img)

for barcode in barcodes:
    (x,y,w,h) = barcode.rect
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    bdata = barcode.data.decode("utf-8")
    btype = barcode.type

    text = "{} ({})".format(bdata, btype)
    cv2.putText(img, text,(x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)

    print("[info] found {} barcode: {}".format(btype, bdata))

cv2.imshow("image", img)
cv2.waitKey(0)