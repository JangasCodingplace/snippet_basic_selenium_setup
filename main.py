from bot import settings
from bot.get_chromedriver import ChromeUserDir
# d = ChromeDriverDownload.install_system_specific_driver()

d = settings.get_driver(use_storage=True)