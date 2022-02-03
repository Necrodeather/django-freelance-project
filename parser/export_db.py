import sqlite3

class add_info(object):
    def __init__(self):
        #Редактировать путь до БД парсера
        self.parser = sqlite3.connect(r'C:\Users\Necrodeather\Desktop\django-freelance-project\parser\parsers\data_storage\database\database.db') 
        self.parser_cursor = self.parser.cursor()
        self.main = sqlite3.connect(r'C:\Users\Necrodeather\Desktop\django-freelance-project\db.sqlite3')
        self.main_cursor = self.main.cursor()

    def add_table(self):
        self.parser_cursor.execute('SELECT sku FROM catalog_product')
        parser_db = self.parser_cursor.fetchall()
        for db in parser_db:
            sql = self.main_cursor.execute(f"SELECT sku FROM catalog_product WHERE sku = '{db[0]}'")
            if sql.fetchone() is None:
                add_sku = self.parser_cursor.execute(f"SELECT sku, created, title, manufacturer_url, weight, lenght, hight, depth, description_short, description_main, description_specs, description_package, description_features, description_simplified FROM catalog_product WHERE sku = '{db[0]}'")
                for sku in add_sku:
                    insert_main = f"INSERT INTO catalog_product (sku, created, title, manufacturer_url, weight, length, hight, depth, description_short, description_main, description_specs, description_package, description_features, description_simplified) VALUES ({'?,' * 13}?)"
                    self.main_cursor.execute(insert_main, sku)
                    self.main.commit()

# q = add_info()
# q.add_table()