# 用来测试添加的选择器是否正确

from bs4 import BeautifulSoup
import re
import url_get_utf8
import url_get_gbk
import url_get_gb2312

#添加需要测试网站的url
url = 'http://news.163.com/rank/'
#获取html # 一定要注意不同网页的解码方式应不同
try:
    html = url_get_utf8.get_html(url) #获取html
except:
    try:
        html = url_get_gbk.get_html(url)
    except:
        try:
            html = url_get_gb2312.get_html(url)
        except Exception as e:
            print(e)
#print(html)
soup = BeautifulSoup(html,'html.parser')  #定义一个Soup对象

#添加需要测试的选择器：
# https://news.sina.com.cn/ ---- #syncad_1 > h1,p:nth-of-type(4) > a,#ad_entry_b2 > ul > li.topli14,#ad_entry_b2 > ul > li
# http://news.163.com/rank/ ---- tr > td.red,
selectors = 'td'
selectors = selectors.split(',')
#print(selector)
data = [] 

for i in selectors:
    try:
        packages = soup.select(i) # 一定注意selector的正确性
        
        for package in packages:
            #print(package)
            #print('----------------------------')

            nodes_a = re.compile(r'<a .*?>.*?</a>') #匹配一对<a>标签

            href = re.compile(r'href="[a-zA-z]+://[^\s]*"') # 匹配 href="..."
            
            re_link = re.compile(r'[0-9a-zA-Z/.:_-]{1,}') # 匹配href="..."中的...

            re_title = re.compile(r'>.+<') # 匹配标题

            str_package = str(package) # findall方法参数需要str类型
            
            a = nodes_a.findall(str_package)
            #print(a)
            for item in a:

                #print(item)
                x  = href.findall(item)
                #print(x)
                link = str(re_link.findall(str(x))[1]) #取出href="..."中的...
                
                # 匹配中文
                title = str(re_title.findall(str(item)))
                #print(title)
                #print(link)
                
                info = title[3:-3]+' '+link
                data.append(info)
            #print('---------------------------------------------------------')
            
    except Exception as e:
        print(e)
#print('---------------------------')
for i in data:
    print(i)
#print(data)

#解决一个<li>标签中含有两个或多个<a>标签的情形
#创建多个模块，支持不同编码的网页的不同解码方式，或一个模块能够智能区分需要的解码方式
#测试代码对不同网站的支持情况，提高代码的复用性，将代码更加模块化

#解决网页中存在滚动条的情况
