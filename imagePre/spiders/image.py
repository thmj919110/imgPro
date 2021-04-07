import scrapy

from imagePre.items import ImagepreItem
class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['www.sdsaasd.cpm']
    start_urls = ['https://sc.chinaz.com/tupian/shanshuitupian.html']
    url = 'https://sc.chinaz.com/tupian/shanshuitupian_%d.html'
    page_num = 2
    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            url_img = 'http:'+div.xpath('./div/a/img/@src2').extract_first()
            item = ImagepreItem()
            item['url_img'] = url_img
            yield item
        if self.page_num<=5:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)

