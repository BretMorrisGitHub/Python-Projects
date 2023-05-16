import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_file TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    length = len(fileList)
    i = 0
    item = fileList[i]
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (file,))
            conn.commit()
            i = i + 1
            print(file)
        
            
conn.close()

