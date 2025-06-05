import cv2
import imutils
redLower=(15,164,162)
redUpper=(45,232,255)
camera=cv2.VideoCapture(1)
while True:
    (grabbed,frame)=camera.read()
    frame=imutils.resize(frame,width=600)
    blurimg=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurimg,cv2.COLOR_BGR2HSV)
    mask=cv2.inrange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts=cv2.findContours(mask,cv2.RETR_EXTERNAL,CHAIN_APPROX_SIMPLEX)[-2]
    center=None
    if len(cnts)>0:
        c=cv2.max(cnts,key=contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius > 250:
                print("stop")
            else:
                if(center[0]<100):
                    print("left")
                elif(center[0]<250):
                    print("right")
                elif(radius>450):
                    print("front")
                else:
                    print("stop")
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)&0xff
    if key==ord("q"):
        break
camera.relase()
cv2.destroyAllWindows()
    
                    
