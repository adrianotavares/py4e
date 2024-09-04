# astr = 'Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

# tot = 0 
# for i in [5, 4, 3, 2, 1] :
#     tot = tot + 1
# print(tot)

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#      print('Happy New Year:',  friend)
# print('Done!')

# zork = 0
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + thing
# print('After', zork)

# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)

# data = [ 'Joseph', 'Glenn', 'Sally' ]
# # print(friends[2])

# fruit = 'Banana'
# # fruit[0] = 'b'
# print(fruit)


# print(len(data))

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(len(c))

# t = [9, 41, 12, 3, 74, 15]
# print(len(t))
# print('t=' + str(t)) 
# print('t=' + str(t[2:4]))

# c = 0
# print(len(t))
# while c < len(t) :
#     print(t[c])
#     print (c)
#     c = c + 1
# print('Done')

# friends = [ 'Joseph', 'Glenn', 'Sally' ]
# friends.sort()
# print(friends[0])

# # List
# lst = list()
# lst.append(21)
# lst.append(183)
# print(lst)
# lst[0] = 23
# print(lst)

# # Dictionary
# ddd = dict()
# ddd['age'] = 21
# ddd['course'] = 182
# print(ddd)
# ddd['age'] = 23
# print(ddd)

# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)
# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc)
    
# # Count the number of times a word appears in a file
# counts = dict()
# print('Enter a line of text:')
# line = input('')
# words = line.split()
# print('Words:', words)
# print('Counting...')
# for word in words :
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)

# # list of keys, values and items
# jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())

# # Two iteration variables
# jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# for aaa,bbb in jjj.items() :
#     print(aaa, bbb)

# # Count the number of times a word appears in a file    
# # returns biggest word and its count
# name = input('Enter file:')
# handle = open(name, 'r')
# counts = dict()
# for line in handle :
#     words = line.split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word, count in counts.items() :
#     if bigcount is None or count > bigcount :
#         bigword = word
#         bigcount = count
            
# print(bigword, bigcount)

# # tuples
# (x,y) = (4, 'fred')
# print(y)
# (a,b) = (99, 98)
# print(a)

# print((0, 1, 2) < (0, 1, 3))
# print((0,1,200000) < (0,3,2))

# d = {'a':10, 'c':22, 'b':1}
# print(d.items())
# print(sorted(d.items()))

# d = {'a':10, 'c':22, 'b':1}
# print(d.items())
# for k, v in sorted(d.items()) :
#     print(k, v)
    
# # Sort by values instead of keys
# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k, v in c.items() :
#     tmp.append( (v, k) )
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)
    
# # The top 10 most common words
# handle = open('romeo.txt')
# counts = dict()
# for line in handle :
#     words = line.split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1 
# lst = list()
# for key, val in counts.items() :
#      newtup = (val, key)
#      lst.append(newtup)
# lst = sorted(lst, reverse=True)
# for val, key in lst[:10] :
#     print(key, val)
    
# # Even shorter version
# c = {'a':10, 'b':1, 'c':22}
# print(sorted([(v,k) for k,v in c.items()]))
# print(sorted([(v,k) for k,v in c.items()], reverse=True))
    
# x , y = 3, 4
# print(y)    

# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)    

# data = [9, 41, 12, 3, 74, 15]
# data.sort(reverse=True)
# print(data)

# days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# print(days[2])

# Regular expression
# import re
# hand = open('mbox-short.txt')
# for line in hand :
#     line = line.rstrip()
#     if re.search('^From:', line) :
#         print(line)
#     if re.search('^X.*:', line) :
#         print(line)
#     if re.search('^X-\S*:', line) :
#         print(line)
    
# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(y)
# y = re.findall('[AEIOU]+', x)
# print(y)

# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)
# y = re.findall('^F.+?:', x)
# print(y)

# import re
# hand = open('mbox-short.txt')
# email = list()
# for line in hand :
#     if re.search(r'^From: (\S+@\S+)', line.rstrip()) :
#         email.append(re.findall(r'^From: (\S+@\S+)', line))
# print(email)

# import re
# lin = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)', lin)  
# print(y)

# import re
# lin = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
# y = re.findall('href="(.+)"', lin)  
# print(y)

# import re
# lin = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall(r'\S+@\S+', lin)  
# print(y)

# import re
# lin = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall(r'\S+?@\S+', lin)  
# print(y)

# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)

# # Networking - HTTP - Socket 
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True :
#     data = mysock.recv(512)
#     if len(data) < 1 :
#         break
#     print(data.decode())
# mysock.close()

# Characters, ASCII and unicode

# ASCII (0 to 255)
# print(ord('H'))
# print(ord('e'))
# print(ord('\n'))
# print(chr(72))
# print(chr(101))
# print(chr(10))

# UNICODE (0 to 4 billion)
# UTF-8 (8-bit variable length encoding)
# x = b'abc'
# print(type(x))
# x = 'abc'
# print(type(x))
# x = u'abc'
# print(type(x))
# x = u'我'
# print(x)

# encode and decode
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # unicode to bytes
# mysock.send(cmd)

# while True :
#     data = mysock.recv(512) # bytes
#     if len(data) < 1 :
#         break
#     print(data.decode()) # bytes to unicode
# mysock.close()

# urllib - higher level
# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# for line in fhand :
#     print(line.decode().strip())
    
# urlwords.py
# counting words in a file
# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand :
#     words = line.decode().split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# urllib2.py
# first  lines of code @ Google
# import urllib.request
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand :
#     print(line.decode().strip())
    
# BeautifulSoup Installation
# to run this, you need to install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags :
#     print(tag.get('href', None))
    
# import xml.etree.ElementTree as ET
# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''

# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Phone', tree.find('phone').text)
# print('Attr:', tree.find('phone').get('type'))
# print('Attr:', tree.find('email').get('hide'))

# XML - eXtensible Markup Language
# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>
# '''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))
# for item in lst :
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))
    
# JSON - JavaScript Object Notation
# import json
# data = '''
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''
# info = json.loads(data)
# print('Name:', info["name"])
# print('Phone:', info["phone"]["number"])
# print('Hide:', info["email"]["hide"])

# list of dictionaries 
# import json 
# input = '''
# [
#     { "id" : "001",
#       "x" : "2",
#       "name" : "Chuck"
#     } ,
#     { "id" : "009",
#       "x" : "7",
#       "name" : "Chuck"
#     }
# ]'''
# info = json.loads(input)
# print('User count:', len(info))
# for item in info :
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

# import json 
# input = '''
# [ "Glenn", "Sally", "Jen" ]
# '''
# info = json.loads(input)
# print('Type:', type(info))

# GeoJSON
# import urllib.request, urllib.parse
# import json, ssl

# # Heavily rate limited proxy of https://www.geoapify.com/ api
# serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     address = address.strip()
#     parms = dict()
#     parms['q'] = address

#     url = serviceurl + urllib.parse.urlencode(parms)

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'features' not in js:
#         print('==== Download error ===')
#         print(data)
#         break

#     if len(js['features']) == 0:
#         print('==== Object not found ====')
#         print(data)
#         break

#     # print(json.dumps(js, indent=4))

#     lat = js['features'][0]['properties']['lat']
#     lon = js['features'][0]['properties']['lon']
#     print('lat', lat, 'lon', lon)
#     location = js['features'][0]['properties']['formatted']
#     print(location)


# x = b'abc'
# print(type(x))
# # 3 japanes characters
# x = u'我你他'
# print(x)

# print(ord(x[0]))
# print(chr(25105))
# print(chr(20320))
# print(chr(20013))

# encode and decode
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # unicode to bytes
# mysock.send(cmd)

# while True :
#     data = mysock.recv(512) # bytes
#     if len(data) < 1 :
#         break
#     print(data.decode()) # bytes to unicode
# mysock.close()

# print(chr(108))
# print(chr(105))
# print(chr(115))
# print(chr(116))

# Object Oriented Programming in Python
# class PartyAnimal:
#     def __init__(self) :
#         print('I am constructed')
#         self.x = 0
    
#     def party(self) :
#         self.x = self.x + 1
#         print('So far', self.x)
        
#     def __del__(self) :
#         print('I am destructed', self.x)
        
# an = PartyAnimal()
# an.party()
# an.party()
# an.party()
# PartyAnimal.party(an)
# an.party()

# print ("Type ", type(an))   
# print("Dir ", dir(an))
# print("Type ", type(an.x))
# print("Type ", type(an.party))

# an = 42
# print('an contains', an)
# print ("Type ", type(an)) 

# Object Oriented Programming in Python
# class PartyAnimal:
#     def __init__(self, z) :
#         self.x = 0
#         self.name = z
#         print(self.name,'constructed')     
#     def party(self) :
#         self.x = self.x + 1
#         print(self.name,'party count ', self.x)
    
# s = PartyAnimal('Sally')
# s.party()
# j = PartyAnimal('Jim')
# j.party()
# s.party()

# inhreritance
# class PartyAnimal:
#     def __init__(self, z) :
#         self.x = 0
#         self.name = z
#         print(self.name,'constructed')
        
    
#     def party(self) :
#         self.x = self.x + 1
#         print(self.name,'party count ', self.x)
        
# class FootballFan(PartyAnimal):
    
#     def __init__(self, nam) :
#         super().__init__(nam)
#         self.points = 0
    
#     def touchdown(self) :
#         self.points = self.points + 7
#         self.party()
#         print(self.name, 'points', self.points)

# s = PartyAnimal('Sally')
# s.party()        
# j = FootballFan('Jim')
# j.party()
# j.touchdown()

# Databases - https://sqlitebrowser.org/

# CREATE TABLE "Ages" (
# 	"name"	TEXT,
# 	"age"	INTEGER
# );

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Gavin', 28);
# INSERT INTO Ages (name, age) VALUES ('Ellise', 31);
# INSERT INTO Ages (name, age) VALUES ('Carah', 35);
# INSERT INTO Ages (name, age) VALUES ('Samy', 28);
# INSERT INTO Ages (name, age) VALUES ('Kasey', 32);

# SELECT hex(name || age) AS X FROM Ages ORDER BY X

# SELECT hex(name || age) AS X FROM Ages ORDER BY X

# 43617261683335
# 456C6C6973653331
# 476176696E3238
# 4B617365793332
# 53616D793238

# Database - SQLLite
# import sqlite3
# conn = sqlite3.connect('./db/orgdb.sqlite')
# cur = conn.cursor()

# cur.execute('SELECT count FROM Counts WHERE org = ? ', ('xxx', ))
# row = cur.fetchone()
# print(type(row))
# print(row)

# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# fname = input('Enter file name: ')
# if len(fname) < 1 :
#     fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh :
#     if not line.startswith('From: ') :
#         continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
#     row = cur.fetchone()
#     if row is None :
#         cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
#     else :
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
#     conn.commit()
    
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# for row in cur.execute(sqlstr) :
#     print(str(row[0]), row[1])
    
# x = -1    
  
# if x < 2 :
#     print("Below 2")
# elif x < 20 :
#     print("Below 20")
# elif x < 10 :
#     print("Below 10")
# else :
#     print("Something else")
       
# if x < 2 :
#     print("Below 2")
# elif x < 0 :
#     print("Negative")
# else :
#     print("Something else")

# zap = "hello there bob"
# print(zap[4])

# x = 12
# if x < 5:
# print("smaller")
# else:
#     print("bigger")
# print("all done")

# def fred():
#    print("Zap")

# def jane():
#    print("ABC")

# jane()
# fred()
# jane()

# stuff = ['joseph', 'sally', 'walter', 'tim']
# print(stuff[2])

# def hello():
#     print("Hello")
#     print("There")

# x = 10
# x = x + 1

# x = -1
# for value in [3, 41, 12, 9, 74, 15] :
#     if value > x :
#         x = value
# print(x)

# total = 0
# for abc in range(5):
#     total = total + abc
#     print(total)
# print('total:', total)

# a = "123"
# b = 456
# c = a + b
# print(c)

# abc = "With three words"
# stuff = abc.split()
# print(stuff)

# abc = "With three words"
# stuff = abc.split()
# print(len(stuff))