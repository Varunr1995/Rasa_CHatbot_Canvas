import mysql.connector

def DataUpdate(art_type_entry, size_entry, frame_entry, finishing_entry, orientation_entry):
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'V@run1995',
        database = 'rasa_chatbot'
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO chatbot_info (model, frame_size, frame_type, frame_finishing, frame_orientation) VALUES ('{0}','{1}','{2}','{3}','{4}');".format(art_type_entry, size_entry,frame_entry, finishing_entry, orientation_entry)
    mycursor.execute(sql)

    mydb.commit()