Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: C:/Users/JOHN/Desktop/DSP/practical/demopy.py ============
tup=(2,4,3,2,5,6,3)
tup.count(2)
2
sorted(tup)
[2, 2, 3, 3, 4, 5, 6]
str=("hello world! this is john")
str
'hello world! this is john'
str.upper()
'HELLO WORLD! THIS IS JOHN'
str.title()
'Hello World! This Is John'
str.capitalize()
'Hello world! this is john'
str=("python is a programming language and it is in trending")
str
'python is a programming language and it is in trending'
str.count("is")
2
str.swapcase()
'PYTHON IS A PROGRAMMING LANGUAGE AND IT IS IN TRENDING'
str.partition('is')
('python ', 'is', ' a programming language and it is in trending')
str.startwith('python')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str.startwith('python')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
str.startswith('python')
True
str.endswith(1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str.endswith(1)
TypeError: endswith first arg must be str or a tuple of str, not int
str.endswith('python')
False
set={"a","b","c"}
set
{'a', 'b', 'c'}
set.add('d')
set
{'a', 'b', 'd', 'c'}
str.reverse()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    str.reverse()
AttributeError: 'str' object has no attribute 'reverse'
l.reverse()
l
[5, 4, 2, 1]
l=[1,2,3,4]
l2=['john']
l.extend(l2)
l
[1, 2, 3, 4, 'john']
del l[2]
l
[1, 2, 4, 'john']
#update() updates the dict with the elements from another dict obj
dic1={'a':23,'n':44}
dict2={'c':56}
dict3={'b':56}
dict1.update(dict3)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict1.update(dict3)
NameError: name 'dict1' is not defined. Did you mean: 'dic1'?
d1={'a':'john','b':'ias'}
d2={'b':'paul'}
d1.update(d2)
d1
{'a': 'john', 'b': 'paul'}
j=d1.copy()
j
{'a': 'john', 'b': 'paul'}
j.clear()
j
{}
tup1=("john")
tup.extend(tup1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tup.extend(tup1)
AttributeError: 'tuple' object has no attribute 'extend'
tp=('john',2,4,'prince')
tt=('king')
tp.extend(tt)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tp.extend(tt)
AttributeError: 'tuple' object has no attribute 'extend'
