# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ImageprePipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imagesPilines(ImagesPipeline):

    #就是可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url_img'])

    #指定图片的存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        name_image = request.url.split('/')[-1]
        return name_image
    #返回给下一个即将执行的管道类
    def item_completed(self, results, item, info):
        return item