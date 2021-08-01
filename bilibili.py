# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib import request
from bs4 import BeautifulSoup
import time
import requests
import re
import json

DEBUG=1                     #1 if want all comments;0 if only with keywords
FILE=1                      #1 if want results recorded in file;0 if on terminal
def content_bilibili():
    url_video="https://www.bilibili.com/video/BV1fx411F7G8?from=search&seid=15924329464979522645"
    url_comment='https://comment.bilibili.com/662885.xml'
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",

        "Cookie": "_uuid=003E182E-4E74-0385-EEA5-7F8491BEBF3C55784infoc; buvid3=92AE183D-C4F7-455A-AF17-F418C5F1A415148806infoc; CURRENT_FNVAL=80; bsource=search_baidu; blackside_state=1; rpdid=|(J|)J|kRk~m0J'uYk~~)mY~~; fingerprint=9c58be88976ba81ef8416db6e94889ba; buvid_fp=92AE183D-C4F7-455A-AF17-F418C5F1A415148806infoc; buvid_fp_plain=92AE183D-C4F7-455A-AF17-F418C5F1A415148806infoc; SESSDATA=c4a71948%2C1643341727%2C9842a%2A81; bili_jct=8dd7efb0d486086b1fd49620c1436f38; DedeUserID=514303642; DedeUserID__ckMd5=6a43674866dc6b2a; sid=6k7ov69x; PVID=1; bfe_id=1e33d9ad1cb29251013800c68af42315"
    }
    # req = request.Request(url_comment, headers=headers)
    # response = request.urlopen(req).read().decode()
    # req = requests.get(url_comment, headers=headers)
    # request.encoding = 'utf8'
    req = requests.get(url_comment)  # 获取页面
    req.encoding = 'utf8'  # 因为是中文，我们需要进行转码，否则出来的都是unicode
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.find_all('d')
    analyze_comment(results)


comment_num=0
record_needed=[]
def analyze_comment(res):
    global comment_num
    p_find = ['工作室','作者','studio']
    fo = open("弹幕.txt", "a+")
    if FILE:
        comment_num = 0
        fo.write("\n\n——————新尝试——————\n")
    for item in res:
        comment_num+=1
        item=str(item)
        for key_word in p_find:
            if re.search(key_word, item) is not None or DEBUG:
                # item = item.replace("<br/>", '\n')
                # item = item.replace('。', '。\n')
                item = re.sub("<.*?>", '', item)
                if not FILE:
                    print(str(comment_num)+':'+item)
                else:
                    fo.write(str(comment_num)+':'+item+'\n')
                break

if __name__ == '__main__':
    for i in range(5):
        content_bilibili()
        time.sleep(10)



