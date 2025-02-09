'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 'From ' line 
by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle :
    if line.startswith('From ') :
        l = line.rstrip().split()
        #print(l)
        time = l[5]
        #print(time)
        #print(time.split(':'))
        tlist = time.split(':')
        hour = tlist[0]
        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, val in counts.items() :
     newtup = (key, val)
     lst.append(newtup)

lst = sorted(lst)

for key, val in lst :
    print(key, val)
    
