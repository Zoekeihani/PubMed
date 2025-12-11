from PubMed import PubMed
from PubMedSearch import PubMedSearch


if __name__ == "__main__":
    pubmed = PubMed()

    pubmed.esearch("fbn1")
    xml_text = pubmed.efetch()

    fetch = PubMedSearch(xml_text)
    articles = fetch.get_articles()

    for art in articles:
        print("Title:", art["Title"])
        print("Keywords:", ", ".join(art["Keywords"]))
        print("MeSH:", ", ".join(art["MeSH"]))
        print("---")







