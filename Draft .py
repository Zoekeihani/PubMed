import requests
import xml.etree.ElementTree as ET
import re

class PubMed:
    def __init__(self):
        self.api_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.qk = ""
        self.webenv = ""
        self.report_type = "xml"
# request to get url
    def test_query(self):
        r = requests.get(self.api_base_url)
        print("test_query Result: " + r.text)
# find DB names
    def einfo(self):
        r = requests.get(self.api_base_url + "einfo.fcgi?db=pubmed")
        print("einfo Result: "+ r.text)
# find UID
    def esearch(self, keyword):
        r = requests.get(self.api_base_url + "esearch.fcgi?db=pubmed&term="+keyword+"&usehistory=y")
        #print("esearch Result: " + r.text)

        for line in r.text.splitlines():
            qk_match = re.search("<QueryKey>(.+?)</QueryKey>", line)
            webenv_match = re.search("<WebEnv>(.+?)</WebEnv>", line)

            if qk_match:
                self.qk = qk_match.group(1)

            if webenv_match:
                self.webenv = webenv_match.group(1)

        print(f"query_key: {self.qk}\nwebenv: {self.webenv}")

    #def esummary(self):
        #r = requests.get(self.api_base_url + f"esummary.fcgi?db=pubmed&query_key={self.qk}&WebEnv={self.webenv}")
        #print(f'esummary: "{r.text}"')
        #return r.text


    def efetch(self, retmax=20):
        url = (self.api_base_url +
               f"efetch.fcgi?db=pubmed&query_key={self.qk}&WebEnv={self.webenv}&rettype={self.report_type}&retmode=xml&retmax={retmax}")
        r = requests.get(url)
        return r.text


class PubMedSearch:
    def __init__(self, xml_text):
        self.root = ET.fromstring(xml_text)
        #self.all_docs = self.root.findall(".//DocSum")

    #def get_titles(self):
        #titles = []
        #for docsum in self.all_docs:
            #for item in docsum.findall("Item"):
                #if item.attrib.get("Name") == "Title":
                    #titles.append(item.text)
        #return titles



    def get_articles(self):
        articles = []
        for article in self.root.findall(".//PubmedArticle"):
            record = {}
            # Title
            title_elem = article.find(".//Article/ArticleTitle")
            if title_elem is not None:
                title_elem = article.find(".//VernacularTitle")
            record["Title"] = title_elem.text if title_elem is not None else "[NO TITLE]"
            # Keywords
            kwlist = article.findall(".//KeywordList/Keyword")
            record["Keywords"] = [kw.text for kw in kwlist if kw.text] or ["None"]
            # MeSH terms
            meshlist = article.findall(".//MeshHeadingList/MeshHeading/DescriptorName")
            record["MeSH"] = [m.text for m in meshlist if m.text] or ["None"]
            articles.append(record)
        return articles






if __name__ == "__main__":
    pubmed = PubMed()
    # pubmed.test_query()
    # pubmed.einfo()
    # pubmed.esearch()
    #pubmed.esearch("fbn1")
    #pubmed.esummary()
    #xml_text = pubmed.esummary()
    #summary = PubMedSearch(xml_text)
    #titles = summary.get_titles()

    #print("Article Titles:")
    #for t in titles:
        #print("-", t)


    pubmed.esearch("fbn1")
    xml_text = pubmed.efetch()

    fetch = PubMedSearch(xml_text)
    articles = fetch.get_articles()

    for art in articles:
        print("Title:", art["Title"])
        print("Keywords:", ", ".join(art["Keywords"]))
        print("MeSH:", ", ".join(art["MeSH"]))
        print("---")







'''
Esearch = list of UID 
ESummary = feeding the UID and getting summary
EFetch = feed the UID and get some record
load the esummary result  create class and object and then print the name of each article 
'''
