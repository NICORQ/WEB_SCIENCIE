import sqlite3

def insertValues( id , title , href , name_site ):
    con = sqlite3.connect('/home/bencenodev/entregable/tags_porn_xvideos')
    cursor = con.cursor()
    sql = '''INSERT INTO 'tags_xvideos'( 'ID' , 'TITLE', 'HREF', 'NAME_SITE') VALUES(?,?,?,?)'''

    cursor.execute(sql, (id, title, href , name_site) )
    con.commit()
    cursor.close()
