from setuptools import setup

setup(
        name='json2csv',
        version='0.1',
        modules=['json2csv'],
        scripts=['json2csv.py'],
        url='https://github.com/evidens/json2csv',
        license='MIT License',
        author='evidens',
        author_email='',
        description='Converts JSON files to CSV (pulling data from nested structures). Useful for Mongo data',
)