import psycopg2

def connect():
    print("Connecting to Database")

    conn = psycopg2.connect(
                host="127.0.0.1",
                port="5432",
                database="Rasa_Chatbot",
                user="postgres",
                password="V@run1995"
                )
    
    print("Connected")
    return conn

def DataUpdate(art_type_entry, size_entry, frame_entry, finishing_entry, orientation_entry):
    conn = connect()
    cursor = conn.cursor()
    
    postgres_insert_query = "INSERT INTO rasa_chatbot_customer(model,size,type,orientation,finishing) VALUES ('{0}','{1}','{2}','{3}','{4}');".format(art_type_entry,size_entry, frame_entry, finishing_entry, orientation_entry)
    
    cursor.execute(postgres_insert_query)
    
    conn.commit()

    print("Record inserted successfully into table")

# from configparser import ConfigParser
# import psycopg2
# 
# 
# def config(filename='database.ini', section='postgresql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
# 
#     # get section, default to postgresql
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             db[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))
# 
#     return db
# 
# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()
# 
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
#         
#         # create a cursor
#         cur = conn.cursor()
# 
#         postgres_insert_query = "INSERT INTO rasa_chatbot_customer(model,size,type,orientation,finishing) VALUES ('{0}','{1}','{2}','{3}','{4}');".format(art_type_entry,size_entry, frame_entry, finishing_entry, orientation_entry)
#         cursor.execute(postgres_insert_query)
#         conn.commit()
#        
#     # close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
# 
# 
# if __name__ == '__main__':
#     connect()
