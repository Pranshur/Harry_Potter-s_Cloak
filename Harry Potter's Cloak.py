import cv2
import numpy as np

def func(a):
    pass

cv2.namedWindow("Editing Tools")
cv2.createTrackbar("Minimum Hue", "Editing Tools", 0, 179, func)
cv2.createTrackbar("Maximum Hue", "Editing Tools", 179, 179, func)
cv2.createTrackbar("Minimum Saturation", "Editing Tools", 115, 255, func)
cv2.createTrackbar("Maximum Saturation", "Editing Tools", 255, 255, func)
cv2.createTrackbar("Minimum Value", "Editing Tools", 55, 255, func)
cv2.createTrackbar("Maximum Value", "Editing Tools", 200, 255, func)
vid=cv2.VideoCapture(0)
kernel=np.ones((3, 3))

while True:
    cv2.waitKey(1000)
    ret, init_frame=vid.read()
    if ret:
        break

while True:
    success, frame=vid.read()
    minHue=cv2.getTrackbarPos("Minimum Hue", "Editing Tools")
    maxHue=cv2.getTrackbarPos("Maximum Hue", "Editing Tools")
    minSat=cv2.getTrackbarPos("Minimum Saturation", "Editing Tools")
    maxSat=cv2.getTrackbarPos("Maximum Saturation", "Editing Tools")
    minVal=cv2.getTrackbarPos("Minimum Value", "Editing Tools")
    maxVal=cv2.getTrackbarPos("Maximum Value", "Editing Tools")

    min=np.array([minHue, minSat, minVal])
    max=np.array([maxHue, maxSat, maxVal])

    mask=cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), min, max)
    mask=cv2.erode(mask, kernel, iterations=5)
    mask=cv2.dilate(mask, kernel, iterations=5)
    mask_inv=255-mask

    b=frame[:, :, 0]
    g=frame[:, :, 1]
    r=frame[:, :, 2]

    b=cv2.bitwise_and(mask_inv, b)
    g=cv2.bitwise_and(mask_inv, g)
    r=cv2.bitwise_and(mask_inv, r)

    frame_inv=cv2.merge((b, g, r))

    b=init_frame[:, :, 0]
    g=init_frame[:, :, 1]
    r=init_frame[:, :, 2]

    b=cv2.bitwise_and(mask, b)
    g=cv2.bitwise_and(mask, g)
    r=cv2.bitwise_and(mask, r)
    
    cloth_area=cv2.merge((b, g, r))

    final=cv2.bitwise_or(frame_inv, cloth_area)


    # cv2.imshow("Frame", frame)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Frame Inverse", frame_inv)
    # cv2.imshow("Cloth Area", cloth_area)
    cv2.imshow("Harry Potter's Cloak", final)
    if cv2.waitKey(1):
        continue
