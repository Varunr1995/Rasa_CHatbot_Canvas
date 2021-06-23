import psycopg2

def connect():
    print('Connecting to Database')

    # Set up a connection to the postgres server.

    conn = psycopg2.connect(
                host="localhost",
                database="Rasa_Chatbot",
                user="postgres",
                password="V@run1995"
                )
    print("Connected!")

    return conn

def DataUpdate(*args):
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    args = list(args)
    conn = connect()
    cursor = conn.cursor()
    sql = "INSERT INTO `Rasa_Chatbot_Info` (`model`, `frame_size`, `frame_type`,`frame_orientation`,`frame_finishing`) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return

    
    
    
