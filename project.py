#setup

from cv2 import selectROI, imread, imwrite, IMREAD_GRAYSCALE
from numpy import asarray
from pytesseract import image_to_string
from os import listdir ,path
from os.path import join
from os import chdir
from os import mkdir
from shutil import copy
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk
from subprocess import check_output
from time import sleep
try:
    import formStore 
except ModuleNotFoundError:
    print('formstore.py file not found')
    sleep(0.5)
    print('a new store will be made')


#global variable declaration
skip=[]
skipVariable=0
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
        showCrosshair = False
        fromCenter = False
        r=(0,0,0,0)
        print(picture)
        print(item)
        while r==(0,0,0,0):
            r=selectROI(item,picture, fromCenter, showCrosshair)
            if r==(0,0,0,0):
                root=Tk()
                root.withdraw()
                skipQuestion=messagebox.askquestion("Retry?","Press Yes to retry selection or press no to skip this image.")
                sleep(1)
                if skipQuestion=='no':
                    skipVariable=1
                    assert skipVariable==0
            
    
def Tesseract(img):
    return image_to_string(img)

def preProcess(img_path='/home/neil/Desktop/a/grayimage.jpg',foldername="/home/neil/wordpress/output/"):
    img=imread(img_path,IMREAD_GRAYSCALE)
    img[img[:]<100]=asarray(0)
    img[img[:]!=0]=asarray(255)
    return img

def errorRecursion(fields_to_collect,img,fieldStore,img_path):
    print(img)
    vError=0
    while vError==0:
        vError=0
        for item in fields_to_collect:
                    try:
                        imageText=Tesseract(ROIselector(img,item))
                        print("Is the following correct:")
                        print(item+": "+imageText)
                        confirmation=input()
                        if confirmation=='y'or confirmation=='Y':
                            fieldStore[item]=imageText
                        else: 
                            if confirmation=='n' or confirmation=='N':
                                print('Enter correct value of field')
                                imageText=input()
                                fieldStore[item]=imageText
                            else:
                                raise ValueError
                    except AssertionError:
                        print('skipping {}...'.format(img_path))
                        skip.append(img_path)
                    except ValueError:
                        root=Tk()
                        root.withdraw()
                        messagebox.showwarning('Something other than y or n was input','Type only y or n in the input box')
                        print('Try again.')
                        vError=1

def skip_folder_gen(folder):
    try:
        chdir(folder)
        mkdir(folder+'skipped/')
        sleep(1)
        print('made directory')
    except FileExistsError:
        pass
    process=check_output(['mkdir','skipped'],shell=True)
    for file_path in skip:
        file_name=file_path.split('/')
        copy(file_name[-1],folder+'skipped/'+file_name[-1])


def MainProcess():
    V1error=0
    while V1error==1:
        try:
            print('Do you want to review the information collected after each file is finished?(y/n)')
            reviewAfterEveryFile=input()
            if reviewAfterEveryFile not in ['y','n']:
                raise ValueError
        except ValueError:
            root=Tk()
            root.withdraw()
            messagebox.showwarning('ValueError','Type only y or n as input box')
            print('Try again.')
            vError=1
    root = Tk()
    root.withdraw()
    root.filename =  filedialog.askdirectory(parent=root,initialdir="/home/neil/Desktop",title='Please select a directory')   
    foldername=str(root.filename)
    folder_all=listdir(foldername)
    imgs=[img for img in folder_all if img[-3:]=='jpg']
    img_paths=[join(root.filename,img) for img in imgs]
    for img_path in img_paths:
        img=preProcess(img_path)
        fieldStore={}
        errorRecursion(fields_to_collect,img,fieldStore,img_path)
        intermediate_field_store={img_path:fieldStore}
        if skipVariable==0:
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
        else:
            intermediate_field_store={}
            skipVariable=0 
    skip_folder_gen(foldername)       



n=""
while n!= "exit":
    print(">>>",end="")
    n=input()
    try:
        if n=='Folder()':
            MainProcess()
        else:
            if n=='help()':
                print(halp)
            else:
                if n=='exit':
                    pass
                else:
                    raise UnicodeError
    except UnicodeError:
        print('CommandNotFoundError: \'{}\' command not found'.format(n))
exit()
