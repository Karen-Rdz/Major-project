import numpy as np 
import cv2

filemane = 'chess.jpg'
img = cv2.imread (filemane)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5,5), (-1,-1), criteria)

res = np.hstack((centroids, corners))
res = np.int0(res)

img[res[:,1], res[:, 0]] = [0,0,255]
img [res[:,3], res[:,2]] = [0,255,0]

cv2.imwrite('Subpixel.jpg', img)