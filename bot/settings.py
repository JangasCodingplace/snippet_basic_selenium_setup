import os
from sys import platform
from urllib.request import urlretrieve
from urllib.request import urlopen
from time import sleep

import requests
import xml.etree.ElementTree as ET

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException

from .globals import (
    BASE_DIR,
    ASSETS_DIR,
    CHROMIUM_SYSTEM_STRINGS
)

from .get_chromedriver import (
    ChromeUserDir
)



def get_driver(
    driver_dir = ASSETS_DIR,
    window_size = None,
    headless = False,
    use_storage = False,
    update_storage = False,
):
    if not os.path.exists(driver_dir):
        os.mkdir(driver_dir)

    chrome_driver = os.path.join(
        driver_dir,
        CHROMIUM_SYSTEM_STRINGS[platform]['driver']
    )

    if not os.path.exists(chrome_driver):
        from .get_chromedriver import ChromeDriverDownload
        ChromeDriverDownload.install_system_specific_driver(dst=driver_dir)

    chrome_options = Options()
    if window_size is not None:
        if not isinstance(window_size, str):
            window_size = ','.join(window_size)
        chrome_options.add_argument(f"--window-size={window_size}")

    if headless:
        chrome_options.add_argument("--headless")
    
    if use_storage:
        chromeProfilePath = os.path.join(
            driver_dir,
            'Chrome'
        )
        if not os.path.exists(chromeProfilePath) or update_storage:
            ChromeUserDir.copy_dir_to_dst(driver_dir)
        chrome_options.add_argument(f"--user-data-dir={chromeProfilePath}")

    return webdriver.Chrome(
        options=chrome_options,
        executable_path=chrome_driver
    )

