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
    while i < length:
        if item.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(ID, col_file) VALUES (?,?)", (i , item))
            conn.commit()
            i = i + 1
            print(item)
        else:
            i = i + 1
        #This print was for problem solving purposes
            print(i)
conn.close()

