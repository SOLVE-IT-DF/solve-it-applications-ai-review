import os
import logging
from pybtex.database.input import bibtex
from pybtex.scanner import TokenRequired
from pybtex.plugin import find_plugin

def get_inline_from_file(filepath):
    parser = bibtex.Parser()
    try:
        bib_data = parser.parse_file(filepath)
    except TokenRequired:
        logging.error("Error parsing .bib file {}".format(filepath))
        return None

    for each in bib_data.entries:
        entry = bib_data.entries[each]
        persons = entry.persons
        if 'author' in persons:
            authors = persons['author']
        else:
            authors = []
        fields = entry.fields

        if len(authors) == 0:
            author_str = ''
        elif len(authors) == 1:
            author_str = authors[0].last_names[0]
        elif len(authors) == 2:
            author_str = '{} & {}'.format(authors[0].last_names[0], authors[1].last_names[0])
        else:
            author_str = '{} et al'.format(authors[0].last_names[0])

        if 'year' in fields:
            year = fields['year']
        else:
            year = None

        if year is None and len(authors) == 0:
            final_str = ""
        else:
            final_str = "({} {})".format(author_str, year)

        if 'note' in fields:
            note = fields['note']
        else:
            note = None

        return final_str, note


def get_all_inlines_from_path(folder_path):
    citations = []
    for each_bib_file in os.listdir(folder_path):
        if each_bib_file[-4:] == '.bib':
            bib_file_path = os.path.join(folder_path, each_bib_file)
            file_citations = get_inline_from_file(bib_file_path)
            if file_citations is not None:
                citations.append(file_citations)
    return citations


base_path = 'data'

for each_path in sorted(os.listdir(base_path)):
    if os.path.isdir(os.path.join(base_path, each_path)):
        if each_path != 'T1000':
            if os.path.exists(os.path.join(base_path, each_path, 'non-ai')):
                non_ai_citations = get_all_inlines_from_path(os.path.join(base_path, each_path, 'non-ai'))
            if os.path.exists(os.path.join(base_path, each_path, 'app-env')):
                app_env_citations = get_all_inlines_from_path(os.path.join(base_path, each_path, 'app-env'))
            if os.path.exists(os.path.join(base_path, each_path, 'ac-idea')):
                ac_idea_citations = get_all_inlines_from_path(os.path.join(base_path, each_path, 'ac-idea'))
            if os.path.exists(os.path.join(base_path, each_path, 'ac-imp')):
                ac_imp_citations = get_all_inlines_from_path(os.path.join(base_path, each_path, 'ac-imp'))
            if os.path.exists(os.path.join(base_path, each_path, 'in-tool')):
                in_tool_citations = get_all_inlines_from_path(os.path.join(base_path, each_path, 'in-tool'))

            print()
            print(each_path)
            print('=====')
            print('Application Envisioned:')
            for each in app_env_citations:
                print('- {} {}'.format(each[1], each[0]))
            print('Academic Ideas:')
            for each in ac_idea_citations:
                print('- {} {}'.format(each[1], each[0]))
            print('Academic Implementations:')
            for each in ac_imp_citations:
                print('- {} {}'.format(each[1], each[0]))
            print('In Tools:')
            for each in in_tool_citations:
                print('- {} {}'.format(each[1], each[0]))




quit()



