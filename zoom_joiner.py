from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import av
import pyvirtualcam
import pyautogui
import datetime
import time

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

ZOOM_LINK = "https://us05web.zoom.us/j/<your_link>" # the zoom link
VIDEOFILE = "C:\\Users\\steph\\Downloads\\clip.mp4" #path to video file
EMAIL = "blank" #your email here
PASSWORD = "blank" #your password here
MEETING_TIME = () #the time of the meeting in the format [year, month, day, hour, minute]

class SeleniumScripts:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        # Note - this function does not work with the current driver
        # Zoom, understandably, does not like scripts that facilitate automatic logins, and will block this login attempt
        # There are technically unofficial webdrivers that can get around this detection. 
        # I've tested them and they work, but it's a bit of a gray area, and I've chosen not to use them here.
        # Instead, you'll need to login manually and then run the script
        email_box = self.driver.find_element("id","email")
        password_box = self.driver.find_element("id","password")
        email_box.send_keys(email)
        password_box.send_keys(password)
        login_button = self.driver.find_element("id","js_btn_login")
        login_button.click()

    def open_zoom_from_link(self, zoom_link):
        # Goes to the specified Zoom link
        self.driver.get(zoom_link)
        # Goes left and hits enter to open up the Zoom app
        pyautogui.press('left')
        pyautogui.press('enter')

    def display_image(self):
        # Locates the join button and clicks it
        join_x, join_y = pyautogui.locateCenterOnScreen(os.path.join(__location__, 'join_button.png'))
        pyautogui.moveTo(join_x, join_y)
        pyautogui.click()

        pyautogui. keyDown("alt")
        # Presses the tab key once.
        pyautogui. press("v")
        # Lets go of the alt key.
        pyautogui. keyUp("alt")

class VirtualCamera:
    def __init__(self, path):
        self.container = av.open(path)
        height = self.container.streams[0].codec_context.coded_height
        width = self.container.streams[0].codec_context.coded_width

        self.cam = pyvirtualcam.Camera(width=width, height=height, fps=60)

    def display(self):
        while True:
            try:
                for frame in self.container.decode():
                    if type(frame) != av.video.frame.VideoFrame:
                        continue
                    self.cam.send(frame.to_ndarray(format="bgr24"))
                    self.cam.sleep_until_next_frame()
            except:
                continue

def main():
    # Sets up the webdriver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    # Schedules the meeting into the future
    scheduled_time = datetime.datetime(*MEETING_TIME)
    time.sleep(scheduled_time - (datetime.datetime.now()).total_seconds())

    # Runs the selenium and pyautogui scripts
    Script = SeleniumScripts(driver)

    # Opens up the zoom link
    Script.open_zoom_from_link(ZOOM_LINK)
    time.sleep(5)

    # Turns on the video
    Script.display_image()
    time.sleep(5)

    # Sets up the virtual camera and plays the video
    video = VirtualCamera(VIDEOFILE)
    video.display()

main()