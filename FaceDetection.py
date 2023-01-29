import cv2 # import openCV

def selectNextCamera(currentIndex = -1):
    '''
    Loads next camera and if there is no available camera at next index, set it to the first one
    '''
    index = currentIndex + 1
    nextCam = cv2.VideoCapture(index)
    if (nextCam.isOpened):
        ret, _ = nextCam.read()
        if ret:
            return index, nextCam
        
        return 0, cv2.VideoCapture(0)
        
alg = 'haarcascade_frontalface_default.xml'  # accessed the model file

cascade = cv2.CascadeClassifier(alg) # loading the model with cv2

cameraIndex = None
cameraIndex, cam = selectNextCamera()  # initialization camera
Q_KEY, F2_KEY, ENTER_KEY = 81, 113, 13

while True:
    
    _,img = cam.read() # read the frame from the camera
    
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converting color into gray scale image

    face = cascade.detectMultiScale(grayImg) # get coordinates of face

    for (x, y, w, h) in face: # segregating x,y,w,h
        
        cv2.rectangle(img, (x, y), (x + w, y + h),(0,255,0),2) # draw the retangle

    cv2.imshow("FaceDetect",img)

    key = cv2.waitKey(1)

    if key == Q_KEY or key == F2_KEY : 
        break
    if key == ENTER_KEY: # switch to next camera by pressing Enter
        cameraIndex, cam = selectNextCamera(cameraIndex)  # select next available camera

cam.release()
cv2.destroyAllWindows()
        

    

 

