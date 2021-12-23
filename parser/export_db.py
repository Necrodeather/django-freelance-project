import sqlite3
 
class delete_info(object):
    def __init__(self, table_main, table_update):
        self.table_update = table_update
        self.table_main = table_main
        self.conn = sqlite3.connect(f'/home/necrodeather/Desktop/Wyrestorm-django/parser/parsers/data_storage/database/database.db') 
        self.cursor = self.conn.cursor()

    def delete(self):
        self.cursor.execute(f"""
            INSERT INTO {self.table_main} (article, name, description_min, description_max, features, specifications, image_count, image_links)
            SELECT article, name, description_min, description_max, features, specifications, image_count, image_links FROM {self.table_update}
        """)
        
        self.cursor.execute(f"""DELETE FROM {self.table_update}""")
        self.conn.commit()
        print('done!')