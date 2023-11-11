import cv2

Black_White = cv2.imread("photo/Black_White.png")
Black_White2 = cv2.imread("photo/Black_White2.png")


imgAnd = cv2.bitwise_and(Black_White , Black_White2 )
cv2.imshow("and " , imgAnd)
cv2.waitKey()
cv2.imwrite("out.png"  , imgAnd )

imgOR = cv2.bitwise_xor(Black_White , imgAnd )
cv2.imshow(" " , imgOR)
cv2.waitKey()
cv2.imwrite("out1.png"  , imgOR )

XORimg = cv2.bitwise_or(imgOR , Black_White2)

cv2.imwrite("out2.png"  , XORimg )
cv2.imshow(" " , XORimg)
cv2.waitKey()