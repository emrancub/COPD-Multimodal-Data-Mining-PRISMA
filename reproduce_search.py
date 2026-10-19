#!/usr/bin/env python3
"""Reproduce the Europe PMC PubMed/MEDLINE (SRC:MED) search query for the WIREs DMKD COPD PRISMA Advanced Review."""
import argparse
import datetime
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', default='search_rerun.json', help='Output JSON path for retrieved records')
args = parser.parse_args()
out = Path(args.output).resolve()
if out.exists():
    raise SystemExit(f'Output file {out} already exists; choose a new --output filename to preserve prior data.')

log_path = here / 'search_log.json' if (here / 'search_log.json').exists() else (here.parent / 'data' / 'search_log.json')
log = json.loads(log_path.read_text(encoding='utf-8'))
query_str = log.get('query') or log.get('stream_1_query')

cursor = '*'
records = []
pages = []
while True:
    params = {
        'query': query_str,
        'format': 'json',
        'resultType': 'core',
        'pageSize': 1000,
        'cursorMark': cursor,
    }
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urlencode(params)
    request = Request(url, headers={'User-Agent': 'COPD-PRISMA-WIREs-DMKD-Reproducibility/1.0'})
    with urlopen(request, timeout=90) as response:
        payload = json.load(response)
    batch = payload.get('resultList', {}).get('result', [])
    pages.append(len(batch))
    for record in batch:
        records.append({
            k: record.get(k, '')
            for k in ('id', 'pmid', 'source', 'doi', 'title', 'pubYear', 'firstPublicationDate')
        })
    next_cursor = payload.get('nextCursorMark')
    if not batch or not next_cursor or next_cursor == cursor or len(records) >= payload.get('hitCount', 0):
        break
    cursor = next_cursor

result = {
    'run_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'archived_search_date': log.get('search_date', '2026-10-02'),
    'query': query_str,
    'hit_count': payload.get('hitCount', len(records)),
    'pages': pages,
    'records': records,
}
out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Successfully retrieved {len(records)} records (hitCount={payload.get('hitCount')}) -> {out}")
