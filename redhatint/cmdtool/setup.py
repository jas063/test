from setuptools import setup, find_packages

setup(
    name='cmdtool',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    
    entry_points={
    'console_scripts': [
        'extract-text = cmdtool.script:extract_text',
        'generate-resource = cmdtool.script:generate_resource',
        'display-html = cmdtool.script:display_html',
    ],
},
)
