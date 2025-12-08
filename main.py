import requests
import xml.etree
import re

class PubMed:
    def __init__(self):
        self.api_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
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
        # print("esearch Result: " + r.text)

        qk = ""
        webenv = ""

        for line in r.text.splitlines():
            qk_match = re.search("<QueryKey>(.+?)</QueryKey>", line)
            webenv_match = re.search("<WebEnv>(.+?)</WebEnv>", line)

            if qk_match:
                qk = qk_match.group(1)

            if webenv_match:
                webenv = webenv_match.group(1)

        print(f"query_key: {qk}\nwebenv: {webenv}")

    def esummary(self, qk, webenv):
        r = requests.get(self.api_base_url + f"esummary.fcgi?db=pubmed&query_key={qk}&WebEnv={webenv}")
        print("esummary Result: "+ r.text)


if __name__ == "__main__":
    pubmed = PubMed()
    # pubmed.test_query()
    # pubmed.einfo()
    # pubmed.esearch()
    #pubmed.esearch("fbn1")
    pubmed.esummary(1, "MCID_69336c0ee7c255073e09f504")



'''
Esearch = list of UID 
ESummary = feeding the UID and getting summary
EFetch = feed the UID and get some record
'''
