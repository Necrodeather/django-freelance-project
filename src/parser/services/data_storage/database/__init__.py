import sqlite3
from core.settings import BASE_DIR

class DB:
    def __init__(self):
        self.conn = sqlite3.connect(f'{BASE_DIR}/parser.sqlite3')
        self.cursor = self.conn.cursor()

    async def check_db(self, sku):
        response = self.cursor.execute('SELECT * FROM catalog_product WHERE sku=?', (sku,))
        return(bool(len(response.fetchall())))

    async def new_item(self, args):
        if not(await self.check_db(args[0])):
            self.cursor.execute('INSERT INTO catalog_product (sku, created, title, manufacturer_url, description_short, description_main, description_specs, description_features, brand_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                args
            )
            self.conn.commit()
            print(f'SKU: {args[0]}\nSHOP: {args[8]}\n\n')
            return(self.cursor.lastrowid)
        return()

    
    async def getItem(self, sku):
        response = self.cursor.execute('SELECT sku, title, manufacturer_url, description_short, description_main, description_specs, description_features FROM catalog_product WHERE sku=?', (sku,))
        # print(response.fetchone())
        return(response.fetchone())


    async def checkItem(self, sku):
        response = self.cursor.execute('SELECT * FROM catalog_product WHERE sku=?', (sku,))
        return(bool(len(response.fetchall())))

    
    async def updateItem(self, args):
        self.cursor.execute('UPDATE catalog_product SET sku=?, title=?, manufacturer_url=?, description_short=?, description_main=?, description_specs=?, description_features=?, source_name=?, image_count=?, image_links=?, time_update=? WHERE sku=?', args)
        self.conn.commit()
        return()


    async def addPoints(self, sku, bp1='', bp2='', bp3='', bp4='', bp5='', bp6='', bp7='', bp8='', bp9='', bp10=''):
        self.cursor.execute('UPDATE catalog_product SET bp1=?, bp2=?, bp3=?, bp4=?, bp5=?, bp6=?, bp7=?, bp8=?, bp9=?, bp10=? WHERE sku=?',
        (bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, bp9, bp10, sku))
        self.conn.commit()
        return()
    


    async def newImg(self, imgLink, productId):
        self.cursor.execute('INSERT INTO catalog_image (image_file, is_main, product_id) VALUES (?, ?, ?)', (imgLink, 0, productId))
        self.conn.commit()
        return()