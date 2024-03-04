import os
import sqlite3
from sqlite3 import Error

#Merge the given directory with the given file path
def get_path(directory, file_path):
    return os.path.join(directory, file_path)

#Create the connection and get the cursor with the connection object
def create_connection(db_path):
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        print(
            "Connection to SQLite DB successful. Cursor has been created")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection, cursor

#Execute any kind of query with or without the query placeholder
def execute_query(connection, cursor, query, query_placeHolder=None):
    try:
        if query_placeHolder is None:
            cursor.execute(query)
        else:
            cursor.execute(query, query_placeHolder)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        pass

#Get all the rows of a table
def get_rows(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

# Walk throughout the directory, get the required info and insert into table
def insert_files(connection, cursor, directory, query_insert, table_name):
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            file_path = get_path(folder, file)
            file_size = os.stat(file_path).st_size
            file_extension = os.path.splitext(file_path)[1]
            
            execute_query(connection, cursor, query_insert, (file_path, file_size, file_extension))

    rows = get_rows(cursor, table_name)
    print("Inserted Rows:", rows)

def main():
    db_directory = 'C:\\Users\\HP\\Desktop'
    files_directory = 'C:\\Users\\HP\\Desktop\\Docs'
    db_name = 'app.db'
    my_file_extension = '.txt'
    table_name = 'FILE_INFO'
    max_numb = 10

    query_createTable = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
        FileID INTEGER PRIMARY KEY AUTOINCREMENT,
        FilePath VARCHAR(255) NOT NULL,
        FileSize BIGINT NOT NULL, -- Alternatively, INT if it is smaller
        FileExtension VARCHAR(10) NOT NULL
        );
    '''

    query_insert = f'INSERT INTO {table_name} (FilePath, FileSize, FileExtension) VALUES (?, ?, ?)'

    query_getNLargestFiles = f"""
        SELECT * FROM {table_name}
        ORDER BY FilePath DESC
        LIMIT ?"""
    
    query_fileExtension = f"""
        SELECT * FROM {table_name}
        WHERE FileExtension=?
        ORDER BY FileExtension DESC"""
    

    my_db_path = get_path(db_directory, db_name)
    my_connection, my_cursor = create_connection(my_db_path)

    try:
        # Create a table
        execute_query(my_connection, my_cursor, query_createTable)
        
        # Insert the files in the given directory and get the inserted rows
        insert_files(my_connection, my_cursor, files_directory, query_insert, table_name) 
        
        # Get n Largest Files
        execute_query(my_connection, my_cursor, query_getNLargestFiles, (max_numb,))
        
        # Print files with .txt extension
        execute_query(my_connection, my_cursor, query_fileExtension, (my_file_extension,))

    finally:
        #Finally, close the connection if it is still open
        if my_connection:
            my_connection.close()

if __name__ == '__main__':
    main()
