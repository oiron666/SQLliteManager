import sqlite3

def sql_con(database):
    try:
        con = sqlite3.connect(database)
        return con
    except Error:
        print('Error')

def sql_expedia_read(con, table):
    try:
        print("The SQLite connection is open")
        cursorObj = con.cursor()
        tableName = table
        sqlite_select_Query = "select batch, quantity, analyst, batchdate from " + tableName
        cursorObj.execute(sqlite_select_Query)
        record = cursorObj.fetchall()
        cursorObj.close()
        recordList = []
        for element in record:
            elementToList = list(element)
            recordList.append(elementToList)
            #print(recordList)
        return recordList
    except sqlite3.Error as error:
        print("Error while using sql_expedia_read", error)
    finally:
        if (con):
            con.close()
            print("The SQLite connection is closed")

def sql_expedia_insert(con, list, table):
    try:
        cursorObj = con.cursor()
        for element in list:
            entities = (element[0], element[1], element[2], element[3])
            print(entities)
            cursorObj.execute('INSERT INTO (batch, quantity, analyst, batchdate) VALUES(?, ?, ?, ?)', entities)
            con.commit()
        cursorObj.close()
    except sqlite3.Error as error:
        print("Error while using sql_insert_expedia", error)
    finally:
        if (con):
            con.close()
            print("The SQLite connection is closed")
