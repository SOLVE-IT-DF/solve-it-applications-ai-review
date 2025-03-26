# An index of AI applicability in digital forensics - an application of the SOLVE-IT knowledge base

## Introduction
This repository demonstrates an application of the SOLVE-IT knowledge base (https://github.com/SOLVE-IT-DF/solve-it) as described in Section 5.5 of the paper below:

```Hargreaves, C., van Beek, H., Casey, E., SOLVE-IT: A proposed digital forensic knowledge base inspired by MITRE ATT&CK, Forensic Science International: Digital Investigation, Volume 52, Supplement, 2025, 301864, ISSN 2666-2817, https://doi.org/10.1016/j.fsidi.2025.301864```


## Description
It shows how the knowledge base can be used to consider available digital forensic techniques in a structured manner and consider the existing and potential ways in which AI could be used to assist. 

The review conducted for the DFRWS EU 2025 paper uses explicit categories (described below) rather than general ones e.g. high, medium or low. Also note that generic applications such as the use of AI to inform how to perform a technique or explain CLI tool usage are not included.

Categories are:

- Unclassified
- Non AI-based process likely sufficient
- Some application can be envisaged
- In academic work (idea)
- In academic work (implementation)
- In tools

## PDF from DFRWS EU 2025

The details of the review can be found in the [releases](https://github.com/SOLVE-IT-DF/solve-it-applications-ai-review/releases) section as a PDF for now. This will shortly be updated with a code repo that auto-generates the output using the SOLVE-IT repo. This is superseded by the bibtex implementation (see below)


## Bibtex implementation

The python script ```generate_listing.py``` will look in the data folder and iterate through all subfolders that are named Txxxx which represent the techniques in SOLVE-IT. Each one has subfolders that represent the different 'status' (non-ai, app-environment, ac-idea, ac-imp, in-tool). Bibtex files can be placed in each of these folders with references to the supporting work. The 'note' field should be added to the .bib files to provide the text that explains the relevance of the reference and the details of the idea, or implementation. 

Output will be to stdout. For example T1001 (Triage):

```
T1001
=====
Application Envisioned:
Academic Ideas:
- Identifying the most relevant devices from a set could potentially be improved with AI (Du et al 2020)
Academic Implementations:
In Tools:
```


