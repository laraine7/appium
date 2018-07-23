# encoding: utf-8
from appium import webdriver

desired_caps={

    'platformName': 'Android',
    # 'deviceName':'lae9a8b2',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '6.0.1',
    # apk包名
    'appPackage': 'com.mondial.fashiontech',
    # 'appPackage':'com.taobao.taobao',
    # apk的launcherActivity
    'appActivity': 'com.mondial.fashiontech.launcher.SplashActivity',
    'unicodeKeyboard':True,
    'reserKeyboard':True,
    'noReset': True,
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

size=driver.get_window_size()
print(size)
print(size['width'])