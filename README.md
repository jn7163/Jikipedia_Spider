# Jikipedia_Spider
python selenium+mitmproxy实现 小鸡词典爬虫

## 环境：
win10 chrome python3 selenium mitmproxy
注意：这里安装selenium时要下载正确的对应的ChromeDriver版本

## 运行
1.先执行命令：`mitmdump -s de_mitmproxy.py` ，启动中间人代理，可以实现对http(s)的拦截
2.执行命令：`python de_selenium.py` ,调用selenium来模拟正常用户访问浏览器

## 效果：

