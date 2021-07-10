import cv2
import numpy as np

from PIL import ImageFont,ImageDraw,Image
f = open("participants.txt","r")
names = f.read().split('\n')

f1 = open("coordinates.txt","r")
coordinates = f1.read().split('\n')

flag = True

for i in range(len(names)):
    nametoprint = names[i]
    datep = "10.07.2021"

    img = cv2.imread('template.jpg')
    convertedimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    pilim = Image.fromarray(convertedimg)
    draw=ImageDraw.Draw(pilim)
    font=ImageFont.truetype("fonts/MLSJN.ttf",40)
    font1 = ImageFont.truetype("fonts/TrajanPro-Regular.ttf", 20)

    draw.text((int(coordinates[0]),int(coordinates[1])),nametoprint,font=font,fill='black')
    draw.text((int(coordinates[2]), int(coordinates[3])),datep,font=font1,fill='black')

    cv2processed=cv2.cvtColor(np.array(pilim),cv2.COLOR_RGB2BGR)

    if flag:
        cv2.imshow('Certificate',cv2processed)
        flag=False
    path=''
    cv2.imwrite('./certificates/'+nametoprint+'.png',cv2processed)
    cv2.waitKey(0)

    cv2.destroyAllWindows()








