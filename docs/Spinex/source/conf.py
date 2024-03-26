# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'P4 Documentation'
copyright = '2024, P4 Language Consortium'
author = 'Adarsh'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   'myst_parser',
   'breathe',
   'exhale'
]
breathe_default_project = "P4C-DOCUMENTATION-HOSTING"

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./api",
    "rootFileName":          "library_root.rst",
    "doxygenStripFromPath":  "..",
    # Heavily encouraged optional argument (see docs)
    "rootFileTitle":         "Library API",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    "INPUT = ../include"
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'
templates_path = ['_templates']
exclude_patterns = []

language = 'y'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {
        "text": "P4 Compiler",
    },
    "github_url": "https://github.com/p4lang",
    "collapse_navigation": True,
    "favicons": [
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "https://secure.example.com/favicon/favicon-16x16.png",
      },
      {
         "rel": "icon",
         "sizes": "32x32",
         "href": "favicon-32x32.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "180x180",
         "href": "apple-touch-icon.png"
      },]
    ,"use_edit_page_button": True,
}
html_context = {
    "github_url": "https://github.com",
    "github_user": "p4lang", 
    "github_repo": "p4c", 
    "github_version":"main",
    "doc_path": "docs",
}
html_sidebars = {
   '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'],
}

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory. They are copied after the builtin static files, so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/P4.png'
