import requests
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



    def efetch(self):
        url = (self.api_base_url +
               f"efetch.fcgi?db=pubmed&query_key={self.qk}&WebEnv={self.webenv}&rettype={self.report_type}&retmode=xml&retmax={retmax}")
        r = requests.get(url)
        return r.text
