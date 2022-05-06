import sqlite3
from core.settings import BASE_DIR

class add_info:
    def __init__(self):
        self.parser = sqlite3.connect(BASE_DIR / 'parser.sqlite3') 
        self.parser_cursor = self.parser.cursor()
        self.main = sqlite3.connect(BASE_DIR / 'info.sqlite3')
        self.main_cursor = self.main.cursor()

    def add_table(self):
        self.parser_cursor.execute('SELECT sku FROM catalog_product')
        parser_db = self.parser_cursor.fetchall()
        for db in parser_db:
            sql = self.main_cursor.execute(f"SELECT sku FROM info_product WHERE sku = '{db[0]}'")
            if sql.fetchone() is None:
                add_sku = self.parser_cursor.execute(f"SELECT * FROM catalog_product WHERE sku = '{db[0]}'")
                for sku in add_sku:
                    insert_main = f"INSERT INTO info_product (id, sku, created, title, manufacturer_url, weight, lenght, hight, depth, description_short, description_main, description_specs, description_package, description_features, description_simplified, time_update, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, bp9, bp10, brand_id) VALUES ({'?,' * 26}?)"
                    self.main_cursor.execute(insert_main, sku)
                    self.main.commit()

    def add_images(self):
        self.parser_cursor.execute('SELECT image_file FROM catalog_image')
        parser_db = self.parser_cursor.fetchall()
        for db in parser_db:
            sql = self.main_cursor.execute(f"SELECT image_file FROM info_image WHERE image_file = '{db[0]}'")
            if sql.fetchone() is None:
                add_image = self.parser_cursor.execute(f"SELECT * FROM catalog_image WHERE image_file = '{db[0]}'")
                for image in add_image:
                    insert_main = f"INSERT INTO info_image (id, image_file, is_main, product_id) VALUES ({'?,' * 3}?)"
                    self.main_cursor.execute(insert_main, image)
                    self.main.commit()