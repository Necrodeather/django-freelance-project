import requests
from bs4 import BeautifulSoup
import asyncio

import pytz
import datetime as dt
from parser.services.loader import db, cfg

import time
import re


loop = asyncio.new_event_loop()

class Parse:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}


    def getSku(self, html):
        try:
            sku = html.find('div', class_='product-short-description').find('h2')
            if not(sku):
                return()
            return(sku.text.strip())
        except:
            return()


    def getTitle(self, html):
        try:
            title = html.find('h1', class_='product-title product_title entry-title')
            return(title.text.strip())
        except:
            print('Ошибка в получении названия')


    def getPoints(self, html):
        try:
            block_points = html.find('div', class_='product-short-description').find_all('li')
            points = ()
            for point in block_points:
                points += (point.text.strip(),)
            return(points)
        except:
            print('Ошибка в получении поинтов')


    def getLinkImages(self, html):
        # try:
        productId = self.site_response.headers['Set-Cookie'].split('woocommerce_recently_viewed=')[1].split(';')[0]
        ajaxResponse = requests.post(
            url='https://atlona.com/wp-admin/admin-ajax.php',
            headers=self.headers,
            data={
                'action': 'variable_action',
                'product_id': productId,
                'variation_id': '',
                'nav_slides': ''
            }
        )
        imagesBlock = BeautifulSoup(ajaxResponse.text, 'lxml')
        images = imagesBlock.find_all('a', class_='woocommerce-main-image')
        strImagesLinks = ''
        list = []
        for image in images:
            imgLink = image.find('img').get('src')
            strImagesLinks+=f'{imgLink}\n'
            list.append(imgLink)
        return(len(images), list)
        # except:
        #     print('Ошибка в получении ссылок на картинки')


    def checkDetails(self, html):
        result = html.find('li', class_='details_tab')
        return(result)


    def getOverviewDesc(self, html):
        try:
            block = html.find('div', id='tab-description').find_all('div', class_='col-inner')
            desc = f'{block[1].text.strip()}\n{block[2].text.strip()}'
            return(desc)
        except:
            try:
                return(block[1].text.strip())
            except:
                return('None')

    
    def getOverviewFeatures(self, html):
        try:
            block = html.find('div', id='tab-description').find_all('div', class_='row')
            for element in block:
                element_title = element.find('span', class_='section-title-main')
                if not(element_title):
                    continue
                

                if element_title.text.lower() == 'features':
                    return(element.text.strip())
            return('None')
        except:
            return('Ошибка в получени овервью фьючерс')



    def getDetailsDescFeatures(self, html):
        block = html.find('div', id='tab-details')
        text=block.text.strip().split('Features')
        return(text[0], text[1])

    def delStyles(self, html):
        # styles = [
        #     'class', 'id', 'style', 'width', 'border', 'cellpadding', 'cellspacing', 'colspan',
        #     'data-title', 'data-searching-settings', 'data-pagination-length', 'data-override',
        #     'data-merged', 'data-lang', 'data-features', 'data-auto-index', 'data-percent-format',
        #     'data-responsive-mode', 'data-search-value', 'data-time-format'
        # ]
        styles = ['table', 'tr', 'td', 'th', 'div', 'tbody', 'thead', 'span', 'section']
        for style in styles:
            html = re.sub(r'(?<=<'+style+r')(.|\n)*?(?=>)', '', str(html))
            # html = re.sub(r'\s*'+style+r'\s*=\s*"[^"]*"(?=[^<]*>)', '', str(html))

        html = re.sub(r'<style>(.|\n)*?<\/style>', '', str(html))
        return(html)



    def getDescription(self, html):
        if not(self.checkDetails(html)):
            description_main = self.getOverviewDesc(html)
            features = self.getOverviewFeatures(html)
            return(description_main, features.replace('Features', ''))

        descDetails = self.getDetailsDescFeatures(html)
        description_main = descDetails[0]
        features = descDetails[1]
        return(description_main, features.replace('Features', ''))
        

    def getSpecification(self, html):
        result = html.find('li', class_='specifications_tab')
        if not(result):
            return('None')
        result = html.find('div', id='tab-specifications')
        tables = self.delStyles(result)
        return(tables)

        # result = html.find('li', class_='specifications_tab')
        # if not(result):
        #     return('None')
        

        # str_table = ''

        # tables = html.find_all('div', class_='supsystic-tables-wrap')
        # for table in tables:
        #     str_table += table.text + '\n'

        # return(str_table)


    async def get_time(self):
        now = dt.datetime.now(pytz.utc)
        time = now.astimezone(pytz.timezone(cfg)).strftime('%Y-%m-%d %H:%M:%S')
        return(time)


    # async def checks(self, one, two):
    #     print(one[0]==two[0])
    #     print(one[1]==two[1])
    #     print(one[2]==two[2])
    #     print(one[3]==two[3])
    #     print(one[4]==two[4])
    #     print(one[5].encode('utf')==two[5].encode('utf-8'))
    #     print(one[6]==two[6])
    #     print(one[7]==two[7])
    #     print(one[8]==two[8])
    #     print(one[9]==two[9])



    async def parse(self, url):
        self.site_response = requests.get(url=url, headers=self.headers)
        html = BeautifulSoup(self.site_response.text, 'lxml')
        sku = self.getSku(html)
        created = await self.get_time()
        if not(sku):
            return()
        title = self.getTitle(html)
        points = self.getPoints(html)
        desc = self.getDescription(html)
        specs = self.getSpecification(html)
        images = self.getLinkImages(html)
        args = (sku, created, title, url, 'null', desc[0], specs, desc[1], 1)
        if not(await db.checkItem(sku)):
            resp = await db.new_item(args)
            for img in images[1]:
                await db.newImg(img, resp)
            await db.addPoints(sku, *points)
            return()
        oldItemInfo = await db.getItem(sku)
        args = (sku, title, url, 'null', desc[0], specs, desc[1])
        # await self.checks(args, oldItemInfo)
        if args != oldItemInfo:
            await db.updateItem(args+(created, sku))
            await db.addPoints(sku, *points)
            return()







        # print(
        #     f'LINK: {url}\
        #     \nSKU: {sku}\
        #     \nTITLE: {title}\
        #     \n\nPOINTS: {points}\
        #     \n\nDESC: {desc[0]}\
        #     \n\nFEATURES: {desc[1]}\
        #     \n\nCOUNT IMAGES: {images[0]}\
        #     \nIMAGES: {images[1]}\
        #     \nSPECS: {specs}\n\n\n'
        # )
        
















headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}


async def get_count_pages(url: str, headers):
    response = requests.get(url=url, headers=headers)
    html_page = BeautifulSoup(response.text, 'lxml')
    block = html_page.find('nav', class_='wpgb-pagination-facet').find_all('li')
    return(len(block))


async def get_page(number):
    prs = Parse()

    url = f'https://atlona.com/product-finder/?_pagination={number}'
    response = requests.get(url=url, headers=headers)
    page=BeautifulSoup(response.text, 'lxml')

    items_links = []

    cards = page.find('div', class_='wpgb-masonry').find_all('article')


    for card in cards:
        link = card.find('div', class_='wpgb-card-body').find('a').get('href')
        await prs.parse(link)

    return()


async def main():
    url = 'https://atlona.com/product-finder/'


    count_pages = await get_count_pages(url, headers)

    for num in range(1, count_pages):
        await get_page(num)

    print('Atlona finish parsing')
    return()