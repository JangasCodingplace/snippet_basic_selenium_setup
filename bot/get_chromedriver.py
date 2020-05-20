import os
import requests
import shutil
import xml.etree.ElementTree as ET

from sys import platform
from getpass import getuser
from urllib.request import urlretrieve
from urllib.request import urlopen
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException

from .globals import (
    BASE_DIR,
    BOT_DIR,
    ASSETS_DIR,
    CHROMIUM_SYSTEM_STRINGS
)

"""
Helpful Links (2020-05-19)
https://docs.python.org/2/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
https://sdbrett.com/BrettsITBlog/2017/03/python-parsing-api-xml-response-data/
"""

class ChromeDriverDownload:
    # Keep that list up to date!
    min_version, max_version = [70,83]

    chrome_href = 'https://chromedriver.storage.googleapis.com/'
    namespace = 'http://doc.s3.amazonaws.com/2006-03-01'
    uri = '{%s}'%namespace

    def get_driver_version_pathes(system_specific=True):
        """
        Returns a list of Chromium Versions which you can add to
        Basic href for download.
        You can list OS Specific Chromiums (default) or unspecific.
        """
        response = requests.get(
            ChromeDriverDownload.chrome_href
        )
        root = ET.fromstring(
            response.content
        )
        
        chromiums = []
        for content in root.findall(f'{ChromeDriverDownload.uri}Contents'):
            key = content.find(f'{ChromeDriverDownload.uri}Key')
            version_list = [
                str(i) for i in range(
                    ChromeDriverDownload.min_version,
                    ChromeDriverDownload.max_version+1
                )
            ]
            if key.text.startswith(tuple(version_list)):
                chrome_system_string = ChromeDriverDownload.CHROMIUM_SYSTEM_STRINGS[platform]['zip_type']
                platform_driver = f'chromedriver_{chrome_system_string}.zip'
                if system_specific:
                    if key.text.endswith(platform_driver):
                        chromiums.append(key.text)
                else:
                    chromiums.append(key.text)
        
        return chromiums

    def download_and_unpack_chromedriver(download_url, dst=ASSETS_DIR):
        chrome_driver_dst = os.path.join(
            dst,
            ChromeDriverDownload.CHROMIUM_SYSTEM_STRINGS[platform]['driver']
        )
        zip_dst = os.path.join(
            dst,
            f'chromedriver.zip'
        )
        urlretrieve(
            download_url,
            zip_dst
        )


        """
        Please Note: The Chromefile (for MacOS) is a UNIX File.
        It's difficult to execute it by Python.
        Therefor I implemented a system intern shell command.

        Windows path is missing at the moment.
        Therefor a standard Python Service can be used.
        """
        if platform in ['darwin', 'linux', 'linux2']:
            while not os.path.exists(chrome_driver_dst):
                os.system(f'unzip {zip_dst}')
                wrong_chrome_path = os.path.join(
                    BASE_DIR,
                    'chromedriver'
                )
                os.replace(
                    wrong_chrome_path,
                    chrome_driver_dst
                )
            os.remove(zip_dst)
            sleep(2)
        
        else:
            print('WINDOWS WILL FOLLOW SOON')
            raise ValueError('Not Supported System')
        
        return chrome_driver_dst

    def driver_validation_test(driver_path):
        if not os.path.exists(driver_path):
            raise ValueError('Driver in Path does not exist.')
        try:
            driver = webdriver.Chrome(executable_path=driver_path)
            # driver.get('https://google.com')
            driver.quit()
            return True
        except SessionNotCreatedException:
            return False
        except Exception as e:
            print(e)
            raise ValueError('Ups. Something unexpected happened. Read Msg above.')

    def install_system_specific_driver(version = None, dst = ASSETS_DIR, clean_dst = True):
        if dst != ASSETS_DIR:
            if not os.path.exists(dst):
                raise ValueError('Target Dir does not exist.')
        if clean_dst:
            if platform == 'win32':
                if os.path.exists(os.path.join(dst, 'chromedriver.exe')):
                    os.remove(os.path.join(dst, 'chromedriver.exe'))
            else:
                if os.path.exists(os.path.join(dst, 'chromedriver')):
                    os.remove(os.path.join(dst, 'chromedriver'))

        if version is not None:
            download_url = f'{ChromeDriverDownload.chrome_href}{version}'
            driver_path = ChromeDriverDownload.download_and_unpack_chromedriver()
            if not ChromeDriverDownload.driver_validation_test(driver_path):
                raise ValueError('Invalid Driver Version.')
            return True
        
        versions = ChromeDriverDownload.get_driver_version_pathes()
        for version in reversed(versions):
            download_url = f'{ChromeDriverDownload.chrome_href}{version}'
            driver_path = ChromeDriverDownload.download_and_unpack_chromedriver(download_url)
            if ChromeDriverDownload.driver_validation_test(driver_path):
                return True
        
        raise ValueError('There is no valid Chromedriver for your current system. Please check if you installed Chrome.')

class ChromeUserDir:
    class MacOS:
        chrome_user_dir = os.path.join(
            '/'
            'Users',
            getuser(),
            'Library',
            'Application\ Support',
            'Google',
            'Chrome'
        )
    def copy_dir_to_dst(dst=ASSETS_DIR,clean_dst=True):
        if clean_dst:
            if os.path.exists(os.path.join(dst,'Chrome')):
                shutil.rmtree(os.path.join(dst,'Chrome'))
        if platform == 'darwin':
            chrome_dir = ChromeUserDir.MacOS.chrome_user_dir
        else:
            raise ValueError('Not Supported Platform for Chrome individualization.')
        # shutil.copytree(chrome_dir, os.path.join(dst,'Chrome'), symlinks=False, ignore=None)
        os.system(f'cp -a {chrome_dir} {dst}')
