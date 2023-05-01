from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S1074363437%3A1679937404868520&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&ifkv=AQMjQ7QoXTeZQ5aOQTAGB_M2em-vMxd1ymHa2phfEPxxJ1JZkd50MpS5Z0llPBCtbhMSUa4xXnnbvQ&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(10)

login = driver.find_element(By.ID, 'identifierId')
time.sleep(4)
login.send_keys("200103520@stu.sdu.edu.kz")
time.sleep(4)
next = driver.find_element(By.XPATH, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']").click()
time.sleep(4)
password = driver.find_element(By.NAME, 'Passwd')
time.sleep(4)
password.send_keys("Atyrau-atyra")
time.sleep(10)
next1 = driver.find_element(By.XPATH, "//*[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']").click()
time.sleep(10)
drag = driver.find_element(By.CSS_SELECTOR, "[data-id='1C6TtmV3cG8rtohY6-ZwyV1iYDUS6hiJU']")
time.sleep(4)
drop = driver.find_element(By.CSS_SELECTOR, "[data-id='1FJVoXm0CbrusGTc-iuHdMY7HTx9N3DRb']")
time.sleep(4)
mydrive = driver.find_element(By.XPATH, "//span[@jsname='KSzLFd']")
time.sleep(4)

actions = ActionChains(driver)
actions.drag_and_drop(drag, drop).perform()
time.sleep(20)
actions.double_click(drop).perform()
actions.drag_and_drop(drag, mydrive).perform()
time.sleep(20)


