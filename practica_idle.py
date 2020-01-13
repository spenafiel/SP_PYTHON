Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 3**2
9
>>> 3*2
6
>>> 10-4
6
>>> 21/5
4.2
>>> 21//5
4
>>> "Hello word"
'Hello word'
>>> 'Hello word'
'Hello word'
>>> print("Hello Word")
Hello Word
>>> print("holá")
holá
>>> quit()
>>> 
================ RESTART: C:/Users/CEC/Desktop/01_hello_word.py ================
Hello word
>>> type(98)
<class 'int'>
>>> type(98.6)
<class 'float'>
>>> type("Hi!")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> 1<2
True
>>> 1>2
False
>>> 1==5
False
>>> 2==2
True
>>> 1!2
SyntaxError: invalid syntax
>>> 1!=2
True
>>> 1<=1
True
>>> 1<1
False
>>> str1="Cisco"
>>> str2="Networking"
>>> str3="Academy"
>>> space="  "
>>> print(str1+space+str2+space+str3)
Cisco  Networking  Academy
>>> print(str1+str2+str3)
CiscoNetworkingAcademy
>>> print(str1,str2,str3)
Cisco Networking Academy
>>> x=3
>>> print("This value of X is " + x)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print("This value of X is " + x)
TypeError: can only concatenate str (not "int") to str
>>> print("This value of X is " + str(x))
This value of X is 3
>>> print("This value of X is " + type(x))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print("This value of X is " + type(x))
TypeError: can only concatenate str (not "type") to str
>>> pi=22/7
>>> print(pi)
3.142857142857143
>>> print("[:.2f".format(pi))
[:.2f
>>> print("{:.2f}".format(pi))
3.14
>>> hostnames=["r1","r2","r3","s1","s2"]
>>> type(hostnames)
<class 'list'>
>>> len(hostnames)
5
>>> hostnames
['r1', 'r2', 'r3', 's1', 's2']
>>> p=["m1",2]
>>> type(p)
<class 'list'>
>>> hostnames[0]
'r1'
>>> hostnames[-1]
's2'
>>> hostnames[0]="RTR1"
>>> HOSTNAMES
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    HOSTNAMES
NameError: name 'HOSTNAMES' is not defined
>>> hostnames
['RTR1', 'r2', 'r3', 's1', 's2']
>>> del hostnames[3]
>>> hostnames
['RTR1', 'r2', 'r3', 's2']
>>> hostnames[-6]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    hostnames[-6]
IndexError: list index out of range
>>> textos=["m1","m3",15,56,45,65]
>>> type(textos)
<class 'list'>
>>> len(textos)
6
>>> textos
['m1', 'm3', 15, 56, 45, 65]
>>> textos[5]
65
>>> textos[6]="mas"
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    textos[6]="mas"
IndexError: list assignment index out of range
>>> del textos[5]
>>> textos
['m1', 'm3', 15, 56, 45]
>>> firstName = input("What is your first name?")
What is your first name? Xime
>>> print ("Hello" + firstName + "!")
Hello Xime!
>>> nativeVLAN =1
>>> 