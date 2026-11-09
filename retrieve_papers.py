import requests
import time
import argparse
import os

API_KEY = os.getenv('SEMANTIC_SCHOLAR_API_KEY', None)
if API_KEY is None:
    print('WARNING: No API key found for Semantic Scholar. You may be subject to rate limiting. Consider setting the SEMANTIC_SCHOLAR_API_KEY environment variable.')

PAPERS_DIR = '_papers'
MANUAL_PAPERS_FILENAME = 'manual_paper_semantic_scholar_urls.txt'
PAPER_FIELDS = 'paperId,title,authors,year,url,venue,abstract'
MAX_REQUEST_ATTEMPTS = 8
MIN_REQUEST_INTERVAL = 1.0
last_request_time = None

semantic_scholar_source_papers_ids_names = [
    ('b3fef5d63abaca4a860603089ce91c0198034a54', 'FSD50K: an Open Dataset of Human-Labeled Sound Events'),
    ('c0efe552c69570cb2a73d112cdc5e7ab3afe36ab', 'Freesound technical demo'),
    ('ccc4b1a0ff1d85e5cd6d7247ddd1c16ab10e8145', 'Freesound Datasets: A Platform for the Creation of Open Audio Datasets'),
    ('d1e00bfe592993f06ed3a4b1440866a01e75962e', 'Freesound 2: An Improved Platform for Sharing Audio Clips'),
]

parser = argparse.ArgumentParser(
    description='Searches in Semantic Scholar Scholar for papers that cite some Freesound seminal publications and creates an '\
                'entry for them in the "_papers" folder. This command also adds papers listed in "manual_paper_semantic_scholar_urls.txt" '\
                'does its best to not duplicate entries.')


TEMPLATE = """---
layout: paper
id: "{id}"
title: "{title}"
publication: "{publication}"
year: {year}
external_url: {url}
authors: "{authors}"
---
"""

def paper_filename_from_id(paper_id):
    return os.path.join(PAPERS_DIR, 'paper_{0}.markdown'.format(paper_id))

def write_markdown_file(paper_data, filename):
    authors = ', '.join([author['name']  for author in paper_data['authors']])
    contents = TEMPLATE.format(
        title=paper_data['title'].title().replace('"', "'"),
        url=paper_data['url'],
        year=paper_data['year'],
        authors=authors,
        id=paper_data['paperId'],
        publication=paper_data['venue'] or '',
    )
    abstract = paper_data.get('abstract')
    if abstract and abstract.strip():
        contents += '\n' + abstract.strip() + '\n'
    with open(filename, 'w', encoding='utf-8') as fid:
        fid.write(contents)

def get_semantic_scholar_json(url, params):
    global last_request_time
    headers = {'X-API-KEY': API_KEY} if API_KEY else {}
    for attempt in range(MAX_REQUEST_ATTEMPTS):
        if last_request_time is not None:
            time.sleep(max(0, MIN_REQUEST_INTERVAL - (time.monotonic() - last_request_time)))
        last_request_time = time.monotonic()
        response = requests.get(url, params=params, headers=headers, timeout=60)
        if response.status_code == 429 and attempt < MAX_REQUEST_ATTEMPTS - 1:
            retry_after = response.headers.get('Retry-After', '')
            delay = max(1, int(retry_after)) if retry_after.isdigit() else 2 ** (attempt + 1)
            print('Semantic Scholar rate limited the request; retrying in {} seconds'.format(delay), flush=True)
            time.sleep(delay)
            continue
        if not response.ok:
            raise requests.HTTPError(
                'Semantic Scholar request failed (HTTP {}): {}'.format(response.status_code, response.text),
                response=response,
            )
        return response.json()

def get_citations_page(paper_id, page_size=200, offset=0):
    url = 'https://api.semanticscholar.org/graph/v1/paper/{}/citations'.format(paper_id)
    return get_semantic_scholar_json(url, {'fields': PAPER_FIELDS, 'limit': page_size, 'offset': offset})

def get_all_citations_for_paper(paper_id, paper_name):
    print('- Searching papers citing {}'.format(paper_name))
    next_offset = 0
    papers_data = []
    while next_offset is not None:
        resp = get_citations_page(paper_id, offset=next_offset)
        if not isinstance(resp, dict) or not isinstance(resp.get('data'), list):
            raise ValueError('Unexpected Semantic Scholar citations response for {}: {}'.format(paper_id, resp))
        next_offset = resp.get("next", None)
        papers_data += [element["citingPaper"] for element in resp['data']]
    print('Found {} citations'.format(len(papers_data)))
    return papers_data


def add_remote_papers():
    total_new_papers = 0
    for paper_id, paper_name in semantic_scholar_source_papers_ids_names:
        papers_data = get_all_citations_for_paper(paper_id, paper_name)
        for paper_data in papers_data:
            if paper_data['year'] is not None and paper_data['year'] != '':
                out_filename = paper_filename_from_id(paper_data['paperId'])
                if not os.path.exists(out_filename):
                    total_new_papers += 1
                    write_markdown_file(paper_data, out_filename)
    print('Total new papers added: {}'.format(total_new_papers))



def add_local_papers():

    print('- Adding papers from manual list...')
    with open(MANUAL_PAPERS_FILENAME, 'r', encoding='utf-8') as fid:
        urls = fid.readlines()
    for semantic_scholar_url in urls:
        paper_id = semantic_scholar_url.strip().split('/')[-1]
        print(paper_id)
        out_filename = paper_filename_from_id(paper_id)
        if not os.path.exists(out_filename):
            # If markdown file does not not already exist, get paper information and write file
            url = 'https://api.semanticscholar.org/graph/v1/paper/{}'.format(paper_id)
            resp = get_semantic_scholar_json(url, {'fields': PAPER_FIELDS})
            print(resp)
            write_markdown_file(resp, out_filename)

if __name__ == "__main__":
    args = parser.parse_args()
    add_remote_papers()
    add_local_papers()
