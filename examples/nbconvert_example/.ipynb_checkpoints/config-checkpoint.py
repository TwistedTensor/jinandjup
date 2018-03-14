from jinandjup import JinandjupPreprocessor

c = get_config()
c.NbConvertApp.notebooks = ['untitled.ipynb']
c.FilesWriter.build_directory = 'new_dir'
c.NbConvertApp.export_format = 'notebook'

c.JinandjupPreprocessor.data = {
    'custom_text':'"TEXT"',
    'x':'14'
}

c.NotebookExporter.preprocessors = [JinandjupPreprocessor,'nbconvert.preprocessors.ExecutePreprocessor']
