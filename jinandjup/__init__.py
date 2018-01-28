from __future__ import print_function
from traitlets import Dict
from nbconvert.preprocessors import Preprocessor
from ast import literal_eval
import jinja2

def _safety_check(data):
    for v in data.values():
        try:
            literal_eval(v)
        except (ValueError,SyntaxError):
            raise ValueError("""Invalid value for literal: {}\n(Note: strings need to be quoted twice e.g. "'hello world'" """.format(v))

class JinandjupPreprocessor(Preprocessor):
    """
    A preprocessor that renders jinja whererver cells have a 'jinja' tag in their metadata
    or if they start with the jinandjup cell magic.
    """
    data = Dict({},config=True,help="A dict of values to be substituted in to the jinja template")

    def _renderer(self,source):
        template = jinja2.Template(source)
        return template.render(**self.data)

    def preprocess_cell(self,cell,resources,index):
        _safety_check(self.data)
        tags = cell['metadata'].get('tags',[])

        if cell['source'].startswith('%%jinandjup'):
            source = cell['source'].split('\n',1)[1]
            cell['source'] = self._renderer(source)

        elif 'jinja' in tags:
            cell['source'] = self._renderer(cell['source'])

        return cell,resources

def jinandjup(line,cell):
    '''
    This function defines an IPython cell magic that renders the current
    cell a jinja2 template before executing it. A dictionary of values
    should be passed as follows:
        %%jinandjup {'s':'"What is the answer to the ultimate question?"','i':'7'}
        print('{{s}}')
        print(6*{{i}})
    '''
    data = literal_eval(line)
    if type(data) != dict:
        raise ValueError('jinja data should be passed as a dictionary')
    _safety_check(data)
    ip = get_ipython()
    template = jinja2.Template(cell)
    new_cell = template.render(data)
    print('------------CODE--------------')
    print(new_cell)
    print('------------------------------')
    ip.run_cell(new_cell)

def load_ipython_extension(ipython):
    ipython.register_magic_function(jinandjup,'cell')
