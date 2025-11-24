from __future__ import annotations

import importlib.metadata

project = "stac-cano"
copyright = "2025, Jack Hayes"
author = "Jack Hayes"
version = release = importlib.metadata.version("stac-cano")

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
}
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "announcement": "Welcome to stac-cano!",
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Jack-Hayes/stac-cano",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
    "show_version_warning_banner": True,
    "footer_center": ["last-updated"],
}
html_title = "stac-cano"
html_context = {
    "github_user": "Jack-Hayes",
    "github_repo": "stac-cano",
    "github_version": "main",
    "doc_path": "docs",
}
html_show_sourcelink = False
html_static_path = ["_static"]

myst_enable_extensions = [
    "colon_fence",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pystac": ("https://pystac.readthedocs.io/en/stable", None),
    "xarray": ("https://docs.xarray.dev/en/stable", None),
}

always_document_param_types = True
nb_execution_mode = "auto"
nb_execution_show_tb = True
nb_execution_timeout = 90
nb_execution_allow_errors = False
