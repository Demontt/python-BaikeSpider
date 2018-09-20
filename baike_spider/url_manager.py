class UrlManager(object):
    """
    URL管理器：负责管理待抓取的URL和已抓取的URL，防止重复抓取和循环抓取
    """
    def __init__(self):
        """
        待爬取的new_urls,和爬取过的old_urls
        set()：创建不重复的元素集
        """
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """添加一个新的url，要添加的url不能是重复的"""
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """添加多个url"""
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """判断当前URL管理器中是否还有待爬取的URL,返回一个bool值"""
        return len(self.new_urls) != 0

    def get_new_url(self):
        """
        获取一个新的待爬取的url
        new_urls里面pop()
        old_urls里面add()
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
