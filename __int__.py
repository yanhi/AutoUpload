#This program is for uploading file update database and add blueprint automatically
#Created Date: Thu 09:46 April 19 2018 By HAIYAN
import  os
import psycopg2




str = input("Please input a directory to upload\n:")
if(os.path.exists(str)):
    print(str + "  is exit")
    fs = os.listdir(str)        #generate a list for files or path in str
    while(True):
        conn = psycopg2.connect(database="testdb", user="testdatabase", host="127.0.0.1", password="243303673",
                                port="5432")
        print("Hello! SQL User.")
        i=1

        print("Here the types of data")
        for f in fs:
            print('{0}: {1}'.format(i,f))
            i += 1
        choose=int(input("Chooose one Type to upload to database\n"))
        choosedtype = fs[choose-1]
        print("You have choose: " + choosedtype)

        cur=conn.cursor()
        cur.execute("SELECT * FROM cctdatas")
        rows = cur.fetchall()
        for row in rows:
            print(row)


        uploaddir = os.path.join(str,choosedtype)       ## Upload directory
        if os.path.exists(uploaddir):
            print(uploaddir)
        else:
            raise NameError("ERROR PATH")

        conn.close()
        print("ByeBye SQL")

        if input("Press Enter key to continue"):
            continue
else:
    print(str + "no exit!")
    exit(1)
