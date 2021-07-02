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

    print("Record inserted successfully into table")
    
