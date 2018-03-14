from __future__ import print_function
from traitlets import Dict
from nbconvert.preprocessors import Preprocessor
from ast import literal_eval
import jinja2
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)

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

@magics_class
class JinandjupMagics(Magics):
    def __init__(self,shell,defs={}):
        super(JinandjupMagics,self).__init__(shell)
        self.defs = defs
    @line_cell_magic
    def jinandjup(self,line,cell=None):
        if cell is None:
            for k,v in self.defs.items():
                print('{} = {}'.format(k,v))
        else:
            if line != '':
                data = literal_eval(line)
                if type(data) != dict:
                    raise ValueError('jinja data should be passed as a dict literal')
                _safety_check(data)
                for k,v in data.items():
                    self.defs[k] = v
            template = jinja2.Template(cell)
            new_cell = template.render(self.defs)
            print('------------CODE--------------')
            print(new_cell)
            print('------------------------------')
            self.shell.run_cell(new_cell)

def load_ipython_extension(ipython):
    jjmagics = JinandjupMagics(ipython)
    ipython.register_magics(jjmagics)
