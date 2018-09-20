import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):
    """
    网页解析器：从网页中提取有价值的数据
    """
    @staticmethod
    def _get_new_urls(page_url, soup):
        """从soup中获取新的url列表返回"""
        new_urls = set()
        # 根据正则表达式获取新的url
        # /item/python
        # links = soup.find_all('a',href=re.compile("/item/"))
        links = soup.find_all('a', href=re.compile("/item/(^\")*"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        """从soup中获取所需数据返回"""

        # url
        res_data = {'url': page_url}

        # lemmaWgt-lemmaTitle-title
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # lemma-summary
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        """从html_cont中解析数据：新的url列表和所需数据"""
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
