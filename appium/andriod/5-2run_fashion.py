# encoding: utf-8
from appium import webdriver
import time
import random
from fash_tech_end.lee_selenium import Lee

desired_caps={
                'platformName':'Android',
                # 'deviceName':'lae9a8b2',
                'deviceName':'127.0.0.1:62001',
                'platformVersion':'4.4.2',
                 #apk包名
                'appPackage':'com.mondial.fashiontech',
                # 'appPackage':'com.taobao.taobao',
                #apk的launcherActivity
                'appActivity':'com.mondial.fashiontech.launcher.SplashActivity',
                # 'appActivity':'com.taobao.tao.ContainerActivity'
                'unicodeKeyboard':True,#unicodeKeyboard是使用unicode编码方式发送字符串
                'reserKeyboard':True,#resetKeyboard是将键盘隐藏起来(加上这两个可以输入中文)
                'automationName': 'Uiautomator2',#appium1.4支持最高android版本是6.0，有些小伙伴可能用的appium1.6版本，可以尝试加上这个参数，用uiautomator2运行
                'noReset': True,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#休眠5秒等待页面加载完成
driver_n=Lee(driver)
time.sleep(5)
# driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
# time.sleep(2)
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"hao")
driver.find_element_by_id("com.mondial.fashiontech:id/main_user_center").click()
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/me_my_address").click()
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/address_btn_add").click()
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/address_et_receiver").send_keys("小雨")
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/widget_country_code_et").send_keys("13006626613")
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/address_tv_area_address").click()
time.sleep(1)
elements=driver.find_elements_by_class_name("android.widget.RelativeLayout")

sj=random.randint(0,len(elements)-1)
elements[sj].click()
time.sleep(1)
elements[sj].click()
time.sleep(1)
elements[sj].click()
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/address_et_detail_address").send_keys("天安创新科技广场自动2期")
address=driver.find_element_by_id("com.mondial.fashiontech:id/address_et_detail_address").text
print(address)
driver.find_element_by_id("com.mondial.fashiontech:id/address_btn_confirm").click()

add_address=("id","com.mondial.fashiontech:id/address_btn_add")
driver_n.click(add_address)
#地址内容
time.sleep(1)
driver.find_element_by_id("com.mondial.fashiontech:id/address_et_receiver").send_keys(u"laraine")
time.sleep(1)
# add_name=("id","com.mondial.fashiontech:id/address_et_receiver")
# driver_n.send_keys(add_name,u"小草")
add_tel=("id","com.mondial.fashiontech:id/widget_country_code_et")
driver_n.send_keys(add_tel,"13006626613")
area_address=("id","com.mondial.fashiontech:id/address_tv_area_address")
driver_n.click(area_address)
add_elemets=driver.find_elements_by_id("com.mondial.fashiontech:id/dialog_address_tv_province")
add_elemets_sele=self.is_element_exist("com.mondial.fashiontech:id/dialog_address_tv_province")
time.sleep(2)
for add in range(3):
    if add_elemets_sele:
        add_sj = random.randint(0, len(add_elemets) - 1)
        add_elemets[add_sj].click()


add_det=("id","com.mondial.fashiontech:id/address_et_detail_address")
driver_n.send_keys(add_det,"china,zhongguo,tianan chuangxing keji")

add_con=("id","com.mondial.fashiontech:id/address_btn_confirm")
driver_n.click(add_con)



time.sleep(3)
driver.quit()