# 将文件按行读取

import sys

def read_line(filename):
    try:
        file_object = open(filename,'r')
        lines = file_object.read().splitlines() # 每读一行返回一个列表，每一行作为列表中一个元素
        file_object.close()
        return lines
    except Exception as e:
        print(e)
        sys.exit()