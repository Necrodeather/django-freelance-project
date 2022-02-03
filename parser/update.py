import sqlite3
 
class update_info(object):
    def __init__(self):
        #Редактировать путь до БД парсера
        self.parser = sqlite3.connect(r'C:\Users\Necrodeather\Desktop\django-freelance-project\parser\parsers\data_storage\database\database.db') 
        self.parser_cursor = self.parser.cursor()
        self.main = sqlite3.connect(r'C:\Users\Necrodeather\Desktop\django-freelance-project\db.sqlite3')
        self.main_cursor = self.main.cursor()

    def select_sku(self):
        self.parser_cursor.execute("SELECT sku, title, description_short FROM catalog_product")
        self.parser_results = self.parser_cursor.fetchall()
        #print(self.parser_results)

        self.main_cursor.execute("SELECT sku, title, description_short FROM catalog_product")
        self.main_results = self.main_cursor.fetchall()
        #print(self.main_results)
        self.search_sku()

    def search_sku(self):
        for main_sku in self.main_results:
            for parser_sku in self.parser_results:
                if main_sku[0] == parser_sku[0] and (main_sku[1] != parser_sku[1] or main_sku[2] != parser_sku[2]):
                    print(f'{main_sku}\n{parser_sku}')
                    self.update_sku(parser_sku[0],parser_sku[1],parser_sku[2])

    def update_sku(self, sku, title, short,):
        up = (f"Update catalog_product set title = ?, description_short = ? where sku = '{sku}'")
        data = (title, short)
        self.main_cursor.execute(up, data)
        self.main.commit()
        self.main_cursor.close()
        self.parser_cursor.close()