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
    
    sql = 'INSERT INTO Rasa_Chatbot_Info (model,frame_size,frame_type,frame_orientation,frame_finishing) VALUES ("{0}","{1}","{2}","{3}","{4}");'.format(art_type_entry, size_entry, frame_entry, finishing_entry, orientation_entry)
    
    mycursor.execute(sql)

    
