'''#! pip install pillow
#! pip install opencv-python
#! pip install pypng
#! pip install cv
#! pip install segno
#! pip install qrcode-artistic

##REMOVE THIS AND THE PROGRAM RUNS PERFECT!!!
'''















def creating_qr_code_WITH_USER_INPUTTED_VALUES():
    alpha=ord(useralpha)
    for i in range (n,m+1):
        name=chr(alpha)+ str(i)
        qr = segno.make('THE ID OF THIS PRODUCT IS : '+name,micro=False, mask=7)
        img = qr.to_pil(scale=30, 
                    border=0,
                    dark=(218,84,105),
                    light='white',
                    finder_dark='gray',
                    alignment_dark=(218,84,105),
                    data_dark=(218,84,105)
                    )
        img.save('./QRCODES/'+name+' finalQR.png')
        
        if i % max_no_bags==0:
            alpha=alpha+1
           
        
        # ADDING BACKGROUND DESIGN
        im1 = Image.open('./RESOURCES/background.jpg')
        im2 = Image.open('./QRCODES/'+name+' finalQR.png')
        
        back_im = im1.copy()
        back_im.paste(im2,(241,226))
        back_im.save('./QRCODES/'+name+' finalQR.png', quality=100)
        
        
        #RESIZING THE QRCODE
        
        basewidth = 70
        img = Image.open('./QRCODES/'+name+' finalQR.png')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save('./QRCODES/'+name+' finalQR.png',quality=100)


        #ADDING QR CODE TO THE BAG IMAGE
        j=(a-1)+i
        bag_img_name=str(initial)+str(j)                          #CAN BE EDITED BASED ON SITUATION
        im1 = Image.open('./Bag Images/'+bag_img_name+'.jpg')
        im2 = Image.open('./QRCODES/'+name+' finalQR.png')
        back_im = im1.copy()
        pos = (im1.size[0] - im2.size[0], im1.size[1] - im2.size[1])
        back_im.paste(im2,pos)
        back_im.save('./OUTPUT/'+name+'.png', quality=1000)    
        
    
    


################################################################################################################################

#FINALLY CALLING ALL FUNCTIONS

# importing the required modules

#import pyqrcode
from PIL import Image,ImageOps
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import segno
#import pillow


print("Enter 1 if you want to manually enter data which is to be written in the QR code")
print()
print("Enter 2 if you want to automatically enter data in the QR code using the database")
print()
ch_during_creating_qr_code=int(input("Enter your choice(1/2):"))
if ch_during_creating_qr_code==1:
    print()
    print()
    print("GETTING DATA TO BE ENCRYPTED ON THE QR CODE...........")
    print()
    n=int(input("Enter the no to be printed on 1st QR code:"))
    m=int(input("Enter the no to be printed on last QR code:"))
    useralpha1=input("Enter Alphabet to be printed on the 1st QR code:")
    useralpha=useralpha1.upper()
    print()
    print()
    max_no_bags=int(input("Enter max no of bags that can fit into the BIG bag:"))
    print()
    print()
    print("GETTING THE DETAILS OF THE FILE NAME ON WHICH QR CODE IS TO BE ADDED ")
    print()
    initial=input("Enter the initial word of the file name (eg. if file name is 'download1' then  you should enter: download) : ")
    print()
    a=int(input("Enter the NUMBER on the file name of the bag image on which you want to add the 1st QR code(eg. if file name is 'download1' then you should enter: 1) :"))
    
    
    creating_qr_code_WITH_USER_INPUTTED_VALUES()
    print("QR codes created and added sucessfully.........")

    

elif ch_during_creating_qr_code==2:
    creating_qr_code_AUTOMATICALLY_USING_DATABASE()

