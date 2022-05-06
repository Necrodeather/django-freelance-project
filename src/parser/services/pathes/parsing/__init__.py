import asyncio
import time

from . import parser

from . import parserAthlona


loop = asyncio.new_event_loop()


dp = parser.Parsing_Item_Dispatcher()



async def main():
    try:
        category_links = await parser.Get_Category_Links().collect_category_links()
        items_links = await parser.Get_Items_Links(category_links).collect_items_links()
        print('Start wyrestrom parsing')
        await dp.run_check(items_links)
        await parserAthlona.main()
    except Exception as _ex:
        print(_ex)
