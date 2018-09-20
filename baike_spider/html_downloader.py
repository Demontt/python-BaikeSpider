import urllib.request


class HtmlDownloader(object):

    @staticmethod
    def download(url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
