import scrapy
from scrapy.selector import Selector
from selenium import webdriver  
from shutil import which
from selenium.webdriver.chrome.options  import Options #to convert browser into headless...beacuse we want to give user data..no design
import json


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    start_urls=['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/']
 

    def parse(self, response):
        chrm_option=Options()
        chrm_option.add_argument('--headless')  # used fto get the driver page in background

        chromepath=which("chromedriver")
        driver = webdriver.Chrome(executable_path=chromepath,options=chrm_option)  #driver to get scrrenshot of  website

        #navigate to the url  
        driver.get("https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/") 
        

        search=driver.find_element_by_class_name("filterPanelItem___2z5Gb") 
        search.click() 
        self.html=driver.page_source
        driver.close()
        l=[]
        resp=Selector(text=self.html)
        for i in resp.xpath('//div[contains(@class,"ReactVirtualized__Table__row tableRow___3EtiS")]'):
            currancy=i.xpath(".//div[1]/div/text()").get()
            volume= i.xpath(".//div[2]/span/text()").get()

            data={"currancy" :currancy,"volume": volume}
            l.append(data)

        with open('coin_data.json', 'w') as file:
            json.dump(l, file)
        print(l)






