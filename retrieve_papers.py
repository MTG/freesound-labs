# Needs Python 3 and "scholarly" package
# pip install scholarly - https://pypi.org/project/scholarly/

from __future__ import print_function
import scholarly
import pprint
import os

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
queries = [
    'Freesound technical demo', # Find papers that cite "Freesound Technical demo" ACM paper
    'Freesound 2: An improved platform for sharing audio clips', # Find papers that cite ISMIR 2015 paper
]

def retrieve_papers():
    for q in queries:
        print('* Searching for papers citing: ' + q)
        search_query = scholarly.search_pubs_query(q)  
        publication = next(search_query)
        for paper in publication.get_citedby():
            paper_id = paper.bib['ID']
            print('*', paper_id)
            out_filename = os.path.join(PAPERS_DIR, 'paper_{0}.markdown'.format(paper_id)) 
    
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


def postprocess_papers():
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

#retrieve_papers()
postprocess_papers()