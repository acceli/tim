# tim
在linux使用vim进行实时的纯文本记录

#### 前言

假定linux已经安装了python(一般都已经默认安装)

#### 部署方法

1. 重命名 `tim.py` 为 `tim`
2. 赋予可执行权限 `chmod +x tim`
3. 移动到bin目录 `sudo mv /usr/local/bin/`
4. 输入 `tim` 进行愉快的记录！

#### 功能介绍

``` bash
tim -l #列出按天聚合的文本清单

tim 2023-12-31 #查看指定日期的文本

tim 随便乱敲 #查看当天的文本

tim #记录模式
```
