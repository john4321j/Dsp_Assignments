Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#num data type int,float
ab=45
type(ab)
<class 'int'>
cb=-0.45
type(cb)
<class 'float'>
#Sequence
str="let's do it"
str
"let's do it"
str1="john"
str1[0:]
'john'
str1[1:2]
'o'
str1[1:3]
'oh'
str1[0]='g'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    str1[0]='g'
TypeError: 'str' object does not support item assignment

s="total states in usa # "
num=50
s+num
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s+num
TypeError: can only concatenate str (not "int") to str
#use str to convert it
str(num)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    str(num)
TypeError: 'str' object is not callable
a=["john",25,"prince",876]
list[0]
list[0]
l1="bread"
l2="cake"
l3="jam"
l=["bread","cake","jam"]
l
['bread', 'cake', 'jam']
l[0]
'bread'
l[2]
'jam'
l[0:1]
['bread']
l[:2]
['bread', 'cake']
l[0]="chips"
l
['chips', 'cake', 'jam']
 l[-1]
 
SyntaxError: unexpected indent
l[-1]
'jam'

food="cake","milk","juice"
tiffin="voda","idly","dosa"
items=food+tiffin
items
('cake', 'milk', 'juice', 'voda', 'idly', 'dosa')
len(l)
3
#tuple
t=("john",34,"cvb",89)
t
('john', 34, 'cvb', 89)
s+str(num)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s+str(num)
TypeError: 'str' object is not callable
#str operations
print()_
SyntaxError: invalid syntax
print(str)
let's do it
str
"let's do it"
print("str")
str
print("john")
john
str1="john"
str2="johnpaul"
str1=str2
str2
'johnpaul'
s="john"
s="paul"
print(s)
paul
#dictionary creating
d1={"john":468,"paul":789,"tom":789}
d["john"]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d["john"]
NameError: name 'd' is not defined. Did you mean: 'd1'?
d1["john"]
468
d1["abhi"]={889}
d1
{'john': 468, 'paul': 789, 'tom': 789, 'abhi': {889}}
del d1["paul"]
d
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'd1'?
d1
{'john': 468, 'tom': 789, 'abhi': {889}}
num1=5
num2=10
num1+num2
15
num1-num2
-5
numb1*num2
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    numb1*num2
NameError: name 'numb1' is not defined. Did you mean: 'num1'?
num1*num2
50
t=("john",23,"pail")
print(t)



