"""di={1:2,2:3}
with open('fileStore.py','w') as f:
    f.write("fileStore={}".format(str(di)))
    f.close()"""

import pyautogui as p
import time
#p.FAILSAFE=False
#p.click(583,101)
#p.hotkey('ctrlleft','a')
#browser=webdriver.chromedriver()
Surname=(488,578)#browser.find_element_by_name('applicant_surname')
Given_name=(496,600)#browser.find_element_by_name('applicant_givenname')
Sex_select=(517,618)#from selenium.webdriver.support.ui import Select# Select(driver.find_element_by_name('applicant_sex')).select_by_visible_text('Male/Female/Transgender')
Sex_male=(504,647)
Sex_female=(504,662)
Sex_transgender=(504,676)
DOB=(515,676)
Age=(492,734)
Real_dob=(767,733)
Scroll='p.scroll(-11)'
Specialcategory_select=(507,183)
Specialcategories={}
#p.typewrite('hello')
#p.moveTo(932,124)
time.sleep(3)
p.scroll(-15)
#p.displayMousePosition()
#print(p.position())
#p.moveTo(Surname)














'''for n in range(10):
    p.click(683,100+n*20)
    p.typewrite("it worked!!")
    p.typewrite('\n')
    #p.hotkey('ctrlleft','v')
p.moveTo(0,0,3)
p.moveTo(500,500)'''
"""
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import pyautogui as p
#driver=webdriver.Chrome(executable_path='/home/neil/Desktop/chromedriver')
#driver.get('http:/python.org')
#assert 'Login Page' in driver.title
print(driver.title)

#p.typewrite('windows\n')
#driver.close()
#""""""
from pytesseract import image_to_string
print(image_to_string('/home/neil/wordpress/output/output.jpg'))
    #for i in range(3):
    #    arr[arr[:,:,i]<100]=asarray(0)
    #    arr[arr[:,:,i]!=0]=asarray(255)
    #print(arr)
    
    #scipy.misc.imsave(arr,str(foldername)+"output.jpg")
   
    #img=imread(str(foldername)+"output.jpg")
    #return img"""