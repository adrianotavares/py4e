'''
Welcome Adriano de Pinho Tavares from Using Databases with Python

To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
(Must have a .sqlite suffix)
Hint: The top organizational count is 536.

You do not need to export or convert the database - simply upload the .sqlite file that your program creates.
See the example code for the use of the connect() statement.

Counting Organizations

This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.
Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the 
loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to 
disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, 
there is a balance between the number of operations you execute between commits and the importance of not losing the results 
of operations that have not yet been committed.
'''

import sqlite3

conn = sqlite3.connect('./db/orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'

fh = open(fname)
for line in fh :
    if not line.startswith('From: ') :
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    # print(org)
    
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()
    
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print('count: ', row[1], ' \t org: ',str(row[0]))
    
     

