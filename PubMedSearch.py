import xml.etree.ElementTree as ET
import re

class PubMedSearch:
    def __init__(self, xml_text):
        self.root = ET.fromstring(xml_text)

    def get_articles(self):
        articles = []
        for article in self.root.findall(".//PubmedArticle"):
            record = {}
            # Title
            title_elem = article.find(".//Article/ArticleTitle")
            record["Title"] = title_elem.text if title_elem is not None else "[NO TITLE]"
            # Keywords
            kwlist = article.findall(".//KeywordList/Keyword")
            record["Keywords"] = [kw.text for kw in kwlist if kw.text] or ["None"]
            # MeSH terms
            meshlist = article.findall(".//MeshHeadingList/MeshHeading/DescriptorName")
            record["MeSH"] = [m.text for m in meshlist if m.text] or ["None"]
            articles.append(record)
        return articles



