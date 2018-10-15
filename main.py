# 程序的主体调用部分

from news_get import news_get
from input_text import input_text
from has_different_btw_two import has_diff

def main(url,fold_name,selectors):

    news_get(url,fold_name,selectors)

    diff_text = has_diff(fold_name)# 参数为fold_name 此参数的值非程序生成，需要同selectors一起给定
    
    #text = input_text()
    text = 'all'
    if text !='all':    # 判断输入是否为‘all’，若为all则输出网页所有的变化值························(此处可修改为需要的输入)
        out_put = []
        for item in diff_text:
            if text in item:
                out_put.append(item)

        count = 0   #统计是否有输出
        for item in out_put:
           print(item[0])
           print(item[1])
           count += 1
        if count==0:
            print("没有相关关键字")
    else:
        for item in diff_text:
            print(item)
        if len(diff_text)==0:
            print("没有更新消息")

main('http://www.zjgsu.edu.cn/news/','test',
'ul.pic_lists > li,dl:nth-of-type(3) > div > div.newsbottom > ul > li,#body_l > dl:nth-of-type(1) > ul:nth-of-type(2) > li,#body_l > dl:nth-of-type(2) > ul:nth-of-type(2) > li,#body_l > dl:nth-of-type(4) > ul:nth-of-type(2) > li'
    )



