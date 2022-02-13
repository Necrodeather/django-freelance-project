import sqlite3
from freelance_project.settings import BASE_DIR

class update_info:
    def __init__(self):
        self.parser = sqlite3.connect(BASE_DIR / 'parser/parsers/data_storage/database/database.db') 
        self.parser_cursor = self.parser.cursor()
        self.main = sqlite3.connect(BASE_DIR / 'db.sqlite3')
        self.main_cursor = self.main.cursor()

    def select_sku(self):
        self.parser_cursor.execute("SELECT * FROM catalog_product")
        self.parser_results = self.parser_cursor.fetchall()

        self.main_cursor.execute("SELECT * FROM catalog_product")
        self.main_results = self.main_cursor.fetchall()
        self.search_sku()

    def search_sku(self):
        for main_sku in self.main_results:
            for parser_sku in self.parser_results:
                if main_sku[1] == parser_sku[1] and (main_sku[2:] != parser_sku[2:]):
                    self.update_sku(parser_sku[0],parser_sku[1],parser_sku[2:])

    def update_sku(self, id, sku, agrs):
        up = (f"Update catalog_product set id=? created=?, title=?, manufacturer_url=?, weight=?, length=?, hight=?, depth=?, description_short=?, description_main=?, description_specs=?, description_package=?, description_features=?, description_simplified=?, time_update=?, bp1=?, bp2=?, bp3=?, bp4=?, bp5=?, bp6=?, bp7=?, bp8=?, bp9=?, bp10=?, brand_id=? where sku = ?")
        data = id+agrs+sku
        self.main_cursor.execute(up, data)
        self.main.commit()
