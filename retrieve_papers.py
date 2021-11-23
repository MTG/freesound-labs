import requests
import time
import argparse
import os


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
    if authors == '':
        # If authors are empty, try loading data directly from paper id and not list of citations
        try:
            semantic_scholar_url = 'https://api.semanticscholar.org/v1/paper/{}'.format(paper_data['paperId'])
            resp = requests.get(semantic_scholar_url).json()
            authors = ', '.join([author['name']  for author in resp['authors']])
        except Exception as e:
            print('ERROR getting authors info for paper {}: {}'.format(paper_data['paperId'], str(e)))

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
    print('New paper saved in {0}'.format(filename)) 

def add_remote_papers():

    for paper_id, paper_name in semantic_scholar_source_papers_ids_names:
        
        # Get paper info (including the papers that cite the source paper)
        print('- Searching papers citing {}'.format(paper_name))
        try:
            semantic_scholar_url = 'https://api.semanticscholar.org/v1/paper/{}'.format(paper_id)
            resp = requests.get(semantic_scholar_url).json()
        except Exception as e:
            print('ERROR getting info for paper {}: {}'.format(paper_name, str(e)))

        # For each citation, write a markdown file
        for citation in resp['citations']:
            if citation['year'] is not None and citation['year'] != '':
                out_filename = paper_filename_from_id(citation['paperId'])
                if not os.path.exists(out_filename):
                    write_markdown_file(citation, out_filename)

        # Sleep to avoid API rate limiting
        time.sleep(1)


def add_local_papers():

    print('- Adding papers from manual list...')
    for semantic_scholar_url in open(MANUAL_PAPERS_FILENAME, 'r').readlines():
        paper_id = semantic_scholar_url.split('/')[-1][:-1]
        out_filename = paper_filename_from_id(paper_id)
        if not os.path.exists(out_filename):
            # If markdown file does not already exist, get paper information and write file
            try:
                resp = requests.get('https://api.semanticscholar.org/v1/paper/{}'.format(paper_id)).json()
            except Exception as e:
                print('ERROR getting info for paper id {}: {}'.format(paper_id, str(e)))
            write_markdown_file(resp, out_filename)

            # Sleep to avoid API rate limiting
            time.sleep(1)


if __name__ == "__main__":
    args = parser.parse_args()
    add_remote_papers()
    add_local_papers()
