py_note.py


#help
python -h
#show version
python -V 


#print a string
print("string");
print( y, end=" " ) # not adding to next line


#show a text and get input
input("prompt text")

# show all keywords
import keyword
keyword.kwlist
https://github.com/zha34/py_game

#coment 
# single line
''' multi lines '''
""" multi lines """


#indentation
indent sensitive
but no {}



#split a line into multi

total = item_one + \
        item_two + \
        item_three

#exception
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']



#type
int 
bool
float
complex



#String
cannot be changed

"this is a line with \n"  #will show \n
-从左往右以 0 开始，从右往左以 -1 开始
-用 + 运算符连接在一起，用 * 运算符重复



#using ; to put multi lines into one
import sys; x = 'runoob'; sys.stdout.write(x + '\n')




#import

from sys import argv,path  #  导入特定的成员
 

import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

equivalent

print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


http://kbroman.org/github_tutorial/pages/init.html

https://unity3d.com/cn/learn/tutorials/topics/graphics/gentle-introduction-shaders