# PubMed
(Tools for interacting with the entrez api)
## Overview
This project is a small Python tool that makes it easy to search PubMed and pull basic article information using the NCBI E-utilities API. It’s designed to be simple, readable, and easy to build on—no heavy libraries, just standard Python plus requests.
What It Does
The workflow is straightforward:
1.	Search PubMed with a keyword (Esearch).
PubMed returns a session ID and list of PMIDs.
2.	Fetch article data (Efetch).
The script pulls the full XML records for those PMIDs.
3.	Parse the XML and extract useful fields.
Right now it collects titles, keywords, and MeSH terms and formats them into clean Python dictionaries.
This creates a quick way to explore PubMed programmatically or use the results in research or data-analysis projects.
## Goal
The goal of this project is to provide a lightweight and clear starting point for working with PubMed data programmatically. The code is intentionally simple so it can be customized or expanded into larger workflows—such as automated literature reviews, metadata extraction, or bioinformatics pipelines
## Project Structure
#### main.py:
Runs a sample search and prints results
#### PubMed.py:            
Handles the PubMed API (Esearch, Efetch)
#### PubMedSearch.py:      
Parses XML and extracts article details




