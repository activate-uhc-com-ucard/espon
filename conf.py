# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If you have modules to document, add them to sys.path here.
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Epson Printer Driver Guide'
copyright = '2025, Epson Printer Driver Guide'
author = 'Epson Driver Support Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# SEO-friendly title and metadata for browsers and search engines
html_title = "How to Download & Install Epson Printer Drivers (Windows & Mac)"
html_short_title = "Epson Driver Setup Guide"
html_favicon = 'favicon.ico'  # Place this in the root or _static folder

# Theme configuration
# You can change this if you're using a different theme
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Hide "View page source" link
html_show_sourcelink = False

# Allow raw HTML in RST files (if needed for advanced formatting)
html_allow_unsafe = True
raw_enabled = True

# Optional theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Path to static files (CSS, JS, images)
# Uncomment below if you're using custom assets
# html_static_path = ['_static']
