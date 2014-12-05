__author__ = 'cemkiy'
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup




class cargo_api:
    def yurtici(self, cargo_no):
        page = urllib2.urlopen("http://selfservis.yurticikargo.com/reports/SSWDocumentDetail.aspx?DocId="+str(cargo_no)).read()
        soup = BeautifulSoup(page)
        search_text = "TESLİM EDİLDİ"
        search_text = search_text.decode('utf-8')
        html_element = soup.find(text=search_text)
        if html_element == search_text:
            return True
        else:
            return False

    def aras(self, cargo_no):
        page = urllib2.urlopen('http://kargotakip.araskargo.com.tr/?code='+str(cargo_no)).read()
        soup = BeautifulSoup(page)
        search_text = "teslim edilmiştir"
        search_text = search_text.decode('utf-8')
        td = soup.find("span", {"id": "Label1"})
        td = td.prettify().decode('utf-8')
        if td.find(search_text) != -1:
            return True
        else:
            return False

    def ups(self, cargo_no):
        page = urllib2.urlopen('http://www.ups.com.tr/WaybillSorgu.aspx?waybill='+str(cargo_no)).read()
        soup = BeautifulSoup(page)
        search_text = "Paketiniz teslim edilmiştir."
        search_text = search_text.decode('utf-8')
        html_element = soup.find(text=search_text)
        if html_element == search_text:
            return True
        else:
            return False