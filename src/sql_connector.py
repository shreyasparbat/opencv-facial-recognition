import MySQLdb

"""
Returns all Users in DB
"""
def selectAll():    
    db = open()
    cur = db.cursor()
    cur.execute("SELECT * FROM user_names")
    results = cur.fetchall()
    cur.close()
    db.close()
    return results

"""
Inserts a new User into DB
"""
def insert(name):    
    db = open()
    cur = db.cursor()
    num_rows = len(selectAll())

    sql = "INSERT INTO user_names values ({n}, '{nm}')".format(n=num_rows+1, nm=name)
    cur.execute(sql)
    cur.close()    
    db.close()
    return num_rows+1

"""
Retrieves name of user with a given ID
"""
def retrieve(id):    
    db = open()
    cur = db.cursor()

    sql = "select name from user_names where id={i}".format(i=id)
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()    
    db.close()
    return result[0]
    
"""
Used to connect to database
"""
def open():
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="facial_recognition")
    return db