# Configuration file for the Sphinx documentation builder.

# -- Project information

# project = 'Lumache'
# copyright = '2021, Graziella'
# author = 'Graziella'
project = 'RefactortheDocs'
author = 'Refactor'
copyright = f'2025, {author}'

# release = '0.1'
# version = '0.1.0'
release = '0.9'
version = '0.9.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    #
    'sphinx_copybutton', # 一键复制代码按钮
    'sphinx_design', # 提供了一系列设计元素，如按钮、卡片、网格布局等
    'sphinxcontrib.mermaid', # mermaid
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'shibuya'

###

# 自定义页脚，显示版本信息
html_context = {
    'display_version': True, # 启用版本信息显示
    'version_info': f'v{version}', # 使用格式化字符串动态显示版本号，会显示为"v0.9.0"
}

###

# -- Options for EPUB output
epub_show_urls = 'footnote'
