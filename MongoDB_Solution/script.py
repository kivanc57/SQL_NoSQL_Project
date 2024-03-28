import os
import pymongo

# Merge the given directory with the given file path
def get_path(directory, file_path):
    return os.path.join(directory, file_path)

# Connect to MongoDB Atlas
def create_connection(db_name, connection_string):
    try:
        client = pymongo.MongoClient(connection_string)
        print("Connection to MongoDB successful")
        return client[db_name], client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection to MongoDB failed: {e}")
        return None, None
    
# Execute any kind of query
def execute_query(collection, query):
    try:
        collection.insert_one(query)
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")

# Walk throughout the directory, get the required info and insert into collection
def insert_files(collection, directory):
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            file_path = get_path(folder, file)
            file_size = os.path.getsize(file_path)
            file_extension = os.path.splitext(file_path)[1]

            execute_query(collection, {"FilePath": file_path, "FileSize": file_size, "FileExtension": file_extension})

    print("Files inserted successfully")

def main():
    my_connection_string = "mongodb://localhost:27017/"
    files_directory = 'C:\\Users\\HP\\Desktop\\Docs'
    my_db_name = 'app'
    my_file_extension = '.txt'
    collection_name = 'FILE_INFO'
    max_numb = 10

    query_create_index = [("FilePath", pymongo.DESCENDING)]
    query_file_extension = {"FileExtension": my_file_extension}

    my_connection, _ = create_connection(my_db_name)

    try:
        # Get the collection object from the connection
        collection = my_connection[collection_name]
        
        # Insert the files in the given directory and get the inserted rows
        insert_files(collection, files_directory) 
        
        # Create index for FilePath for efficient sorting
        collection.create_index(query_create_index)
        
        # Get n Largest Files
        largest_files = collection.find().sort("FilePath", pymongo.DESCENDING).limit(max_numb)
        for file in largest_files:
            print(file)
        
        # Print files with .txt extension
        txt_files = collection.find(query_file_extension).sort("FileExtension", pymongo.DESCENDING)
        for file in txt_files:
            print(file)

    finally:
        # Finally, close the connection if it is still open
        if my_connection:
            my_connection.close()

if __name__ == "__main__":
    main()
