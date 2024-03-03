import os
import mysql.connector
from mysql.connector import Error

    #Merge the given directory with the given file path
def get_path(directory, file_path):
    return os.path.join(directory, file_path)

#Create the connection and get the cursor with the connection object
def create_connection(host_name, user_name, user_password, db_path):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_path
        )
        cursor = connection.cursor()
        print(f"Connection to MySQL DB successful. Cursor has been created")
    except Error as e:
        raise
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
        print(f"Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        pass

def main():
    db_directory = 'C:\\Users\\HP\\Desktop'
    files_directory = 'C:\\Users\\HP\\Desktop\\Docs'
    db_name = 'app'
    my_file_extension = '.txt'
    
    query_createDatabase = f"CREATE DATABASE IF NOT EXISTS {db_name}"

    table_name = 'FILE_INFO'
    query_createTable = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
        FileID INTEGER PRIMARY KEY AUTOINCREMENT,
        FilePath VARCHAR(255) NOT NULL,
        FileSize BIGINT NOT NULL, -- Alternatively, INT if it is smaller
        FileExtension VARCHAR(10) NOT NULL
        );
    '''

    query_insert = f'INSERT INTO {table_name} (FilePath, FileSize, FileExtension) VALUES (?, ?, ?)'

    max_numb = 10
    query_getNLargestFiles = f"""
        SELECT * FROM {table_name}
        ORDER BY FilePath DESC
        LIMIT ?"""
    
    query_fileExtension = f"""
        SELECT * FROM {table_name}
        WHERE FileExtension=?
        ORDER BY FileExtension DESC"""
    
    my_db_path = get_path(db_directory, db_name)
    my_connection, my_cursor = create_connection("localhost", "root", "", my_db_path)

        #Create a database
    execute_query(my_connection, my_cursor, query_createDatabase)
    """finally:
        #Finally, close the connection if it is still open
        if my_connection:
            my_connection.close()
"""
if __name__ == '__main__':
    main()
