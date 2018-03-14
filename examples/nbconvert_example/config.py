from jinandjup import JinandjupPreprocessor

'''
This is a config file for nbconvert. It will create a new notebook in
the directory passed to c.FilesWriter.build_directory which will be the
the result of substituting the values given in the dictionary 
c.JinandjupPreprocessor.data into the template notebooks using jinja
in any cells with a 'jinja' tag in the cell matadata.

You can run the conversion with the following command:
jupyter nbconvert --config config.py
'''

c = get_config()
c.NbConvertApp.notebooks = ['template.ipynb']
c.FilesWriter.build_directory = 'new_dir'
c.NbConvertApp.export_format = 'notebook'

c.JinandjupPreprocessor.data = {
    'custom_text':'"TEXT"',
    'x':'14'
}

c.NotebookExporter.preprocessors = [JinandjupPreprocessor,'nbconvert.preprocessors.ExecutePreprocessor']
