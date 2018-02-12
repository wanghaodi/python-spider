import scrapy


from test1.items import Test1Item


class DmozSpider(scrapy.Spider):
    name = "dmoz"  # 爬虫名
    allowed_domains = ["baidu.com"]  # allow_domains是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页。
    start_urls = [
        "http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8",
    ]  # 要爬取的网站

    # parse解析的方法，
    # 调用的时候传入从每一个URL传回的Response对象作为唯一参数，
    # 负责解析并匹配抓取的数据(解析为item)，跟踪更多的URL。
    def parse(self, response):
        for line in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            item = Test1Item()
            item['title'] = line.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()').extract()
            item['author'] = line.xpath(
            './/div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
            item['reply'] = line.xpath('.//div[contains(@class,"col2_left j_threadlist_li_left")]/span/text()').extract()
            yield item