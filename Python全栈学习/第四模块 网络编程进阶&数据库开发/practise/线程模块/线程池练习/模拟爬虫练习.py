#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/28 9:49

import time
import requests
from concurrent.futures import ThreadPoolExecutor
def get_content(url):
    print("Download %s...." % url)
    # time.sleep(4)
    return {"url": url, "content": requests.get(url).text }

def parse(res):
    print(res) # res 是get_content函数的一个执行结果对象
    res = res.result()
    print("%s length: %s" %(res['url'], len(res['content'])))

if __name__ == "__main__":
    pool = ThreadPoolExecutor(3)
    urls = [
        "http://www.baidu.com",
        "http://jd.com",
        "http://news.163.com",
        "https://www.luffycity.com",
        "https://www.cnblogs.com/kerwinC/p/6835208.html"
    ]
    for url in urls:
        pool.submit(get_content, url).add_done_callback(parse) # 回调函数，将get_content的返回值作为要给对象传递给回调函数parse
