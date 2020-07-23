import requests
from bs4 import BeautifulSoup as bs
import time
import random
from tkinter import *
from tkinter import messagebox

window = Tk()

def Click():
    messagebox.showinfo("알림창", "노트북실 자리났다!!!")

MAX_SLEEP_TIME = 3

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

while 1:
    rand_value = random.randint(1, MAX_SLEEP_TIME)
    time.sleep(rand_value)

    URL = 'http://wisem.uos.ac.kr/SEAT/domian5.asp'

    session = requests.Session()
    html = session.get(URL, headers = headers).text
    bsObj = bs(html, 'html.parser')
    laptop = bsObj.select('body > center > form > table:nth-child(3) >tr:nth-child(7) > td:nth-child(6) > font')
    percentage = laptop[0].text[1:4]
    print('만석...')
    if int(percentage) < 100:
        Click()
        window.mainloop()
        break


