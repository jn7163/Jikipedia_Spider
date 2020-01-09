# 利用selenium进行点击、输入等操作
# 使用selenium设置代理，使得mitmproxy可以获取到接口数据
from selenium import webdriver
from time import sleep
import random
import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=127.0.0.1:8080')

# 打开chrome浏览器（需提前安装好chromedriver）
browser = webdriver.Chrome(chrome_options=chrome_options)
print("正在打开网页...")
browser.get("https://jikipedia.com/")


while True:
    sleep(random.randint(6,12))
    # 查找加载更多标志
    try:
        info_more = browser.find_element_by_xpath('//*[@class="curvy cursor"]')  #使用绝对定位
        if info_more.text == "点击加载更多":
            info_more.click() #点击按钮
    except:
        print("页面未到达底部，继续向下滑动页面！")
        # 将滚动条移动到页面的底部
        try:
            js = "var q=document.documentElement.scrollTop=100000"
            browser.execute_script(js)
            sleep(random.randint(4,8))
        except:
            sleep(random.randint(4, 8))

sleep(1)
browser.close()  # 关闭当前页面
sleep(1)
browser.quit()  # 关闭整个浏览器
# 结束程序
sys.exit()


