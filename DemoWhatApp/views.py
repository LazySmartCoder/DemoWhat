from django.shortcuts import render, redirect
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import shutil

# Create your views here.
def index(request):
    return render(request, "index.html")

def subnum(request):
    number = request.POST["num"]
    id = request.POST["id"]

    temp_user_data_dir = f"C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\{id}"

    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={temp_user_data_dir}')

    wd = webdriver.Chrome(options=options)
    wd.get("https://web.whatsapp.com")
    time.sleep(90)
    wd.execute_script('document.getElementsByClassName("_3iLTh")[0].click();')
    time.sleep(20)
    wd.execute_script('document.getElementsByClassName("selectable-text g0rxnol2 k2bacm8l g2bpp9au ln8gz9je cc8mgx9x eta5aym1 d9802myq e4xiuwjv thr4l2wc cixrojiy enbbiyaj g33ro0j9 i5tg98hk f9ovudaz przvwfww gx1rr48f")[0].setAttribute("id", "inp");')
    time.sleep(2)
    input_1=wd.find_element(by=By.ID, value= 'inp')
    time.sleep(2)
    input_1.send_keys(number)
    input_1.send_keys(Keys.ENTER)
    time.sleep(8)
    otp = wd.execute_script("""let textContent = document.querySelector('div').innerText;
                      return textContent""")
    print(otp)
    time.sleep(120)
    wd.close()
    wd.quit()
    return render(request, "index.html", {"dat" : "Thank you for requesting"})

def viewprof(request):
    id = request.POST["id"]
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir=C:\\Users\\A\\AppData\\Local\\Google\\Chrome\\User Data\\{id}")
    wd = webdriver.Chrome(options=options)
    wd.get("https://web.whatsapp.com")
    time.sleep(60)
    return redirect("HomePage")

