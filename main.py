import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('https://www.calculator.net/')
time.sleep(10)


number1 = driver.find_element(By.XPATH, "//span[@onclick='r(4)']")
number2 = driver.find_element(By.XPATH, "//span[@onclick='r(8)']")
number3 = driver.find_element(By.XPATH, "//span[@onclick='r(3)']")
number4 = driver.find_element(By.XPATH, "//span[@onclick='r(7)']")
number5 = driver.find_element(By.XPATH, "//span[@onclick='r(6)']")
number6 = driver.find_element(By.XPATH, "//span[@onclick='r(2)']")
number7 = driver.find_element(By.XPATH, "//span[@onclick='r(0)']")
number8 = driver.find_element(By.XPATH, "//span[@onclick='r(1)']")
plus = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[1]/span[4]")
minus = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[2]/span[4]")
multiply = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[3]/span[4]")
division = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[4]/span[4]")
equal = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[5]/span[4]")
clear = driver.find_element(By.XPATH, "/html/body/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/div/div[5]/span[3]")

actions = ActionChains(driver)
actions.click(number1)
actions.click(plus).perform()
actions.click(number2)
actions.click(equal).perform()
actions.click(clear).perform()

actions.click(number3)
actions.click(multiply)
actions.click(number4)
actions.click(equal).perform()
actions.click(clear).perform()

actions.click(number5)
actions.click(division)
actions.click(number6)
actions.click(equal).perform()
actions.click(clear).perform()

actions.click(number7)
actions.click(minus)
actions.click(number8)
actions.click(equal).perform()
actions.click(clear).perform()
time.sleep(20)



