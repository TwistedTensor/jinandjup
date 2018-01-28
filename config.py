from jinandjup import JinandjupPreprocessor

c = get_config()
c.NbConvertApp.notebooks = ['untitled.ipynb']
c.FilesWriter.build_directory = 'new_dir'
c.NbConvertApp.export_format = 'notebook'

c.JinandjupPreprocessor.data = {
    's':'"hello there"',
    'op':'3',
    'modeltype':'"lg"'
}

c.NotebookExporter.preprocessors = [JinandjupPreprocessor,'nbconvert.preprocessors.ExecutePreprocessor']
