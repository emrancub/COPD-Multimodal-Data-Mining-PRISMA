# COPD Health Data Mining Across Modalities — PRISMA 2020 Evidence Register & Reproducibility Dataset (Supplementary Dataset S1)

This repository contains the complete machine-readable PRISMA 2020 / PRISMA-ScR / PRISMA-S literature identification, screening, eligibility verification, four-domain **PROBAST+AI** risk-of-bias audit, and bibliographic verification dataset accompanying our Advanced Review submitted to ***WIREs Data Mining and Knowledge Discovery***:

> **Title:** *Mining health data for chronic obstructive pulmonary disease: Machine learning, deep learning, and knowledge discovery across modalities*
>
> **Authors:** Md Emran Hasan\$^{1}$, Yue-Fang Wu$^{2}$, and Dong-Jun Yu$^{1\*}\$
>
> **Affiliations:** \$^{1}$School of Computer Science and Engineering, Nanjing University of Science and Technology, Nanjing 210094, China; $^{2}$Department of Internal Medicine, Nanjing University of Science and Technology Hospital, Nanjing 210094, China.
>
> **Corresponding Author:** Prof. Dong-Jun Yu (`njyudj@njust.edu.cn`) | **First Author:** Md Emran Hasan (`mdemranhasan@njust.edu.cn`)

## Summary of PRISMA 2020 Two-Stream Evidence Accounting

| PRISMA 2020 Stage | Stream / Specification | Verified Record Count | 
| ----- | ----- | ----- | 
| **Stream 1 (Biomedical Core)** | PubMed/MEDLINE & PMC (`SRC:MED` via Europe PMC; `2020-01-01` to `2026-10-02`) | **1,192 unique PMIDs** | 
| **Stream 2 (Cross-Disciplinary)** | IEEE Xplore, ACM DL, ScienceDirect, SpringerLink, Nature, Wiley, RSNA, ATS, ERS (`474` audited → `268` unique → `128` overlapped & `2` unresolved removed) | **138 resolved non-overlapping records** | 
| **Total Unique Records Screened** | Combined deduplicated screening pool ($1,192 + 138$) | **1,330 unique records** | 
| **Primary Reports Sought** | `194` from Stream 1 + `6` from Stream 2 (`A001, A020, A026, A029, A030, A051`) | **200 primary reports sought** | 
| **Full-Text Reports Assessed** | `135` Europe PMC XML/PDF + `20` institutional/publisher full texts (**77.5% retrieval rate**) | **155 full-text reports assessed** | 
| **Reports Not Retrieved** | Subscription/embargo-gated reports itemized transparently with permanent DOIs (SI Table S3) | **45 unretrieved reports** | 
| **Full-Text Exclusions** | Excluded after full-text review with explicit study-level methodological reasons (SI Table S2) | **30 excluded reports** | 
| **Included Primary Studies** | Primary validation, prospective evaluation, or multi-cohort biological replication studies (SI Table S1) | **125 included primary studies** | 
| **Contextual & Methodological** | Foundational cohorts, reporting standards (TRIPOD+AI, PROBAST+AI, CLAIM, DECIDE-AI, CONSORT-AI), and methodological references | **80 contextual sources** | 
| **Total Verified Bibliography** | Cross-verified against Crossref and PubMed metadata ($125 + 80$) | **205 verified references** | 

## Repository File Manifest

| File Name | Format | Description & Reproducibility Role | 
| ----- | ----- | ----- | 
| `search_log.json` | JSON | Exact Europe PMC (`SRC:MED`) Boolean query, date bounds (`2020-01-01` to `2026-10-02`), interactive web search URL, parameterized REST API URL, and two-stream screening protocol. | 
| `search_export_and_screening.json` | JSON | Complete export of all **1,192 unique PubMed/Europe PMC records** with PMIDs, DOIs, publication dates, titles, and stage-by-stage screening outcomes. | 
| `supplied_reference_audit.json` | JSON | Cross-disciplinary audit of **474 candidate entries** (`268` unique records; `138` resolved non-overlapping with Stream 1) resolved against publisher-deposited Crossref metadata. | 
| `flow_counts.json` | JSON | Exact reconciled stage counts for the PRISMA 2020 two-stream flow diagram (Main Figure 2 and Table 1). | 
| `report_decisions.json` | JSON | Itemized retrieval and eligibility decisions for all **200 sought primary validation reports** (`125` included, `30` excluded at full text, `45` unavailable). | 
| `study_evidence.json` | JSON | Structured extraction records for all **125 included primary studies** (inputs, analytical target, validation cohort design, four-domain **PROBAST+AI** risk-of-bias rating, interpretation limit, and permanent DOI). | 
| `numeric_claim_audit.json` | JSON | Primary-source locator and interpretation-boundary verification records for quantitative benchmark estimates cited in the review (SI Table S8). | 
| `reference_verification.json` | JSON | Publisher-deposited Crossref and PubMed metadata verification records for all **205 references** in the unified bibliography. | 
| `reproduce_search.py` | Python 3 | Standalone executable Python script (standard library only) that queries the Europe PMC REST API using `search_log.json` and exports the retrieved records. | 

## Reproducing the Literature Search

### 1. Direct Browser Links (Zero Installation Required)

* **Interactive Europe PMC Web Search (1,192 PubMed/MEDLINE Records):** [Open in Browser](https://www.google.com/search?q=https://europepmc.org/search%3Fquery%3D%2528TITLE_ABS%253A%2522chronic%2520obstructive%2520pulmonary%2520disease%2522%2520OR%2520TITLE_ABS%253ACOPD%2529%2520AND%2520%2528TITLE_ABS%253A%2522machine%2520learning%2522%2520OR%2520TITLE_ABS%253A%2522deep%2520learning%2522%2520OR%2520TITLE_ABS%253A%2522artificial%2520intelligence%2522%2520OR%2520TITLE_ABS%253A%2522neural%2520network%2522%2520OR%2520TITLE_ABS%253A%2522neural%2520networks%2522%2520OR%2520TITLE_ABS%253Aradiomics%2529%2520AND%2520FIRST_PDATE%253A%255B2020-01-01%2520TO%25202026-10-02%255D%2520AND%2520SRC%253AMED)

* **Live Parameterized Europe PMC REST API JSON Query:** [Open JSON Response in Browser](https://www.google.com/search?q=https://www.ebi.ac.uk/europepmc/webservices/rest/search%3Fquery%3D%2528TITLE_ABS%253A%2522chronic%2Bobstructive%2Bpulmonary%2Bdisease%2522%2BOR%2BTITLE_ABS%253ACOPD%2529%2BAND%2B%2528TITLE_ABS%253A%2522machine%2Blearning%2522%2BOR%2BTITLE_ABS%253A%2522deep%2Blearning%2522%2BOR%2BTITLE_ABS%253A%2522artificial%2Bintelligence%2522%2BOR%2BTITLE_ABS%253A%2522neural%2Bnetwork%2522%2BOR%2BTITLE_ABS%253A%2522neural%2Bnetworks%2522%2BOR%2BTITLE_ABS%253Aradiomics%2529%2BAND%2BFIRST_PDATE%253A%255B2020-01-01%2BTO%2B2026-10-02%255D%2BAND%2BSRC%253AMED%26format%3Djson%26resultType%3Dcore%26pageSize%3D25)

### 2. Command-Line Python Reproduction

Requires Python 3.8+ (uses only standard-library modules `urllib`, `json`, `pathlib`, `argparse`):

```
python3 reproduce_search.py --output search_rerun.json

```

## License & Citation

All structured extraction tables, PROBAST+AI audit annotations, and reproduction scripts in this repository are released under the MIT / CC-BY 4.0 license for academic and scientific research. No identifiable patient-level health data are stored or redistributed in this repository.