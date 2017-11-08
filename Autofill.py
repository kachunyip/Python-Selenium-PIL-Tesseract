# coding: utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image,ImageEnhance
import random,os,time,pytesseract

bs = webdriver.Firefox(executable_path="geckodriver")
bs.set_window_size(600,400)

def func():
    bs.get('https://www.wjx.cn/m/17854971.aspx/')
    bs.find_elements_by_class_name("ui-radio")[1].click()
    bs.find_elements_by_class_name("ui-checkbox")[0].click()
    bs.find_elements_by_class_name("ui-checkbox")[2].click()
    bs.find_elements_by_class_name("ui-radio")[4].click()
    bs.find_elements_by_class_name("ui-checkbox")[3].click()
    bs.find_elements_by_class_name("ui-checkbox")[9].click()
    bs.find_elements_by_class_name("ui-checkbox")[10].click()
    bs.find_elements_by_class_name("ui-checkbox")[12].click()
    bs.find_elements_by_class_name("ui-radio")[7].click()
    bs.find_elements_by_class_name("ui-checkbox")[random.randint(14, 17)].click()
    try:
        bs.find_element_by_id("yucinput").click()
        time.sleep(2)
        bs.get_screenshot_as_file('D://python_project//wholepage.png')
        im = Image.open("D://python_project//wholepage.png")
        box = (160, 180, 409, 308)
        region = im.crop(box)
        region.save("D://python_project//testwholepage.png")
        im = Image.open("D://python_project//testwholepage.png")
        im = im.convert("L")
        threshold = 55
        pixdata = im.load()
        w, h = im.size
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255

        for y in range(1, h - 1):
            for x in range(1, w - 1):
                count = 0
                if pixdata[x, y - 1] > 245:
                    count = count + 1
                if pixdata[x, y + 1] > 245:
                    count = count + 1
                if pixdata[x - 1, y] > 245:
                    count = count + 1
                if pixdata[x + 1, y] > 245:
                    count = count + 1
                if count > 2:
                    pixdata[x, y] = 255

        im.save("D://python_project//newMethod.png")
        img = Image.open("D://python_project//newMethod.png")
        code = pytesseract.image_to_string(img, "eng")
        newCode = ''
        for c in code:
            if(c.isalnum()):
                newCode += c
        print(newCode)
        bs.find_element_by_id("yucinput").send_keys(newCode)
    except Exception:
        print("Error")
    finally:
        bs.find_element_by_id("ctlNext").send_keys(Keys.ENTER)

def func2():
    bs.get('https://www.wjx.cn/m/17854971.aspx/')
    bs.find_elements_by_class_name("ui-radio")[random.randint(0, 1)].click()
    bs.find_elements_by_class_name("ui-checkbox")[random.randint(0, 2)].click()
    bs.find_elements_by_class_name("ui-radio")[random.randint(2, 4)].click()
    bs.find_elements_by_class_name("ui-checkbox")[random.randint(3, 6)].click()
    bs.find_elements_by_class_name("ui-checkbox")[random.randint(7, 10)].click()
    bs.find_elements_by_class_name("ui-checkbox")[random.randint(11, 13)].click()
    bs.find_elements_by_class_name("ui-radio")[random.randint(5, 7)].click()
    bs.find_elements_by_class_name("ui-checkbox")[random.randint(14, 17)].click()
    bs.find_element_by_id("ctlNext").send_keys(Keys.ENTER)

''' def check(css):

    s = bs.find_elements_by_css_selector(css_selector=css).
    if(len(s) == 0):
        func2()
    elif len(s) == 1:
        func() '''

while True:
    try:
        '''check("#yucinput")'''
        func()
    except Exception:
        t = bs.switch_to_alert()
        print(t.text)
        t.accept()
    time.sleep(2)