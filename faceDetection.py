import cv2

img = cv2.imread("images.jpeg",0)
cv2.imshow("Legend",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
