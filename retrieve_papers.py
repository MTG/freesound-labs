import requests
import time
import argparse
import os

API_KEY = os.getenv('SEMANTIC_SCHOLAR_API_KEY', None)
if API_KEY is None:
    print('WARNING: No API key found for Semantic Scholar. You may be subject to rate limiting. Consider setting the SEMANTIC_SCHOLAR_API_KEY environment variable.')

PAPERS_DIR = '_papers'
MANUAL_PAPERS_FILENAME = 'manual_paper_semantic_scholar_urls.txt'

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
    fid = open(filename, 'w')
    fid.write(contents)
    fid.close()

def get_citations_page(paper_id, page_size=200, offset=0):
    fields = 'paperId,title,authors,year,url,venue'
    semantic_scholar_url = 'https://api.semanticscholar.org/graph/v1/paper/{}/citations?fields={}&limit={}&offset={}'.format(paper_id, fields, page_size, offset)
    headers = {'X-API-KEY': API_KEY} if API_KEY else {}
    resp = requests.get(semantic_scholar_url, headers=headers).json()
    return resp

def get_all_citations_for_paper(paper_id, paper_name):
    print('- Searching papers citing {}'.format(paper_name))
    next_offset = 0
    papers_data = []
    while next_offset is not None:
        resp = get_citations_page(paper_id, offset=next_offset)
        next_offset = resp.get("next", None)
        papers_data += [element["citingPaper"] for element in resp['data']]
        time.sleep(1)
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
    for semantic_scholar_url in open(MANUAL_PAPERS_FILENAME, 'r').readlines():
        paper_id = semantic_scholar_url.split('/')[-1][:-1]
        print(paper_id)
        out_filename = paper_filename_from_id(paper_id)
        if not os.path.exists(out_filename):
            # If markdown file does not not already exist, get paper information and write file
            try:
                headers = {'X-API-KEY': API_KEY} if API_KEY else {}
                fields = 'paperId,title,authors,year,url,venue'
                resp = requests.get('https://api.semanticscholar.org/graph/v1/paper/{}?fields={}'.format(paper_id, fields), headers=headers).json()
            except Exception as e:
                print('ERROR getting info for paper id {}: {}'.format(paper_id, str(e)))
            print(resp)
            write_markdown_file(resp, out_filename)

            # Sleep to avoid API rate limiting
            time.sleep(1)


if __name__ == "__main__":
    args = parser.parse_args()
    #add_remote_papers()
    add_local_papers()
