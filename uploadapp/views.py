from django.shortcuts import render
from .models import User
from django.core.files.storage import FileSystemStorage
import re
import cv2
import pytesseract
from django.conf import settings
from django.http import JsonResponse
def index(request):
    return render(request,'index.html')



def uploadImage(request):
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    

    pi = request.FILES['image']
    fs = FileSystemStorage()
    print("request handling...")
    fs.save(pi.name,pi)
    img=cv2.imread(settings.MEDIA_ROOT+'\\'+pi.name)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #print(pytesseract.image_to_boxes(img))
    himg , wimg, _ = img.shape

    boxes = pytesseract.image_to_data(img)

    print(boxes)
    for x,b in enumerate(boxes.splitlines()) :
        if x!=0:
            b = b.split()
            if len(b)==12:
                if isValidPanCardNo(b[11]):
                    print(b[11])  
                    pno = b[11]              
    #            x,y,w,h = int (b[6]),int (b[7]),int (b[8]),int (b[9])
    #            cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,255),3)
    #            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
    print(img.shape)
    print(pi.name)
    print(pi.size)
    #return render(request,'index.html')
    return JsonResponse({
        "pan number" : pno
    })
# Create your views here.

def isValidPanCardNo(panCardNo):
 
    # Regex to check valid 
    # PAN Card number
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
 
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the PAN Card number 
    # is empty return false
    if(panCardNo == None):
        return False
 
    # Return if the PAN Card number 
    # matched the ReGex 
    if(re.search(p, panCardNo) and
       len(panCardNo) == 10):
        return True
    else:
        return False