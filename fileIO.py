import os, sqlite3


def fSearch(extension, directory):
    out = []
    for file in directory:
        if extension in os.path.splitext(file)[1]:
            out.append(file)
    return out

def dbInsert(name):
    conn = sqlite3.connect('test.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_txt ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            txt_name TEXT)')
        cur.execute('INSERT INTO tbl_txt(txt_name) VALUES ("' + name + '")')
        conn.commit()
    conn.close()





if __name__ == '__main__':
    
    directory = ('information.docx', 'hello.txt', 'myImage.png', \
                 'myMovie.mpg', 'world.txt', 'data.pdf', 'myPhoto.jpg')
    
    result = fSearch('.txt', directory)
    
    for item in result:
        dbInsert(item)
        
    print(result)
