import os
import pickle
from time import sleep
from bot import settings
from bot.get_chromedriver import ChromeUserDir
# d = ChromeDriverDownload.install_system_specific_driver()

driver = settings.get_driver(
    use_storage=True,
)

DIR = os.path.dirname(os.path.abspath(__file__))
driver.get("http://www.dropbox.com")
# sleep(45)
pickle_file = os.path.join(DIR,'cookies.pkl')
# pickle.dump( driver.get_cookies() , open(pickle_file,"wb"))
# driver.quit()


# cookies = pickle.load(open(pickle_file, "rb"))
# for cookie in cookies:
#     try:
#         print('YOPE')
#         driver.add_cookie(cookie)
#     except:
#         print('NOPE')
#         continue

# driver.get("http://www.dropbox.com")
