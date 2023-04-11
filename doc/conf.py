# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx.ext.githubpages
import sphinx.ext.extlinks

project = 'Metra M1T380 docs'
copyright = '2023, Roman Dobrodii'
author = 'Roman Dobrodii'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.githubpages', 'sphinx.ext.extlinks']

#templates_path = ['_templates']
exclude_patterns = []

extlinks = {
    'ghraw': ('https://github.com/rdobrodii/metra-m1t380-doc/raw/main/%s', ''),
    'ghblob': ('https://github.com/rdobrodii/metra-m1t380-doc/blob/main/%s', ''),
    'ghtree': ('https://github.com/rdobrodii/metra-m1t380-doc/tree/main/%s', '')
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_extra_path = ['../files/reversed/MHB8748.html']
