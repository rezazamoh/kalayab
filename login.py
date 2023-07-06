import sqlite3

# Sqlite database and table
def sqllitefile():
    global conn
    conn = sqlite3.connect('login_data.db')
    global c
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS login_details
                (USER_ID TEXT PRIMARY KEY NOT NULL,
                 PASSWORD TEXT NOT NULL);''')

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
        
def validity(user):
    if len(user) < 3 or len(user) > 16:
        return 0
    else:
        if isEnglish(user):
            return 1
        else:
            return 0
        
def register(user_id,password):
    sqllitefile()
    # If user_name already exists
    if conn.execute("select USER_ID from login_details where USER_ID like ?", (user_id,)).fetchone():
        return 'Duplicated Username!'
    else:
        if validity(user_id) and validity(password):
            c.execute("INSERT INTO login_details (USER_ID, PASSWORD) \
                VALUES (?, ?)", (user_id, password))
            conn.commit()
            c.close()
            conn.close()
            return '1'
        else:
            return 'Not a Valid Username or Pass'
    
def login(user_id,password):
    sqllitefile()
    #Check user
    user_id_exists = c.execute("select USER_ID from login_details where USER_ID like ?", (user_id,)).fetchone()
    if not user_id_exists:
        return 'No such username!'
    else:
        #Chcek pass
        password_id_exists = c.execute("select password from login_details \
        where user_id = ? and password = ?", (user_id, password,)).fetchone()
        if password_id_exists:
            return '0'
        else:
            return 'Password is not correct!'    

def add_to_loved(user_id,title,link):
    sqllitefile()
    try:
        loved_list = c.execute("select loved_items from login_details \
            where user_id = ?", (user_id)).fetchone()
    except:
        loved_list = {}
        loved_list[title] = link
        
    c.execute("INSERT INTO login_details (USER_ID, loved_items) \
        VALUES (?, ?)", (user_id, loved_list))
    conn.commit()
    c.close()
    conn.close()

def delete_from_loved(user_id,title,link):
    sqllitefile()
    loved_list = c.execute("select loved_items from login_details \
        where user_id = ?", (user_id)).fetchone()
    if loved_list:
        del loved_list[title]
    c.execute("INSERT INTO login_details (USER_ID, loved_items) \
        VALUES (?, ?)", (user_id, loved_list))
    conn.commit()
    c.close()
    conn.close()