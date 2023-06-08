
import cv2 as cv
import pytesseract
import YB_Pcb_Car
import time

car = YB_Pcb_Car.YB_Pcb_Car()

def get_ocr(img):
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('Camera', frame)
    k = cv.waitKey(1)
    if k % 256 == 32:
        text_ocr = get_ocr(frame)
        print(text_ocr)
        if "Sad" in text_ocr:
            print("why")
            car.Ctrl_Servo(2, 20)
            time.sleep(0.5)
            car.Ctrl_Servo(2, 90)
        if "Happy" in text_ocr:
            print("how")
            car.Ctrl_Servo(2, 180)
            time.sleep(0.5)
            car.Ctrl_Servo(2, 90)
    if k % 256 == 27:
        break

cap.release()
cv.destroyAllWindows()