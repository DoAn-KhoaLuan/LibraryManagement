import urllib
import json
import scrapy


class DemoScrapyItem(scrapy.Item):
    product_name = scrapy.Field()
    price_sale =scrapy.Field()
    price = scrapy.Field()
    rate_average = scrapy.Field()


class BookItem(scrapy.Item):
    book_name = scrapy.Field()
    page_number = scrapy.Field()
    retail_price = scrapy.Field()
    discount = scrapy.Field()
    ranking = scrapy.Field()
    rate_star = scrapy.Field()
    rate_count = scrapy.Field()

class BookTikiSpider(scrapy.Spider):
    name = 'book_tiki'
    allowed_domains = ['www.tiki.vn']
    start_urls = ['https://tiki.vn/api/v2/products/8120020'] # URL của response dưới hàm Parse()

    # def parse(self, response):
    #     # Request tới từng sản phẩm có trong danh sách các Macbook dựa vào href
    #     for item_url in response.css("li.item > a ::attr(href)").extract():
    #         yield scrapy.Request(response.urljoin(item_url),
    #                              callback=self.parse_macbook)  # Nếu có sản phẩm thì sẽ gọi tới function parse_macbook
    #
    #     # nếu có sản phẩm kế tiếp thì tiếp tục crawl
    #     next_page = response.css("li.next > a ::attr(href)").extract_first()
    #     if next_page:
    #         yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_macbook(self, response):
        item = DemoScrapyItem()

        item['product_name'] = response.css(
            'ul.breadcrumb + h1 ::text').extract_first()  # Tên macbook

        print("item ne: ", item)
        out_of_stock = response.css('span.productstatus ::text').extract_first()  # Tình trạng còn hàng hay không
        if out_of_stock:
            item['price'] = response.css(
                'strong.pricesell ::text').extract_first()
        else:
            item['price'] = response.css(
                'aside.price_sale > div.area_price.notapply > strong ::text').extract_first()

        discount_online = response.css(
            'div.box-online.notapply').extract_first()  # Check nếu có giảm giá khi mua online hay không
        if discount_online:
            item['price_sale'] = response.css(
                'aside.price_sale > div.box-online.notapply > div > strong ::text').extract_first()
        else:
            item['price_sale'] = response.css(
                'span.hisprice ::text').extract_first()

        item['rate_average'] = response.css('div.toprt > div.crt > div::attr(data-gpa)').extract_first()

        yield item

    def parse(self, response):
        book = BookItem()

        get_books_req =  urllib.request.Request("https://tiki.vn/api/v2/products?q=dung+an+nhan", None, {'Content-Type': 'application/json'})
        fs = urllib.request.urlopen(get_books_req)
        response = fs.read()

        fs.close()
        books_json_res = json.loads(response)
        book_id = books_json_res["data"][1]["id"]
        print("bood_id: ", book_id)


        # book['book_name'] = response.css(".container .flex.flex-auto .attM6y span::text").extract_first()
        # book_box = response.css("body")[0].css("main .Container-itwfbd-0 .inner a.product-item")[1]
        # detail_book_url = "https://tiki.vn" + book_box.css("a::attr(href)").get()
        req = urllib.request.Request("https://tiki.vn/api/v2/products/8120020", None, {'Content-Type': 'application/json'})
        f = urllib.request.urlopen(req)

        response = f.read()

        f.close()
        book_json_res = json.loads(response)
        book["book_name"] = book_json_res["name"]
        book["retail_price"] = book_json_res["price"]
        book["rate_star"] = book_json_res["rating_average"]
        book["rate_count"] = book_json_res["review_count"]

        print("response: ",book_json_res["id"])

        yield book
