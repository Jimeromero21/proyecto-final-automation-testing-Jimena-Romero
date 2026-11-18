import sys
from pathlib import Path

from selenium import webdriver

# Permite importar Page/ y config.py desde features/
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import BASE_URL


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(BASE_URL)


def after_scenario(context, scenario):
    context.driver.quit()