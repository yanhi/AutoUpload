#This program is for uploading file update database and add watermark automatically
#Created Date: Thu 09:46 April 19 2018 By HAIYAN
import  os
import psycopg2

str = input("Please input a directory to upload\n:")
if(os.path.exists(str)):
    print(str + "  is exit")
    fs = os.listdir(str)        #generate a list for files or path in str
    while(True):

        conn = psycopg2.connect(database="dpdb", user="dbyan", host="10.211.55.8", password="243303673",
                                port="5432")
        print("Hello! SQL User.")
        i=1
        print("Here the types of data")
        fsd = []
        for f in fs:
            if not f.startswith('.'):
                print('{0}: {1}'.format(i,f))
                i += 1
                fsd.append(f)
        choose=int(input("Chooose one Type to upload to database\n"))
        choosentype = fsd[choose-1]
        print("You have choose: " + choosentype)

        """
        add choosentype to database please!
        
        """
        
        cur=conn.cursor()
        cur.execute("SELECT * FROM cctdatas")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        typenumlist = []
        fst = os.listdir(os.path.join(str,choosentype))
        for x in fst:
            if not x.startswith('.'):
                typenumlist.append(x)


        print(typenumlist)              #每个文件夹里边的排号

        for x in typenumlist:
            paihaolist = []
            os

        uploaddir = os.path.join(str,choosentype)       ## Upload directory
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
