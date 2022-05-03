from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as e
from selenium.webdriver.chrome.options import Options
from log_config import logging
from PIL import Image, ImageOps
import requests
from mongo_collections import DatabaseAtlas
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER

def get_element(element):
    try:
        selected_element = driver.find_element(By.XPATH, element)
    except e.NoSuchElementException:
        raise ValueError("Expected XPATH input")
    return selected_element

def get_element_if_exists(element):
    try:
        selected_element = driver.find_element(By.XPATH, element)
    except e.NoSuchElementException:
        logging.warning("Element does not exist")
        return None
    return selected_element

#get the inner text property for the elements that are guaranteed to exist
def get_element_text(element):
    try:
        selected_element = driver.find_element(By.XPATH, element)
    except e.NoSuchElementException:
        raise ValueError("Expected XPATH input")
    return selected_element.get_attribute("innerText")

def get_text_if_exists(element):
    try:
        selected_element = driver.find_element(By.XPATH, element)
    except e.NoSuchElementException:
        logging.warning("Element does not exist")
        return None
    return selected_element.get_attribute("innerText")

def config_options(options):
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/dev/null")

def config_driver():
    chrome_options = Options()
    config_options(chrome_options)
    driver = webdriver.Chrome(DRIVER, options = chrome_options)

    return driver

DRIVER = "chromedriver_2.exe"

driver = config_driver()


