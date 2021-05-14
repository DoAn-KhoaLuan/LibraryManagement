import scrapy

from library import app, socketio
from library.crawlerscrapy.crawlerscrapy.spiders.book_tiki import BookTikiSpider

if __name__ == "__main__":
    spi = BookTikiSpider(scrapy.Spider)
    spi.parse(None)
    app.debug = True
    # app.run(debug=True, host='0.0.0.0')
    socketio.run(app, "localhost", 5000)
