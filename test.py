# 用来测试添加的选择器是否正确

from bs4 import BeautifulSoup
import re
from url_get import get_html

#添加需要测试网站的url

html = get_html('http://www.zjgsu.edu.cn/news/') #获取html
soup = BeautifulSoup(html,'html.parser')  #定义一个Soup对象

#添加需要测试的选择器：
selector = 'ul.pic_lists > li,dl:nth-of-type(3) > div > div.newsbottom > ul > li,#body_l > dl:nth-of-type(1) > ul:nth-of-type(2) > li,#body_l > dl:nth-of-type(2) > ul:nth-of-type(2) > li,#body_l > dl:nth-of-type(4) > ul:nth-of-type(2) > li'
selector = selector.split(',')
data = [] 

for i in selector:
    try:
        newses = soup.select(i) # 一定注意selector的正确性
                
        for news in newses:

            href = re.compile(r'href="[0-9a-zA-Z/.]{1,}"') # 匹配 href="..."
            re_link = re.compile(r'[0-9a-zA-Z/.]{1,}') # 匹配href="..."中的...

            str_news = str(news) # findall方法参数需要str类型

            i = href.findall(str_news)[0] #匹配正常情况下，得到一个只含一个元素的列表，取出这个元素href="..."
            link = re_link.findall(i)[1] #取出href="..."中的...

            title = news.get_text().strip()    #去掉首位空格

            info = title+'  '+link
        
            data.append(info)
    except Exception as e:
        print(e)

print(data)


