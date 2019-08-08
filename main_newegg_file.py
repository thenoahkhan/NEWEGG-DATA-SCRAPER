from urllib.request import urlopen as UR
from bs4 import BeautifulSoup as soup
import re 


URL_SIMP = 'https://www.newegg.com/Xbox-One-Systems/SubCategory/ID-3216'
URL_CLIENT = UR(URL_SIMP)
PAGE = URL_CLIENT.read()
URL_CLIENT.close()
PAGE_SOUP = soup(PAGE,"html.parser")
PAGE_CONTENT = PAGE_SOUP.findAll("div",{"class":"item-container"})

filename = "newegg.csv"
f = open(filename,"w")
headers = ("PRICE, SHIP, NAME\n")
f.write(headers)

for CONTENT in PAGE_CONTENT:

    PRICE_DATA = CONTENT.findAll("li",{"class":"price-current"})
    PRICE = PRICE_DATA[0].text
    PRICE_SIMP = re.sub("[^\d\.]", "", PRICE)
    

    SHIP_CONTENT = CONTENT.findAll("li",{"class":"price-ship"})
    SHIP = SHIP_CONTENT[0].text.strip()

    NAME = CONTENT.img["title"]

    print("Price: " + "$" +PRICE_SIMP)
    print("Shipping Cost: "+SHIP)
    print("Name of Product: "+NAME)
    print("\n")

    f.write("$" + PRICE_SIMP + "," + SHIP + "," + NAME.replace(",","||") + "\n")
    
f.close()
