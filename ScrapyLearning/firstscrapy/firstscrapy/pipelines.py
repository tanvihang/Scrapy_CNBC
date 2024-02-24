# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class FirstscrapyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            database = 'scrapyquotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes""")
        self.curr.execute("""
                CREATE TABLE quotes(
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          quote VARCHAR(255),
                          author VARCHAR(255),
                          authorUrl VARCHAR(255),
                          tags VARCHAR(255)
                )
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""
            INSERT INTO quotes(quote, author, authorUrl, tags) VALUES(%s,%s,%s,%s)
        """,(
            item['quote'],
            item['author'],
            item['authorUrl'],
            item['tags'][0]
        ))
        self.conn.commit()