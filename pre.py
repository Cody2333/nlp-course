#coding:utf-8
# 。分行
# 。“ 不换行
import re
#设置分句的标志符号
cutlist="。！？".decode('utf-8')

# 检查某字符是否分句标志符号的函数；如果是，返回True， 否则返回False
def FindTok(char):
    global cutlist
    if char in cutlist:
        return True
    else:
        return False

result = open('version2_formatted.txt', 'w')
with open ('version2.1.txt', 'r') as f:
  print f
  for line in f:
    l = line.strip('\r\n')
    print l
    if FindTok(l[len(l)-1]):
      print 'xx'
      result.write(l + '\n')
    else:
      result.write(l)
  result.close()
