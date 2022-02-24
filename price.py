# # coding = utf-8
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import requests
# import sys
# import traceback
#
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument('--no-sandbox')
# browser = webdriver.Firefox(options=options)
# try:
#     browser.get("https://www.samsungeshop.com.cn/product/SM-G9910/SM-G9910ZVDCHC")
#     time.sleep(15)
#     text = browser.execute_script("return document.querySelector('.t2-now').textContent")
#     token = '6192272b6d474223b67d9cbb56b7ffb0'
#     content = "S21当前价格:" + text + "。"  # 改成你要的正文内容
#     url = 'http://pushplus.hxtrip.com/send?token=' + token + '&content=' + content
#     requests.get(url)
#     # 退出浏览器
#     browser.quit()
# except:
#     browser.quit()
#     print("报错信息")
#     print(sys.exc_info()[0], sys.exc_info()[1])
#     traceback.print_tb(sys.exc_info()[2])
#     token = '6192272b6d474223b67d9cbb56b7ffb0'
#     content = "查询价格失败"  # 改成你要的正文内容
#     url = 'http://pushplus.hxtrip.com/send?token=' + token + '&content=' + content
#     requests.get(url)
