import sqlite3

def sql_con(database):
    try:
        con = sqlite3.connect(database)
        return con
    except Error:
        print('Error')

def sql_read(con, table, columns, where):
    try:
        print("The SQLite connection is open")
        cursorObj = con.cursor()
        tableName = table
        columnNames = columns
        whereName = where
        sqlite_select_Query = 'select ' + columnNames ' from ' + tableName + ' where ' + whereName
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
        print("Error while using sql_expedia", error)
    finally:
        if (con):
            con.close()
            print("The SQLite connection is closed")

def sql_insert(con, table, columns, valuesList):
    try:
        cursorObj = con.cursor()
        insertCmd = 'INSERT INTO ' + table +' (' + columns + ') ' +  'VALUES(?, ?, ?, ?)'
        for element in valuesList:
            entities = (element[0], element[1], element[2], element[3])
            print(entities)
            cursorObj.execute(insertCmd, entities)
            con.commit()
        cursorObj.close()
    except sqlite3.Error as error:
        print("Error while using sql_insert", error)
    finally:
        if (con):
            con.close()
            print("The SQLite connection is closed")

def sql_update(con, table, set, where):
    try:
        cursorObj = con.cursor()
        updateCmd = 'UPDATE ' + table + ' SET ' + set + ' WHERE ' + where
        cursorObj.execute(updateCmd)
        con.commit()
    except sqlite3.Error as error:
        print("Error while using sql_insert", error)
    finally:
        if (con):
            con.close()
            print("The SQLite connection is closed")
