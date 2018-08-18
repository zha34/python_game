py_note.py


#help=====================================================

python -h
#show version
python -V 


#print a string
print("string");
print( y, end=" " ) # not adding to next line

%c  格式化字符及其ASCII码
%s  格式化字符串	
%d  格式化整数
%u  格式化无符号整型
%o  格式化无符号八进制数
%x  格式化无符号十六进制数
%X  格式化无符号十六进制数（大写）
%f  格式化浮点数字，可指定小数点后的精度
%e  用科学计数法格式化浮点数
%E  作用同%e，用科学计数法格式化浮点数
%g  %f和%e的简写
%G  %f 和 %E 的简写
%p  用十六进制数格式化变量的地址


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


# assign value
a = b = c = 1
a, b, c = 1, 2, "runoob"

#delete variable
del var



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


# relation

# compare value
a == b

# compare reference (obj)
a is b

#type=====================================================

print(type(a)) #type the type of a 

Number
	int 
	float
	bool
	complex


>>>5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32




String
#cannot be changed

"this is a line with \n"  #will show \n
-从左往右以 0 开始，从右往左以 -1 开始
-用 + 运算符连接在一起，用 * 运算符重复





Tuple
# very similar to List and String
# can not modify value, except class object


tup = ()
tup = (1,) #for 1 elem only

#using ()
>>>tup = (1, 2, 3, 4, 5, 6)
>>> print(tup[0])
1
>>> print(tup[1:5])
(2, 3, 4, 5)
>>> tup[0] = 11  # 修改元组元素的操作是非法的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment





List
#using []
>>>a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为 [] 
>>> a
[9, 2, 6]

del list[2]



Set 
# unorder set of elems
# used for remove duplicate elems
# used for test existence
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')


# empty set
a = set()
# used for set calculation

a = set('abracadabra')
b = set('alacazam')
 
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素


# using {}


Dictionary

# key is unique 
# key can not be chnaged
# key: value 1 to 1

dict = {}

dict['one'] = "1 - 菜鸟教程"
print (dict['one'])       # 输出键为 'one' 的值
>> 1 - 菜鸟教程

dict[2]     = "2 - 菜鸟工具"
print (dict[2])           # 输出键为 2 的值
>> 2 - 菜鸟工具

 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
 
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

>> {'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
>> dict_keys(['name', 'site', 'code'])
>> dict_values(['runoob', 'www.runoob.com', 1])


>>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
 
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
 
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Taobao': 3, 'Runoob': 1, 'Google': 2}

clear()
keys()
values()


#using ; to put multi lines into one
import sys; x = 'runoob'; sys.stdout.write(x + '\n')




#import=====================================================


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








https://unity3d.com/cn/learn/tutorials/topics/graphics/gentle-introduction-shaders