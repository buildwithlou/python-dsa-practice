# Configuration file for the Sphinx documentation builder.
import os
import sys

# -- Path setup -----------------------------------------------------
# We tell Sphinx to look up into the task_tracker directory
sys.path.insert(0, os.path.abspath("../Projects"))

# -- Project information -----------------------------------------------------
project = "Task Tracker"
copyright = "2026, Lourdes P."
author = "Lourdes P."
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
