import requests # 导入requests包
from bs4 import BeautifulSoup
import json
import os
def translate(word):
    r = requests.get('http://www.youdao.com/w/eng/'+word) # 向有道词典请求资源
    html = r.text
    soup = BeautifulSoup(html, 'html.parser') # 结构化文本soup
    div = soup.find(name='div', attrs={'class': 'trans-container'}) # 获取中文释义所在的标签
    return div.get_text() # 获取标签内文本

def Translate(filename, sp):
    wordlist = filename.split('.')[0]
    filepath = os.path.join(sp._dirSpeech, wordlist + ".json")
    if not os.path.exists(filepath):
        CNTable = []
        fr = open(filename)
        for i in fr.readlines():
            CNTable.append(translate(i))
        fr.close()
        with open(filepath, "w") as f:
            json.dump(CNTable, f)  # 写入json
    with open(filepath) as f:
        NewTable = json.load(f)#从json中读取
    return NewTable