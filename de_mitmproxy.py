import mitmproxy.http
import json
import time
import os

import re
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    # 去掉字符串中的 回车 和 空格
    new_title = "".join((re.sub("\n", " ", new_title)).split(" "))
    return new_title

class DouyinCrawl:
    def __init__(self):
        if not os.path.isdir("saveData"):
            # 如果目录不存在，则创建目录存储具体游记文章
            os.mkdir("saveData")

    # 拦截响应
    def response(self,  flow: mitmproxy.http.HTTPFlow):
        if 'api.jikipedia.com/go/browse_definitions' in flow.request.url:
            response = flow.response
            # 状态码为200，说明响应成功，获取到内容了
            if response.status_code == 200:
                data_json = response.text
                # # json.loads()函数是将json格式数据转换为字典
                data_obj = json.loads(data_json)
                if isinstance(data_obj, list):
                    for item in data_obj:
                        try:
                            title =str(item["id"]) + "_" + str(item["term"]["id"]) + "_" + item["term"]["title"]
                            title = validateTitle(title) #使得标题名符合文件命名要求
                            with open('./saveData/'+ title +'.json', 'w') as f:
                                # 1、python3里面默认编码是unicode
                                # 2、python3做dump与dumps操作时，会将中文转换成unicode编码，并以16进制方式存储，再做逆向操作时，会将unicode编码转换回中文
                                # 即添加参数 ensure_ascii=False，它默认的是Ture
                                json.dump(item, f,ensure_ascii=False)
                        except:
                            pass
addons = [
    DouyinCrawl()
]