print ("Hello world!")

print ("1+2=",1+2)

print ("1/2=",1/2)

# get exact division
print ("1//2=",1//2)

# get mod
print ("1%2=",1%2)
print ("2.75%0.5=",2.75%0.5)
print ("9%3=",9%3)

# get square
print ("2**3=",2**3)
# priority of operator
print ("-3**2=",-3**2)
print ("(-3)**2=",(-3)**2)

# long integer, -2147483647<integer<2147483647
print ("1000000000000000000=",1000000000000000000)
print ("1234567892564879*1234567892564879=",1234567892564879*1234567892564879)

# hexadecimal and octonary
print ("hexadecimal 0xAF=",0xAF)
# print ("010=",010)

# variables: variable_name: charactor, number, and _, but cannot begin with number
x = 3
print ("x was assigned value 3, so x=", x)

# get user input
'''
input_1 = input ("Please input the first value: ")
print ("Your first input is ", input_1)
input_2 = input ("Please input the second value: ")
print ("Your second input is ", input_2)
print ("string sum input_1 + input_2 =", input_1+input_2)
print ("integer sum input_1 + input_2 =", int(input_1)+int(input_2))
'''

# check if it's sharp time
#if time%60==0: print ("it's sharp time!")
#if time%60!=0: print ("it's non-sharp time!")

# build-in function
print ("build-in function power - pow: pow(2,3) =", pow(2,3))
print ("build-in function power - pow: 10 + pow(2,3*5)/3.0 =", 10+pow(2,3*5)/3.0)
print ("build-in function absolute - abs: abs(-10) =", abs(-10))
print ("build-in function rounding - round: round(1/2) =", round(1/2))

# module function, need import first
import math
print ("module function round down - floor: math.floor(32.9) =", math.floor(32.9))
print ("module function rounding up, ceiling - ceil: math.ceil(32.9) =", math.ceil(32.9))

# NOT RECOMMEND!!!: module function, import and no need prefix
from math import sqrt
print ("module function square root - sqrt: sqrt(9) =", sqrt(9))

# module function, import cmath, complex math
import cmath
# imaginary number will be ended by j, for example, cmath.sqrt(-1)=1j
print ("import complex math - cmath.sqrt(-1) =", cmath.sqrt(-1))
print ("complex math: (1+3j)*(9+4j) =", (1+3j)*(9+4j))

# REMOVED: raw_input has been removed by python 3.0: raw_input("What is your name? ")

# escape sequence
print ('Let\'s go!')
print ("Let's go!")
print ("\"Let's go!\"")

# joint strings
string_1 = "Hello, "
string_2 = "world!"
print ("string_1 =", string_1)
print ("string_2 =", string_2)
print ("string_1 + string_2 =", string_1+string_2)

# str and repr, repr(boject)
print ("str('Hello, world!') =", str('Hello, world!'))
print ("repr('Hello, world!') =", repr('Hello, world!'))

# transfered meaning
print ("Hello, \nworld!")
print ("C:\\Program Files")
print (r'C:\test\folder1\next')
print (r'C:\test\folder1\next''\\')
print (r'Let\'s go!')

# unicode, Deprecated, because in python 3.0, all strings are Unicode
print (u'Hello, world!')

greeting = "Hello"
print ("greeting[0] =", greeting[0])
print ("greeting[-1] =", greeting[-1])

# print year, month, day in number
'''
months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]

endings = ['st', 'nd', 'rd'] + 17*['th']\
	+ ['st', 'nd', 'rd'] + 7*['th']\
	+ ['st']

year = input('Year: ')
month = input('Month (1-12): ')
day = input ('Day (1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print (month_name + ' ' + ordinal + ', ' + year)
'''

# slicing
tag = '<a href="http://www.python.org">Python web site</a>'
print ("tag[9:30] =", tag[9:30])
print ("tag[32:-4] =", tag[32:-4])

numbers = [1,2,3,4,5,6,7,8,9,10]
print ("numbers[3:6] =", numbers[3:6])
print ("numbers[7:10] =", numbers[7:10])
print ("numbers[-3:-1] =", numbers[-3:-1])
print ("numbers[-3:] =", numbers[-3:])
print ("numbers[:3] =", numbers[:3])
print ("numbers[:] =", numbers[:])
# slicing: step length, step length cannot be 0, negative means from right to left.
print ("numbers[0:10:1] =", numbers[0:10:1])
print ("numbers[0:10:2] =", numbers[0:10:2])
print ("numbers[3:6:3] =", numbers[3:6:3])
print ("numbers[::4] =", numbers[::4])
print ("numbers[8:3:-1] =", numbers[8:3:-1])
print ("numbers[10:0:-2] =", numbers[8:3:-2])
print ("numbers[0:10:-2] =", numbers[0:10:-2])
print ("numbers[::-2] =", numbers[::-2])
print ("numbers[5::-2] =", numbers[5::-2])
print ("numbers[:5:-2] =", numbers[:5:-2])

# slicing: get domain name
'''
url = input('Please enter the URL: ')
domain = url[11:-4]
print ("Domain name: "+domain)
'''

# adding
print ("[1,2,3]+[4,5,6] =", [1,2,3]+[4,5,6])
print ("Hello,+world! =", 'Hello, '+'world!')


# multiple
print ("python*5 =", 'python'*5)
print ("[42]*10 =", [42]*10)

# None, null sequence, and initialize
print ("[None]*10 =", [None]*10)

#sentence = input("Sentence: ")
sentence = "He's a naughty boy!"
screen_width = 80
text_width = len(sentence)
box_width = text_width + 4
left_margin = (screen_width - box_width) //2

print
print (' '*left_margin+'+' + '-'*(box_width-2)+'+')
print (' '*left_margin+'| ' + ' '*text_width+' |')
print (' '*left_margin+'| ' + sentence +' |')
print (' '*left_margin+'| ' + ' '*text_width+' |')
print (' '*left_margin+'+' + '-'*(box_width-2)+'+')
print

# "in" usage
permissions = 'rw'
print ('w' in permissions)
print ('x' in permissions)
users = ['mlh', 'foo', 'bar']
#input ('Enter your user name: ') in users
subject = '$$$ Get rich now!!! $$$'
print ('$$$' in subject)

database = [
	['albert', '1234'],
	['dilbert', '4242'],
	['smith', '7524'],
	['jones', '9843']
]
#username = input('User name: ')
#pin = input('PIN code: ')
username = "albert"
pin = "1234"
if [username, pin] in database: print ('Access granted')

# len, max, min
numbers = [100, 34, 678]
print ("len(numbers) =",len(numbers)) 
print ("max(numbers) =", max(numbers))
print ("min(numbers) =", min(numbers))
print ("max(2,3) =", max(2,3))
print ("min(9,3,2,5) =", min(9,3,2,5))

# list
print ("list('Hello') =", list('Hello'))
# assign value
x = [1,1,1]
x[1] = 2
print ("x =", x)
# delete elements
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print ("names list after deleted: ", names)
# assign value by piece
name = list('Perl')
print ("name =", name)
name[2:] = list('ar')
print ("name =", name)
name = list('Perl')
name[1:] = list('ython')
print ("name =", name)
# insert
numbers = [1,5]
numbers[1:1] = [2,3,4]
print ("numbers =", numbers)
numbers[1:4] = []
print ("numbers =", numbers)

# append
lst = [1,2,3]
lst.append(4)
print ("lst.append(4) =", lst)

# count
print ("count the number of 'to' =", ['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
x = [[1,2],1,1,[2,1,[1,2]]]
print ("x.count(1) =", x.count(1))
print ("x.count([1,2]) =", x.count([1,2]))

# extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print ("extend a by b =", a)
print ("a+b =", a+b)
print ("a=a+b, then a=", a)
a[len(a):] = b
print ("a[len(a):]=b, then a=", a)

# index
knights = ['We','are','the','knights','who','say','ni']
print ("knights.index('who') =", knights.index('who'))

# insert
numbers = [1,2,3,5,6,7]
numbers.insert(3,'four')
print ("numbers.insert(3,'four') =", numbers)
numbers = [1,2,3,5,6,7]
numbers[3:3] = ['four']
print ("numbers[3:3] =", numbers)

# pop: remove the last one in a list, then return the value of the last one.
x = [1,2,3]
print ("x.pop =", x.pop())
print ("x =", x)
print ("x.pop(0) =", x.pop(0))
print ("x =", x)
x = [1,2,3]
print ("x.append(x.pop()) =", x.append(x.pop()))

# remove
x = ['to','be','or','not','to','be']
x.remove('be')
# only removed the first one
print ("x.remove('be') =", x)

# reverse
x = [1,2,3]
x.reverse()
print ("x.reverse() =", x)
# reversed() will return an iterator, not a list, use list to convert it to list.
x = [1,2,3]
print ("list(reversed(x)) =", list(reversed(x)))

# sort: it will sort and change the original list at the same time.
x = [4,6,2,1,7,9]
x.sort()
print ("x.sort =", x)
# keep the original list
x = [4,6,2,1,7,9]
y = x[:]
y.sort()
print ("x =", x)
print ("y.sort() =", y)
# sorted, another way to keep the copy of list
x = [4,6,2,1,7,9]
y = sorted(x)
print ("x =", x)
print ("sorted(x) =", y)
print ("sorted('Python') =", sorted('Python'))

# advanced sorting
# cmp was deprecated
# sorted by length
x = ['aardvark','abalone','acme','add','aerate']
x.sort(key=len)
print ("x.sort(key=len) =", x)
# reversed sorted
x = [4,6,2,1,7,9]
x.sort(reverse=True)
print ("x.sort(reverse=True) =", x)

# tuple
# convert list to tuple
print ("tuple([1,2,3]) =", tuple([1,2,3]))
print ("tuple('abc') =", tuple('abc'))
# keep the original tuple
print ("tuple((1,2,3)) =", tuple((1,2,3)))
x = 1,2,3
print ("x[1] =", x[1])
print ("x[0:2] =", x[0:2])

# string
# format string
format = "Hello, %s, %s enough for ya?"
values = ('world', 'Hot')
print (format%values)
# format floating number
format = "Pi with three decimals: %.3f"
from math import pi
print ("format%pi =", format%pi)
# template string
from string import Template
s = Template('$x, glorious $x!')
print ("s.substitute(x='slurm') =", s.substitute(x='slurm'))
s = Template("It's ${x}tastic!")
print ("s.substitute(x='slurm') =", s.substitute(x='slurm'))
s = Template("Make $$ selling $x!")
print ("s.substitute(x='slurm') =", s.substitute(x='slurm'))
# using dictionary variables
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print ("s.substitute(d) =", s.substitute(d))
# using tuple to format string
print ("'%s plus %s equals %s' % (1,1,2) =", '%s plus %s equals %s'%(1,1,2))
# simple convertion
print ("'Price of eggs: $%d' % 42 =", 'Price of eggs: $%d' % 42)
print ("'Hexadecimal price of eggs: %x' % 42 =", 'Hexadecimal price of eggs: %x' % 42)
from math import pi
print ("'Pi: %f...' % pi =", 'Pi: %f...' % pi)
print ("'Very inexact estimate of pi: %i' % pi =", 'Very inexact estimate of pi: %i' % pi)
#print ("'Using str: %s' % 42L =", 'Using str: %s' % 42L)
#print ("'Using repr: %r' % 42L =", 'Using repr: %r' % 42L)
# width and precision
print ("'%10f' % pi =", '%10f'%pi)  # width = 10
print ("'%10.2f' % pi =", '%10.2f' % pi) # width =10, precision=2
print ("'%.2f' % pi =", '%.2f' % pi) # precision=2
print ("'%.5s' % 'Guido van Rossum' =", '%.5s' % 'Guido van Rossum')
# symbol, alignment, and 0 filling
print ("'%010.2f' % pi =", '%010.2f' % pi) # 0 means width =10, and fill with 0
print ("'%-10.2f' % pi =", '%-10.2f' % pi) # - means left alignment
# null (" ")
#print ("'% 5d' % 10 + \\n + ('%+5d' % -10)F =", '% 5d' % 10 + '\n' + ('% 5d' % -10)F)
#print (('% 5d' % 10) + '\n' + ('% 5d' % -10)F)
print (('%+5d' % 10) + '\n' + ('%+5d' % -10))

# example for string format
width = 35
price_width = 10
item_width = width -price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print ('='*width)
print (header_format % (item_width, 'Item', price_width, 'Price'))
print ('-'*width)

print (format % (item_width, 'Apples', price_width, 0.4))
print (format % (item_width, 'Pears', price_width, 0.5))
print (format % (item_width, 'Cantaloupes', price_width, 1.92))
print (format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8))
print (format % (item_width, 'Prunes (4 lbs.)', price_width, 12))

print ('='*width)

# find
print ("With a moo-moo here. and a mo-moo there.find('moo') =", 'With a moo-moo here. and a mo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print ("title.find('Monty') =", title.find('Monty'))
print ("title.find('Python') =", title.find('Python'))
print ("title.find('Flying') =", title.find('Flying'))
print ("title.find('Zirquss') =", title.find('Zirquss'))

subject = '$$$ Get rich now!!! $$$'
print ("subject.find('$$$') =", subject.find('$$$'))
print ("subject.find('$$$', 1) =", subject.find('$$$, 1')) # only provide the starting point
print ("subject.find('!!!') =", subject.find('!!!'))
print ("subject.find('!!!',0,16) =", subject.find('!!!',0,16)) # provide the starting and end points

# join: the opposite function of split, all elements should be string.
seq = ['1','2','3','4','5']
sep = '+'
print ("sep.join(seq) =", sep.join(seq))
dirs = '','usr','bin','env'
print ("'/'.join(dirs) =", '/'.join(dirs))
print ('C:'+'\\'.join(dirs))

# lower
print ("Trondheim Hammer Dance'.lower() =", 'Trondheim Hammer Dance'.lower())
# No distinct lowercase and uppercase
name = 'Gumby'
names = ['gumby','smith','jones']
if name.lower() in names: print ('Found it!')

# title and capwords
print ("'that's all folks'.title() =", 'that\'s all folks'.title())
import string
#print ("string.capwords(\"that's all, folks\"") =", string.capwords("that's all, folks"))

# replace
print ("'This is a test'.replace('is','eez') =", 'This is a test'.replace('is','eez'))

# split, the opposite function of join
print ("'1+2+3+4+5'.split('+') =", '1+2+3+4+5'.split('+'))
print ("'/usr/bin/env'.split('/') =", '/usr/bin/env'.split('/'))
print ("'Using the default'.split()", 'Using the default'.split())

# strip
print ("'    internal whitespace is kept    '.strip() =", '    internal whitespace is kept    '.strip())
names = ['gumby','smith','jones']
name = 'gumby '
if name in names: print ('Found it - no strip()!')
if name.strip() in names: print ('Found it! - with strip()')
# use strip to remove some disgard character, list them as parameters
print ("'*** SPAM * for * everyone!!! ***'.strip(' *!') =", '*** SPAM * for * everyone!!! ***'.strip(' *!')) # this way only remove both ends' character, not the middle ones

# translate
# maketrans doesn't exist in python 3.0, should use string.maketrans()
'''
from string import maketrans
table = maketrans('cs','kz')
print ("len(table) =", len(table))
'''

# dictionary
phonebook = {'Alice':'2341', 'Beth':'9102', 'Cecil':'3258'}
items = [('name', 'Gumby'),('age', 42)]
d = dict(items)
print ("dictionary d =", d)
print ("d['name'] =", d['name'])
d = dict(name='Gumby', age=42)
print ("dictionary d =", d)

# dictionary and list
x = [None]*43 # list: need initialize first
x[42] = 'Foobar'
print ("x is a list, need initialize first, x[42] =", x[42])
x = {}
x[42] = 'Foobar'
print ("x is a dictionary, x[42] =", x[42])

# dictionary example
people = {
	'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
	},
	'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
	},
	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}
}

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

#name = input('Name: ')
name = 'Alice' 
#request = input('Phone number (p) or address (a)?')
request = 'p'

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people: print ("%s's %s is %s." % (name, labels[key], people[name][key]))

# dictionary format
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print ("Cecil's phone number is %(Cecil)s." % phonebook)

# dictionary format for template
template = '''<html>
	<head><title>%(title)s</title></head>
	<body>
		<h1>%(title)s</h1>
		<p>%(text)s</p>
	</body>
</html>'''
data = {'title': 'My Home Page', 'text':'Welcome to my home page!'}
print (template % data)

# dictionary function: clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print ("dictionary d=",d)
returned_value = d.clear()
print ("d.clear =", returned_value)
# clear: case 1
x = {}
y = x
x['key'] = 'value'
print ("original y =", y)
x = {}
print ("after x = {}, y =", y)
# clear: case 2
x = {}
y = x
x['key'] = 'value'
print ("original y =", y)
x.clear()
print ("after x.clear, y =", y)

# dictionary function: copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print ("y =", y)
print ("x =", x)

# dictionary function: deepcopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print ("copy usage: c =", c)
print ("deepcopy usage: dc =", dc)

# dictionary function: fromkeys, to setup new dictionary
dic = {}.fromkeys(['name','age'])
print ("fromkeys usage: dic =", dic)
print ("dict.fromkeys =", dict.fromkeys(['name', 'age']))
print ("dict.fromkeys =", dict.fromkeys(['name', 'age'], '(unknown)'))

# dictionary function: get, to access dictionary items
d = {}
print ("d.get('name') =", d.get('name')) # key not exist, but no exception for get
print ("d.get('name', 'N/A') =", d.get('name', 'N/A')) # customize default value
d['name'] = 'Eric'
print ("d.get('name') =", d.get('name')) # key exists

# example for get
labels = {
	'phone': 'phone number',
	'addr': 'address'
}
#name = input('Name: ')
name = 'test'
#request = input('Phone number (p) or address (a)? ')
request = 'p'

key = request # if reuest not 'p' or 'a'
if request == 'p':key = 'phone'
if request == 'a':key = 'addr'
# use get() to provide default value
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print ("%s's %s is %s." % (name, label, result))

# items and iteritems, 3.0 disgard iteritems
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam':0}
print ("d.items() =", d.items())
#it = d.iteritems()

# keys and iterkeys, 3.0 disgard iteritems

# pop: get key value, then remove key-value from dictionary
d = {'x':1, 'y':2}
print ("d.pop('x') =", d.pop('x'))
print ("d =", d)

# popitem
d = {'url':'http://www.python.org', 'spam':0, 'title':'Python Web Site', }
print ("d =", d)
print ("d.popitem() =", d.popitem())
print ("d =", d)

# setdefault
d = {}
print ("d.setdefault('name','N/A') =", d.setdefault('name','N/A'))
print ("d =", d)
d['name'] = 'Gumby'
print ("d.setdefault('name','N/A') =", d.setdefault('name', 'N/A'))
print ("d =", d)
d = {}
print ("d.setdefault('name') =", d.setdefault('name'))
print ("d =", d)

# update: use one dictionary item to update another dictionary
d = {
	'title': 'Python Web Site',
	'url': 'htpp://www.python.org',
	'changed': 'Mar 14 22:09:15 MET 2008'
}
x = {'title': 'Python Language Website'}
d.update(x)
print ("d =", d)

# values and itervalues
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print ("d.values =", d.values())

# print
print ('Age: ', 42)
print (1,2,3)
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello'
print (greeting, salutation, name)
print (greeting+',', salutation, name)

# import
#import somemodule
#from somemodule import somefunction
#from somemodule import somefunction, anotherfunction, yetanotherfunction
#from somemodule import *
#module1.open(...)
#module2.open(...)

import math as foobar
print ("foobar.sqrt(4) =", foobar.sqrt(4))
from math import sqrt as foobar
#from module1 import open as open1
#from module2 import open as open2

# assignment
x,y,z = 1,2,3
print ("x,y,z =", x,y,z)
# exchange
x,y = y,x
print ("x,y,z =", x,y,z)
# sequence unpacking
values = 1,2,3
print ("values =", values)
x,y,z = values
print ("x =", x)
scoundrel = {'name':'Robin', 'girlfriend':'Marion'}
key,value = scoundrel.popitem()
print ("key =", key)
print ("value =", value)
#a,b,rest* = [1,2,3,4]

# chained assignment
#x = y = somefunction()

# augmented assignment
x = 2
x += 1
x *= 2
print ("x =", x)
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print ("fnord =", fnord)


# bull
print ("True =", True)
print ("False =", False)
print ("True == 1 is", True == 1)
print ("False == 0 is", False == 0)
print ("True + False + 42 =", True+False+42)
print ("bool('I think, therefore I am') =", bool('I think, therefore I am'))
print ("bool(42) =", bool(42))
print ("bool('') =", bool(''))
print ("bool(0) =", bool(0))

# condition and if
#name = input('What is your name?')
name = 'Gumby'
if name.endswith('Gumby'):print('Hello, Mr. Gumby')

# else
#name = input('What is your name?')
name = 'test'
if name.endswith('Gumby'):
	print('Hello, Mr. Gumby')
else:
	print('Hello, stranger')

# elif, the abbreviation of elseif
#num = input('Enter a number: ')
num = int('-6')
if num > 0:
	print ('The number is positive')
elif num < 0:
	print ('The number is negative')
else:
	print ('The number is zero')

# nesting
#name = input('What is your name? ')
name = 'test'
if name.endswith('Gumby'):
	if name.startswith('Mr.'):
		print ('Hello, Mr. Gumby')
	elif name.startswith('Mrs.'):
		print ('Hello, Mrs. Gumby')
	else:
		print ('Hello, Gumby')
else:
	print ('Hello, Stranger')

# is 
x = y = [1,2,3]
z = [1,2,3]
print ("x == y is", x == y)
print ("x == z is", x == z)
print ("x is y", x is y)
print ("x is z", x is z)

x = [1,2,3]
y = [2,4]
print ("x is not y =", x is not y)
del x[2]
y[1] = 1
y.reverse()
print ("x == y is", x == y)
print ("x is y =", x is y)

# in
#name = input('What is your name? ')
name = 'test'
if 's' in name: 
	print ('Your name contains the letter "s".')
else:
	print ('Your name does not contain the letter "s".')

# string comparison
print ("alpha < beta =", 'alpha' < 'beta')
print ("FnorD.lower() == Fnord.lower() is", 'FnOrD'.lower() == 'Fnord'.lower())
print ("[1,2] < [2,1] =", [1,2] < [2,1])
print ("[2,[1,4]] < [2,[1,5]]", [2,[1,4]] < [2,[1,5]])

# bull
number = int('7')
if number <= 10:
	if number >= 1:
		print ('Great!')
	else:
		print ('Wrong!')
else:
	print ('Wrong!')

# another way
number = int('7')
if number <= 10 and number >= 1:
	print ('Great!')
else:
	print ('Wrong!')

# assert: set check point
'''
age = 10
assert 0<age<100
age = -1
assert 0<age<100
'''

'''
age = -1
assert 0<age<100, 'The age must be realistic'
'''

# loop
'''
x = 1
while x <= 100:
	print (x)
	x += 1
'''

 # for
'''
 words = ['this', 'is', 'an', 'ex', 'parrot']
 for word in words:
 	print (word)
'''

numbers = [0,1,2,3,4,5,6,7,8,9]
for number in numbers:
	print (number)

'''
for number in range(1,101):
	print (number)
'''

d = {'x':1, 'y':2, 'z':3}
for key in d:
	print (key, 'corresponds to', d[key])

for key, value in d.items():
	print (key, 'corresponds to', value)

# iterating tools
names = ['anne', 'beth', 'george', 'damon']
ages = [12,45,32,102]
for i in range(len(names)):
	print (names[i], 'is', ages[i], 'years old')
# another way
zip(names, ages)
for name, age in zip(names, ages):
	print (name, 'is', age, 'years old')

# index iteration
'''
strings = 'an example for indexing iteration'
for string in strings:
	if 'am' in string:
		index = strings.index(string) # Search for the string in the list of strings
		strings[index] = '[censored]'
print (string)
'''

'''
index = 0
strings = 'an example for indexing iteration'
for string in strings:
	index = strings.index(string)
	print ("string ", string)
	print ("index =", index)
	if 'am' in strings:
		print ("am in strings")
		#strings[index] = '[censored]'
index += 1
'''

'''
index = 0
strings = 'an example for indexing iteration'
for index, string in enumerate(strings):
	if 'am' in strings:
		print ("enumerate example: am in strings")
		#strings[index] = '[censored]'
index += 1
'''

# reversed and sorted
print ("sorted(4,3,6,8,3) =", sorted([4,3,6,8,3]))
print ("sorted('Hello, world!') =", sorted('Hello, world!'))
print ("list(reversed('Hello, world!')) =", list(reversed('Hello, world!')))
print ("''.join(reversed('Hello, world!')) =", ''.join(reversed('Hello, world!')))

# jump out iteration: 
# break
from math import sqrt
for n in range(99,0,-1):
	root = sqrt(n)
	if root == int(root):
		print (n)
		break

# continue (rarely used)
'''
for x in seq:
	if condition1: continue
	if condition2: continue
	if condition3: continue

	do_something()
	do_something_else()
	do_another_thing()
	etc()
'''
# "if" is enough for iteration
'''
for x in seq:
	if not (condition1 or condition2 or condition3):
		do_something()
		do_something_else()
		do_another_thing()
		etc()
'''

# while True/break
# for example with dumy value
'''
word = 'dumy'
while word:
	word = input('Please enter a word: ')
	print ('The word was ' + word)
	'''
# no dumy value
'''
word = input('Please enter a word: ')
while word:
	print ('The word was ' + word)
	word = input('Please enter a word: ')
'''
# while True/break
'''
while True:
	word = input('Please enter a word: ')
	if not word: break
	print ('The word was ' + word)
'''

# else
'''
broke_out = False
for x in seq:
	do_something(x)
	if condition(x):
		broke_out = True
		break
	do_something_else(x)
if not broke_out:
	print ("I didn't break out!")
'''

# use else to rewrite
from math import sqrt
for n in range(99,80,-1):
	root = sqrt(n)
	if root == int(root):
		print (n)
		break
	else:
		print ("Didn't find it!")

# list comprehension, lightway iteration
print ("[x*x for x in range(10)] =", [x*x for x in range(10)])
print ("[x*x for x in range(10) if x%3 == 0] =", [x*x for x in range(10) if x%3 == 0])
print ("[(x,y) for x in range(3) for y in range(3)] =", [(x,y) for x in range(3) for y in range(3)])
# use "for" to create same list
result = []
for x in range(3):
	for y in range(3):
		result.append((x,y))
print ("result =", result)
# use with "if"
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print ("[b+'+'+g for b in boys for g in girls if b[0] == g[0]] =", [b+'+'+g for b in boys for g in girls if b[0] == g[0]])
# better solution
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
	letterGirls.setdefault(girl[0],[]).append(girl)
print ("[b+'+'+g for b in boys for g in letterGirls[b[0]]] =", [b+'+'+g for b in boys for g in letterGirls[b[0]]])

# pass, del and exec
# "pass" as a placeholder
if name == 'Ralph Auldus Melish':
	print ('Welcome!')
elif name == 'Enid':
	# not completed yet, so use "pass" to skip temporarily
	pass
elif name == 'Bill Gates':
	print ('Access Denied')

# del: python only delete name, which means remove the reference and the name, but not the value.
# assign none to delete
scoundrel = {'age':42, 'first name':'Robin', 'last name':'of Locksley'}
robin = scoundrel
print ("scoundrel =", scoundrel)
print ("robin =", robin)
scoundrel = None
print ("robin after scoundrel = None: ", robin)






# need user's operation
#input("Press <enter>")