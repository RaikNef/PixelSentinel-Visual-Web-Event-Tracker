from datetime import datetime
from PIL import Image
from io import BytesIO
from IPython.display import display
import time
import csv

def write_to_csv(timestamp, multiplier, participants, bet_sum):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, multiplier, participants, bet_sum])
        print(1)
def cheker():
    timestamp = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
    element = driver.find_element(By.CLASS_NAME, 'crash-round')
    elements = element.find_elements(By.TAG_NAME, 'span')[0]
    print(elements.text)
    crash = elements.text.replace("X", "")
    crash = crash.replace(".", ",")
    
    element = driver.find_element(By.CLASS_NAME, 'bets')
    elements = element.find_elements(By.TAG_NAME, 'span')[0]
    bet = elements.text.replace("\nUSD", "")
    print(bet)

    element = driver.find_element(By.CLASS_NAME, 'users')
    elements = element.find_elements(By.TAG_NAME, 'span')[0]
    print(elements.text)
    users = elements.text
    write_to_csv(timestamp, crash, users, bet)
    return
def check_color_in_area(image):
    for i in range(-3, 4):
        for j in range(-3, 4):
            for k in range(-3, 4):
                for x in range(120, 128):
                    for y in range(245, 254):
                        if image.getpixel((x, y)) == (172 + i, 47 + j, 71 + k):
                            return True
    return False
def check_color_at_points(image_data):
    image = Image.open(BytesIO(image_data))
    if check_color_in_area(image):
        cheker()
        print(f"Цвет найден в области")
        return True
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")
time.sleep(5)
driver.set_window_size(300, 600)

screenshot = driver.get_screenshot_as_png()
image = Image.open(BytesIO(screenshot))
display(image)

# element = driver.find_element(By.CLASS_NAME, 'modal-content')
# element.find_elements(By.TAG_NAME, "button")[0].click()
while(1):
    screenshot = driver.get_screenshot_as_png()
    if check_color_at_points(screenshot):
        time.sleep(4)
    time.sleep(1)