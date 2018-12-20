#setup
import scipy.misc 
from cv2 import selectROI, imread
import shlex
from numpy import asarray
from PIL import Image
from pytesseract import image_to_string
from os import listdir ,path
from os.path import join
from tkinter import filedialog
from tkinter import Tk
from subprocess import check_output
from time import sleep
try:
    import formStore 
except ModuleNotFoundError:
    print('formstore.py file not found')
    sleep((2)
    print('a new store will be made')


#global variable declaration
skip=[]
preProcessConstant=100
fields_to_collect=['name','country']
submissions={}
n=''
halp="""
Type Folder() after the \'>>>\' to upload the text from all image files in a particular folder and press enter

Type File() after the \'>>>\' to upload the text from some images in a particular folder and press enter

Type exit after the\'>>>\' to close the python terminal and press enter
"""


#Function Definitons
def ROIselector(picture,item):
    if __name__ == '__main__' :
        # Select ROI
        showCrosshair = False
        fromCenter = False
        r = selectROI(item, picture, fromCenter, showCrosshair)
        # Crop image
        imCrop = picture[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        # Display cropped image
    return imCrop
    
def Tesseract(img):
    return image_to_string(img)

def preProcess(img_path,foldername="/home/neil/wordpress/output"):
    img=imread(img_path)
    arr=asarray(img)
    for i in range(3):
        arr[arr[:,:,i]<preProcessConstant]=asarray(0)
        arr[arr[:,:,i]!=0]=asarray(255)
    scipy.misc.imsave(str(foldername)+"output.jpg")
    img=imread(str(foldername)+"output.jpg")
    return img


def MainProcess():
    reviewAfterEveryFile=input('Do you want to review the information collected after each file is finished?(y/n') 
    if reviewAfterEveryFile not in ['y','n']:
        raise Exception('Something other than \'y\' or \'n\' was input')
    root = Tk()
    root.filename =  filedialog.askdirectory(parent=root,initialdir="/home/neil/Desktop",title='Please select a directory')
    foldername=str(root.filename)
    folder_all=listdir(root.filename)
    imgs=[img for img in folder_all if img[-3:]=='jpg']
    img_paths=[join(root.filename,img) for img in imgs]
    for img_path in img_paths:
        img=preProcess(img_path)
        fieldStore={}
        for item in fields_to_collect:
            imageText=Tesseract(ROIselector(img,item))
            print("Is the following correct:")
            print(item+": "+imageText)
            confirmation=input()
            if confirmation=='y'or confirmation=='Y':
                fieldStore[item]=imageText
            else: 
                if confirmation=='n' or confirmation=='N':
                    imageText=input('enter correct value of field')
                    fieldStore[item]=imageText
                else:
                    raise Exception('Something other than y or n was input')

        intermediate_field_store={img_path:fieldStore}
        if reviewAfterEveryFile=='y':
            print('The data collected so far is:')
            for field in fields_to_collect:
                print(field+": "+str(intermediate_field_store[img_path][field]))
            confirmation=input('Is the data correct?(y/n)')
            if confirmation=='y':
                submissions.update(intermediate_field_store)
                intermediate_field_store={}
            else:
                if confirmation=='n':
                    intermediate_field_store={}
                    skip.append(img_path)
                else:
                    raise Exception('Something other than y or n was input')
        else:
            submissions.update(intermediate_field_store)
            intermediate_field_store={}
    process=check_output('rm '+str("/home/neil/wordpress/output")+"output.jpg",shell=True)
    print(done)

def Files():
    reviewAfterEveryFile=input('Do you want to review the information collected after each file is finished?(y/n') 
    if reviewAfterEveryFile not in ['y','n']:
        raise Exception('Something other than \'y\' or \'n\' was input')
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    files=root.filename
    imgs=[img for img in files if img[-3:]=='jpg']
    img_paths=[join(root.filename,img) for img in imgs]
    for img_path in img_paths:
        img=preProcess(img_path)
        fieldStore={}
        for item in fields_to_collect:
            imageText=Tesseract(ROIselector(img,item))
            print("Is the following correct:")
            print(item+": "+imageText)
            confirmation=input()
            if confirmation=='y'or confirmation=='Y':
                fieldStore[item]=imageText
            else: 
                if confirmation=='n' or confirmation=='N':
                    imageText=input('enter correct value of field')
                    fieldStore[item]=imageText
                else:
                    raise Exception('Something other than y or n was input')

        intermediate_field_store={img_path:fieldStore}
        if reviewAfterEveryFile=='y':
            print('The data collected so far is:')
            for field in fields_to_collect:
                print(field+": "+str(intermediate_field_store[img_path][field]))
            confirmation=input('Is the data correct?(y/n)')
            if confirmation=='y':
                submissions.update(intermediate_field_store)
                intermediate_field_store={}
            else:
                if confirmation=='n':
                    intermediate_field_store={}
                    skip.append(img_path)
                else:
                    raise Exception('Something other than y or n was input')
        else:
            submissions.update(intermediate_field_store)
            intermediate_field_store={}
    process=check_output('rm '+str("/home/neil/wordpress/output")+"output.jpg",shell=True)
    print(done)


n=""
while n!= "exit":
    print(">>>",end="")
    n=input()
    try:
        q=shlex.split(n)
    except ValueError:
        print('ValueError: No closing quotation marks')
    if n=='Folder()':
        MainProcess()
    else:
        if n=='Files()':
            Files()
        else:
            if n=='help()':
                print(halp)
            else:
                raise Exception('CommandNotFoundError: \'{}\' command not found'.format(q))
exit()
