# KIS Product Pages
Minisite showcasing PC hardware recommended by KIS at Kellogg School of Management.

This uses the [Jinja2](http://jinja.pocoo.org/docs/2.9/) templating engine for Python to stamp out HTML based on data 
provided in JSON format.

## Setup

In order to use this, you need to set up a [Python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and install the 
required modules specified in [requirements.txt](http://pip-python3.readthedocs.io/en/latest/user_guide.html#requirements-files).

You can then generate the HTML output by running `python compile_pages.py`. The paths to the JSON data files are hard-coded in the `compile_pages.py` file. The JSON files themselves specify the output filename and the type of template file to use.
