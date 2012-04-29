from BeautifulSoup import BeautifulSoup
import mechanize 
import urllib

def collect(unit_type, unit_nr): 
    br = mechanize.Browser()
    br.open("http://amazon.com") 
    br.select_form(name="site-search") 
    br['field-keywords'] = unit_type + " " + unit_nr
    response = br.submit()
    soup = BeautifulSoup(response.read())
    return soup.find("div", {"id" : "result_0"})
