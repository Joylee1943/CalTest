# coding=utf-8
from appium import webdriver


desired_caps = {}
#ios, android, firefoxOS
desired_caps['platformName'] = 'Android'
#OS版本--adb shell getprop ro.build.version.release
desired_caps['platformVersion'] = '4.4.2'
#机器名--adb devices
desired_caps['deviceName'] = '127.0.0.1:62001'
#aapt dump badging C:\Users\admin\Desktop\tmp\jisuanqi_583.apk
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
#fullReset,language,app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id('com.ibox.calculators:id/digit1').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("+")').click()
driver.find_element_by_name('2').click()
driver.find_element_by_id('com.ibox.calculators:id/equal').click()
result = driver.find_elements_by_class_name('android.widget.TextView')[1].text
print(result)

driver.quit()
