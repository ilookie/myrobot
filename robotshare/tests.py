# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
#chrome_options.add_argument("--headless")
# 更换头部
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMess/6.5.2.501"')

base_url = "https://activity.waimai.meituan.com/coupon/sharechannel/B2EA8E1ABA8B47EA82DB475BA17B517D?urlKey=FC88ED80E61346B18A31B431789511E3&utm_term=AiphoneBgroupC9.4.0DweixinEwm-orderG5BF83A4416F9B7E97A3928BF8124D8969059BD39DF8BBC4024B5E07C5F40574A20180622193942063&utm_source=appshare&utm_medium=iOSweb&utm_fromapp=wx&utm_sharesource=wm-order"

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(base_url+"/")
start_time=time.time()
print('this is start_time',start_time)

# driver.find_element_by_id("u").send_keys("1258309730")
# driver.find_element_by_id("p").send_keys("wj199104")
# driver.find_element_by_id("go").click()
# time.sleep(3)
# driver.save_screenshot('%s_screen.png'%str(time.time()))
# for item in driver.find_elements_by_xpath("//li[@class='records-1roLU']"):
#     print item.find_element_by_class_name("records-2JDGW").text
    
    
#driver.close()

end_time=time.time()

print('this is end_time',end_time)





