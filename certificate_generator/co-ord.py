import cv2

f=open("coordinates.txt","w")


def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(img,"coordinates (%d,%d)"%(x,y),(60,60),2,1,(0,255,0))

        f.write(str(x)+"\n")
        f.write(str(y)+"\n")


img = cv2.imread("template.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
f.close()

