import requests
import asyncio
from bs4 import BeautifulSoup
import pytz
import datetime as dt


import time
from parser.services.loader import db, cfg
import re


loop = asyncio.get_event_loop()


class Get_Category_Links:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
        self.main_url = 'https://www.wyrestorm.com/av-control/'

    #Получаем основную html страницу
    async def __get_main_html_page(self):
        response = requests.get(url=self.main_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        return(soup)

    #Получаем блок с категориями
    async def __get_category_block(self):
        html_page = await self.__get_main_html_page()
        category_block = html_page.find('div', class_='row row-large')
        return(category_block)

    #Получаем ссылки на категории
    async def collect_category_links(self):
        links_list = []
        category_block = await self.__get_category_block()
        category_links = category_block.find_all('a', class_='ux-menu-link__link flex')

        for i in category_links:
            link = {
                'category_name': i.find('span').text.strip(),
                'link': i.get('href')
            }
            links_list.append(link)

        return(links_list)


class Get_Items_Links:
    def __init__(self, link: Get_Category_Links):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
        self.links = link

    #Получаем HTML страницу по переданной ссылке
    async def __html_page_retrieval(self, link):
        response = requests.get(url=link, headers=self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        return(soup) 

    #Получаем блок с картачками товаров
    async def __get_items_block(self, link):
        html_page = await self.__html_page_retrieval(link)
        items_block = html_page.find('div', class_='content-area')
        return(items_block)

    #Получаем все карточки из блока с товарами
    async def __collect_items_link(self, items_block):
        try:
            items = items_block.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
            return(items)
        except Exception as ex:
            pass


    #Получаем все ссылки на товары из категорий
    async def collect_items_links(self):
        products_list = {}

        for i in self.links:
            try:

                products_list[i['category_name']] = []
                items_block = await self.__get_items_block(i['link'])
                cards_in_items_block = await self.__collect_items_link(items_block)

                for link in cards_in_items_block:
                    link = link.get('href')
                    products_list[i['category_name']].append(link)
            except Exception as _ex:
                continue

        return(products_list)





class Parsing_Item_Dispatcher:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}




    #Получаем всю страницу товара
    async def __get_item_html_page(self, url):
        response = requests.get(url=url, headers=self.headers)
        self.html_page = BeautifulSoup(response.text, 'lxml')
        return(self.html_page)


    async def collect_all_item_info(self):
        sku = await self.get_article()
        created = await self.get_time()
        title = await self.get_name_item()
        manufacturer_url = self.item_link
        description_short = await self.get_min_description()
        description_main = await self.get_max_description()
        description_specs = await self.get_specifications()
        description_features = await self.get_features()
        self.image_links = await self.collect_image_links()
        return(
            sku, created, title, manufacturer_url, description_short, description_main, description_specs, description_features
        )




    async def __new_item(self):
        args = await self.collect_all_item_info()
        if not(await db.checkItem(args[0])):
            resp = await db.new_item(args+(2,))
            for img in self.image_links:
                await db.newImg(img, resp)
            return()
        oldItemInfo = await db.getItem(args[0])
        old_args = (args[0], args[2], args[3], args[4], args[5], args[6], args[7])

        if old_args != oldItemInfo:
            await db.updateItem(old_args+(args[1], args[0]))
            return()


    async def __check_article_database(self, article):
        # if not(await db.check_article(article)):
        await self.__new_item()
        return()
        # else:
        #     item_db = await db.get_item(article)
        #     args = await self.collect_all_item_info()
        #     now = dt.datetime.now(pytz.utc)
        #     time = now.astimezone(pytz.timezone(await cfg.time_zone())).strftime('%Y-%m-%d %H:%M:%S')
        #     if item_db != args:
        #         print('Есть изменения')
        #         await db.delete_item(article)
        #         await db.new_item(args)
        #         await db.new_item_update(args+(time,))
        #     return()

    


    async def run_check(self, items_links):
        for list in items_links.values():
            for link in list:
                self.item_link = link
                await self.__get_item_html_page(link)
                article = await self.get_article()
                if not(article):
                    continue
                await self.__check_article_database(article)
        return()

    
    async def get_time(self):
        now = dt.datetime.now(pytz.utc)
        time = now.astimezone(pytz.timezone(cfg)).strftime('%Y-%m-%d %H:%M:%S')
        return(time)


    async def get_count_image(self):
        try:
            images = self.html_page.find_all('img', class_='attachment-woocommerce_thumbnail')
            image_count = len(images)
            return(image_count)
        except Exception as _ex:
            return('null')

    async def collect_image_links(self):
        try:
            list = []
            str_links = ''
            images = self.html_page.find_all('img', class_='skip-lazy')
            for links in images:
                try:
                    link = links.get('srcset').split(', ')[1]
                    link = link.split(' ')[0]
                    str_links += f'{link}\n\n'
                    list.append(link)
                    # list.append(link[-1])
                except Exception as _ex:
                    print(_ex)

            return(list)
        except Exception as _ex:
            return('null')


    async def get_name_item(self):
        try:
            name = self.html_page.find('h1', class_='product-title product_title entry-title').text.strip()
            return(name)
        except Exception as _ex:
            return('null')


    async def get_min_description(self):
        try:
            description = self.html_page.find('div', class_='product-short-description').find_all('p')[0].text.strip()
            return(description)
        except Exception as _ex:
            return('null')


    async def get_max_description(self):
        try:
            description = ''
            description_block = self.html_page.find('div', class_='sticky_content blue').find('div', class_='text-inner text-center')
            items_description_block = description_block.find_all('div', class_='row')

            for i in items_description_block:
                description += i.find('div', class_='text').text.strip()

            return(description)
        except Exception as _ex:
            return('null')


    async def delStyles(self, html):
        # styles = [
        #     'class', 'id', 'style', 'width', 'border', 'cellpadding', 'cellspacing', 'colspan',
        #     'data-title', 'data-searching-settings', 'data-pagination-length', 'data-override',
        #     'data-merged', 'data-lang', 'data-features', 'data-auto-index', 'data-percent-format',
        #     'data-responsive-mode', 'data-search-value', 'data-time-format'
        # ]
        styles = ['table', 'tr', 'td', 'th', 'div', 'tbody', 'thead', 'span']
        for style in styles:
            html = re.sub(r'(?<=<'+style+r')(.|\n)*?(?=>)', '', str(html))
            # html = re.sub(r'\s*'+style+r'\s*=\s*"[^"]*"(?=[^<]*>)', '', str(html))

        html = re.sub(r'<style>(.|\n)*?<\/style>', '', str(html))
        return(html)

    async def get_specifications(self):
        try:
            feature = ''
            features_block = self.html_page.find('div', id='tab_specifications').find('table')
            result = await self.delStyles(features_block)
            return(result)
        except Exception as _ex:
            return('null')

            
    async def get_features(self):
        try:
            specifications = ''
            specifications_block = self.html_page.find('div', class_='col small-12 large-12')
            specification = specifications_block.find_all('li')

            for i in specification:
                specifications += i.text.strip()
                # specification_text = i.find_all('td')
                # for text in specification_text:
                #     specifications += text.text.strip() + '\n'
            return(specifications)
        except Exception as _ex:
            print(_ex)
            return('null')

    async def get_article(self):
        try:
            article = self.html_page.find('div', class_='product-info summary col-fit col entry-summary product-summary text-left')
            stage=0
            for i in article:
                try:
                    stage+=1
                    if stage==4:
                        str_article = i.split(':')[1].strip()
                        return(str_article)
                except Exception as _ex:
                    pass
                    # print(_ex)
                    # print(stage)
                    # print(article)
                    # print(str_article)
        except:
            pass


    


    



    