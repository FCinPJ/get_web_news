from bs4 import BeautifulSoup
import re
from url_get import get_html
from old_or_new import clarify_old_or_new

#url = 'http://www.zjgsu.edu.cn/news/' #浙江工商大学新闻网

def news_get(url,fold_name,selectors): #参数url：要爬取的网站，fold_name：创建存放txt文件的文件夹名，selectors传入任意个数selector
    
    html = get_html(url) #获取html
    soup = BeautifulSoup(html,'html.parser')  #定义一个Soup对象

    data = [] 
    selectors=selectors.split(',')
    for selector in selectors:

        try:
            newses = soup.select(selector) # 一定注意selector的正确性
            
            for news in newses:

                href = re.compile(r'href="[0-9a-zA-Z/.]{1,}"') # 匹配 href="..."
                re_link = re.compile(r'[0-9a-zA-Z/.]{1,}') # 匹配href="..."中的...

                str_news = str(news) # findall方法参数需要str类型

                i = href.findall(str_news)[0] #匹配正常情况下，得到一个只含一个元素的列表，取出这个元素href="..."
                link = re_link.findall(i)[1] #取出href="..."中的...

                title = news.get_text().strip()    #去掉首位空格

                info = title+'  '+link
                #info = {
                #    'news':title,
                #    'link':link
                #}

                data.append(info)
        except Exception as e:
            print(e)
    #print(data) # 查看爬取信息是否正确
    clarify_old_or_new(data,fold_name)
# 方法调用示例
#news_get('http://www.zjgsu.edu.cn/news/',
#    'test',
#    'ul.pic_lists > li',
#    '#topic > dl:nth-of-type(3) > div > div.newsbottom > ul > li',
#    '#body_l > dl:nth-of-type(1) > ul:nth-of-type(2) > li')


