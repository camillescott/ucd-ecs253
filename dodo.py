#!/usr/bin/env doit

from pathlib import Path
from doit.tools import title_with_actions
from jupyter_core.paths import jupyter_data_dir

template = Path('clean_report.tplx')

def task_copy_template():
    global template

    template_dir = Path(jupyter_data_dir()) / 'templates'

    yield {'name': 'copy_template_to_jupyter_dir',
           'actions': ['cp {0} {1}'.format(template, template_dir)],
           'targets': [str(template_dir / template)],
           'file_dep': [str(template)],
           'clean': True}

def task_compile_notebooks():
    for notebook in Path().glob('*.ipynb'):

        cmd = ['jupyter', 'nbconvert', '--to', 'pdf', '--template',
                str(template), '"{}"'.format(notebook)]
        yield {'basename': 'nbconvert-{0}'.format(notebook),
               'title': title_with_actions,
               'actions': [' '.join(cmd)],
               'targets': [str(notebook.with_suffix('.pdf'))],
               'file_dep': [str(notebook)],
               'clean': True}
