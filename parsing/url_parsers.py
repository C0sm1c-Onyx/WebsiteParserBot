import aiohttp
from bs4 import BeautifulSoup
from lxml import etree

from parsing.utils import clean_number


async def website_parsing_by_xpath(url, xpath):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

            soup = BeautifulSoup(html, 'html.parser')
            dom = etree.HTML(str(soup))
            parsed_data = dom.xpath(xpath)

            if parsed_data:
                return clean_number(parsed_data[0].text)
