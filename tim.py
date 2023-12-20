#!/usr/bin/env python

import os
import sys
import time

# 默认存放路径
file_path = os.environ["HOME"] + "/.tim/"
if not os.path.exists(file_path):
    os.mkdir(file_path)

# 按`2024-01-01.md`的形式保存当天的全部记录
# 每条记录以`◉ 09:30:00: `的形式开头
cdate = time.strftime("%Y-%m-%d")
ctime = time.strftime("%H:%M:%S")
today_path = file_path + cdate + ".md"

# 如果`tim`命令带上了参数，如果是 `-l` 或者 `--list`, 则列出文本列表
# 否则假定参数是`2023-12-31`这种形式的日期
# 存在就阅读指定日期的记录文本，不存在就是瞎写的参数，阅读当天的记录文本好了
# 不带参数则进行当天的记录
if len(sys.argv) > 1:
    if sys.argv[1] in ("-l", "--list"):
        os.system("ls -1 " + file_path)
        sys.exit()
    input_path = file_path + sys.argv[1] + ".md"
    if os.path.exists(input_path):
        os.system("vim " + input_path)
    else:
        os.system("vim " + today_path)
else:
    with open(today_path, "a+", encoding="utf-8") as f:
        f.write("\n◉ " + ctime +": ")
    os.system("vim + " + today_path)
