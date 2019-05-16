# Needs Python 3 and "scholarly" package
# pip install scholarly - https://pypi.org/project/scholarly/

from __future__ import print_function
import scholarly
import pprint
import os

TEMPLATE = """
---
layout: paper
type: {type},
id: "{id}",
title: "{title}"
publication: "{publication}"
year: {year}
url: {url}
authors: "{authors}"
{extra}
---
"""

queries = [
    'Freesound technical demo', # Find papers that cite "Freesound Technical demo" ACM paper
    'Freesound 2: An improved platform for sharing audio clips', # Find papers that cite ISMIR 2015 paper
]

for q in queries:
    print('* Searching for papers citing: ' + q)
    search_query = scholarly.search_pubs_query(q)  
    publication = next(search_query)
    for paper in publication.get_citedby():
        paper_id = paper.bib['ID']
        print('*', paper_id)
        out_filename = '_papers/paper_{0}.markdown'.format(paper_id)
        
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

                extra = ''
                if 'abstract' in  data:
                    extra += 'abstract: "{0}"'.format(data['abstract'])

                contents = TEMPLATE.format(
                    type=data['ENTRYTYPE'],
                    title=data['title'],
                    url=data['url'],
                    year=data['year'],
                    authors=data['author'],
                    id=data['ID'],
                    publication=publication,
                    extra=extra,
                )
                fid = open(out_filename, 'w')
                fid.write(contents)
                fid.close()
                print('Saved in {0}'.format(out_filename))        

            except:
                print('Could not retrieve information for paper')
        else:
            print('Skipping as it alrady exists')
