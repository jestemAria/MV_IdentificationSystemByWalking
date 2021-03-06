from cv2 import cv2 as cv

cap = cv.VideoCapture(0)
fore_ground_back_ground = cv.bgsegm.createBackgroundSubtractorMOG()

# Alternatively, you can use the following:
# fore_ground_back_ground = cv.bgsegm.createBackgroundSubtractorGMG()
# fore_ground_back_ground = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fore_ground_maks = fore_ground_back_ground.apply(frame)
    median = cv.medianBlur(fore_ground_maks, 5)
    canny = cv.Canny(median, 100, 200)

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask Frame', median)
    cv.imshow('Canny', canny)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()
