# Needs Python 3 and "scholarly" package
# pip install scholarly - https://pypi.org/project/scholarly/

from __future__ import print_function
import scholarly
import pprint
import os
import argparse
import time
import requests
import slugify
import random
import shutil


parser = argparse.ArgumentParser(
    description='Searches in Google Scholar for papers that cite Freesound seminal publications and creates an '\
                'entry for them in the "_papers" folder. The retrieve can be a bit lengthly. This command also adds '\
                'papers from the "_papers_manual" folder and does its best to not duplicate entries.')
parser.add_argument('--remote', action='store_true', help='Whether or not to query Google Scholar for new papers remotely')
parser.add_argument('--local', action='store_true', help='Whether or not to add local paper entries from "_papers_manual" folder.')


TEMPLATE = """---
layout: paper
type: {type}
id: "{id}"
title: "{title}"
publication: "{publication}"
year: {year}
external_url: {url}
authors: "{authors}"
---
"""

PAPERS_DIR = '_papers'
MANUAL_PAPERS_DIR = '_papers_manual'
queries = [
    'Freesound technical demo', # Find papers that cite "Freesound Technical demo" ACM paper
    'Freesound 2: An improved platform for sharing audio clips', # Find papers that cite ISMIR 2015 paper
]

# Monkeypatch scholarly URL to make sure content is retreived in english
scholarly.scholarly._PUBSEARCH = "/scholar?hl=en&q={0}"

def add_remote_papers():

    print('\n- Adding remote papers...')
    for q in queries:
        print('* Searching for papers citing: ' + q)
        search_query = scholarly.search_pubs_query(q)  
        publication = next(search_query)

        if hasattr(publication, 'url_scholarbib'):
            for paper in publication.get_citedby():
                paper_key = slugify.slugify('{0}-{1}'.format(paper.bib['author'], paper.bib['title']))
                print('*', paper_key)
                out_filename = os.path.join(PAPERS_DIR, 'paper_{0}.markdown'.format(paper_key)) 
        
                if not os.path.exists(out_filename):
                    try:
                        paper.fill()
                        data = paper.bib

                        if data['ENTRYTYPE'] == 'article':
                            publication = data['journal']
                        elif data['ENTRYTYPE'] == 'inproceedings':
                            publication = data['booktitle']
                        else:
                            publication = ''

                        contents = TEMPLATE.format(
                            type=data['ENTRYTYPE'],
                            title=data['title'],
                            url=data['url'],
                            year=data['year'],
                            authors=data['author'],
                            id=data['ID'],
                            publication=publication,
                        )
                        fid = open(out_filename, 'w')
                        fid.write(contents)
                        fid.close()
                        print('Saved in {0}'.format(out_filename))        

                    except:
                        print('Could not retrieve information for paper')
                else:
                    print('Skipping as it alrady exists')

                time.sleep(2 + random.random() * 4)  # Hopefully avoiding being throttled


def add_local_papers():
    print('\n- Adding local papers...')

    # First get existing paper titles to avoid duplicates
    added_titles = []
    for filename in os.listdir(PAPERS_DIR):
        try:
            lines = open(os.path.join(PAPERS_DIR, filename), 'r').readlines()
        except UnicodeDecodeError:
            lines = open(os.path.join(PAPERS_DIR, filename), 'r', encoding='windows-1252').readlines()
        title = ""
        for line in lines:
            if 'title:' in line:
                position = line.find('"')
                title = line[position+1:-2].lower()
        added_titles.append(title)

    skipped = 0
    for filename in os.listdir(MANUAL_PAPERS_DIR):
        lines = open(os.path.join(MANUAL_PAPERS_DIR, filename), 'r').readlines()
        title = ""
        for line in lines:
            if 'title:' in line:
                position = line.find('"')
                title = line[position+1:-2].lower()
        if title not in added_titles:
            # Paper seems to be new, copy it to the "papers" dir
            shutil.copy(os.path.join(MANUAL_PAPERS_DIR, filename), os.path.join(PAPERS_DIR, filename))
        else:
            skipped += 1
    print(f'{skipped} papers were not added because already existed in papers folder.')


def postprocess_papers():
    print('\n- Post-processing paper entries...')
    for filename in os.listdir(PAPERS_DIR):
        if filename.endswith('.markdown'):
            path = os.path.join(PAPERS_DIR, filename)
            contents = open(path).read()
            
            contents = contents.replace("{\\'a}", "á")
            contents = contents.replace("{\\'e}", "é")
            contents = contents.replace("{\\'i}", "í")
            contents = contents.replace("{\\'\i}", "í")
            contents = contents.replace("{\\'o}", "ó")
            contents = contents.replace("{\\'u}", "ú")
                
            contents = contents.replace('{\\"a}', "ä")
            contents = contents.replace('{\\"e}', "ë")
            contents = contents.replace('{\\"i}', "ï")
            contents = contents.replace('{\\"o}', "ö")
            contents = contents.replace('{\\"u}', "ü")

            contents = contents.replace('{\\`a}', "à")
            contents = contents.replace('{\\`e}', "è")
            contents = contents.replace('{\\`o}', "ò")

            contents = contents.replace("{\\'c}{\\i}", "í")

            contents = contents.replace("\\", "")                
    
            fid = open(path, 'w')
            fid.write(contents)
            fid.close()

if __name__ == "__main__":
    args = parser.parse_args()
    if args.remote:
        add_remote_papers()
    if args.local:
        add_local_papers()
    postprocess_papers()
