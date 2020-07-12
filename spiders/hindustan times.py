import scrapy
class QuotesSpider(scrapy.Spider):
   
    
    name ='technews'
    start_urls = ['https://www.hindustantimes.com/cricket/']
    

    def parse(self,response):
      for quote in response.css('#scroll-container a::text'):
          
          yield {'technews': quote.get(),
                 'date': response.css('.time-dt::text').get(),
                 
                 }
          href = response.css('https://www.hindustantimes.com/cricket/ + quote')
          yield response.follow(href,self.parse_author)

    
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        
        yield {'author':extract_with_css('.author::text').get()
               }         
                
        next_article= response.css('start_urls + #scroll-container a::text ').get()
        if next_article is not None:
            yield response.follow(next_article,callback=self.parse)
                            
                         
                         

                            
