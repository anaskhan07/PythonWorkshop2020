import cv2
vid = cv2.VideoCapture("/home/aiktc/Desktop/anas/car.mp4")
# print(type(vid))

check = True

while check:
    check, frame = vid.read()
    # cv2.imshow("vid frame", frame)
    f_cascade = cv2.CascadeClassifier("cars.xml")
    img = frame
    grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(grey_img,scaleFactor = 1.05,minNeighbors = 1)

    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(69,69,69),2)


    resized = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
    cv2.imshow("video",resized)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
cv2.waitKey(1)
cv2.destroyAllWindows()

vid.release()
# print(frame_count)
# print(type(check))
# print(frame)
