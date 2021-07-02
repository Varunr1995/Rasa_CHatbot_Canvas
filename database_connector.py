import psycopg2

def DataUpdate(art_type_entry, size_entry, frame_entry, finishing_entry, orientation_entry):
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    db = psycopg2.connect(
                host="localhost",
                database="Rasa_Chatbot",
                user="postgres",
                password="V@run1995"
                )

    mycursor = db.connect()
    
    postgres_insert_query = """INSERT INTO rasainfo(model,size,type,orientation,finishing) VALUES (%s,%s,%s,%s,%s);""".format(art_type_entry,size_entry, frame_entry, finishing_entry, orientation_entry)
    
    mycursor.execute(postgres_insert_query)
    
    db.commit()

    print("Record inserted successfully into table")
    