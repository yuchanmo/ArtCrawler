import scrapy
from ..items import ArtInfo,SubLinkInfo


class Sotheby(scrapy.Spider):
    name = 'sotheby'
    allowed_domains = ['sothebys.com']
    start_urls =[
        'https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&q='

    ]
    # def start_requests(self):
    #     urls=[
    #         'https://www.sothebys.com/en/buy/auction/2020/contemporary-art-evening-auction-3?locale=en'
    #         ,'https://www.sothebys.com/en/buy/auction/2020/impressionist-modern-art-evening-sale-2'
    #     ]

    #     for u in urls:
    #         yield scrapy.Request(url=u,callback=self.parse)


    def parse(self,response):
        try:
            r = response
            exibition_urls = r.css('div.Card-media > a::attr(href)').getall()
            yield SubLinkInfo(current_link = r.url, sub_links = exibition_urls)
            # for eu in exibition_urls:
            #     print(f'exibition link : {eu}')
            #     yield scrapy.Request(eu,callback=self.parse_exibition)

        except Exception as e:
            print(e)
        
        
    def parse_exibition(self,response):
        try:
            suburls = response.css('a.css-1um49bp::attr(href)')
            for su in suburls:
                url_text = su.get()
                next_page = response.urljoin(url_text)
                print(f'next detail page : {next_page}')
                yield scrapy.Request(next_page,callback=self.parse_detailpage)
        except Exception as e:
            pass



    def parse_detailpage(self,response):
        try:
            r = response
            exibition = r.css('.css-nqjhlo::text').get()
            lotnum = r.css('.css-hkhcik::text').get()
            artist,title = [c.strip() for c in r.css('h1.css-dzom6s::text').get().split('|')]
            estimate = r.css('.css-7qyd39-label-regular:nth-child(2)::text').get()
            soldprice = r.css('.css-1nkk3t4::text').get() + r.css('.css-65xq9y::text').get()
            description = r.css('.css-j7qwjs').xpath('string()').get()
            imgurl  = r.css('li.slide > img::attr(src)').get()
            print(f'{exibition}-{lotnum}')
            yield ArtInfo(exibition=exibition
            ,lotnum=lotnum
            ,artist=artist
            ,title=title
            ,estimate=estimate
            ,soldprice=soldprice
            ,description=description
            ,imgurl=imgurl)
        except Exception as e:
            print('Exception occured during parsing detail page')
            pass
        

        # ls = response.css('div.css-1up9enl')
        # for l in ls:
        #     a,t = l.css('h3.css-1i601rm-h3-regular::text').get().split('|')
        #     e = l.css('h4:nth-child(2)::text').get()
        #     p = l.css('span.css-8fe5tn-label-bold::text').get()
            
    