#!/usr/bin/env doit

from pathlib import Path
from doit.tools import title_with_actions

def task_compile_notebooks():
    for notebook in Path().glob('*.ipynb'):
        cmd = ['jupyter', 'nbconvert', '--to', 'pdf', '--template',
                'clean_report.tplx', '"{}"'.format(notebook)]
        yield {'basename': 'nbconvert-{0}'.format(notebook),
               'title': title_with_actions,
               'actions': [' '.join(cmd)],
               'targets': [str(notebook.with_suffix('.pdf'))],
               'file_dep': [str(notebook)]}
