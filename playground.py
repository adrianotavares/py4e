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

# Networking - HTTP - Socket 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data.decode())
mysock.close()