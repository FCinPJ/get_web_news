# 程序的主体调用部分

from news_get import news_get
from input_text import input_text
from has_different_btw_two import has_diff
import datetime

def main(url,fold_name,selectors):

    news_get(url,fold_name,selectors)

    diff_text = has_diff(fold_name)# 参数为fold_name 此参数的值非程序生成，需要同selectors一起给定

    file_name = fold_name+'/out.txt' #测试用，向每文件写入这段时间网站的更新消息

    time1 = datetime.datetime.now() # 得到当前时间
    time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
    #text = input_text()
    text = '李咏'
    if text !='all':    # 判断输入是否为‘all’，若为all则输出网页所有的变化值························(此处可修改为需要的输入)
        out_put = []
        for item in diff_text:
            if text in item:
                out_put.append(item)
        count = 0   #统计是否有输出
        for item in out_put:
            print(item)
            
            try:
                with open(file_name,'a+') as file_object:
                    file_object.write(time1_str+'\n')
                    file_object.write(str(item)+'\n')
                    
            except Exception as e:
                print(e)       
                 
            count += 1 
        if count==0:
            print("没有相关关键字")

            try:
                with open(file_name,'a+') as file_object:
                    file_object.write(time1_str+'\n')
                    file_object.write("没有相关关键字"+'\n')
            except Exception as e:
                print(e)
    else:
        for item in diff_text:
            print(item)

            try:
                with open(file_name,'a+') as file_object:
                    file_object.write(time1_str+'\n')
                    file_object.write(item+'\n')
                    
            except Exception as e:
                print(e)
                
        if len(diff_text)==0:
            print("没有更新消息")

            try:
                with open(file_name,'a+') as file_object:
                    file_object.write(time1_str+'\n')
                    file_object.write("没有相关关键字"+'\n')
            except Exception as e:
                print(e)



main('https://news.sina.com.cn/','sina-news',
'#syncad_1 > h1,p:nth-of-type(4) > a,#ad_entry_b2 > ul > li.topli14,#ad_entry_b2 > ul > li'
)

main('http://news.163.com/rank/','163-news','td')

