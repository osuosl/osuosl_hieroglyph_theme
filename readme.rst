Hieroglyph styles for OSU Open Source Lab theme

To make go:

1. pip install osuosl_sphinxtheme

2. In conf.py:
   import osuosl_sphinxtheme
   html_theme = 'osuosl'  ##(must be changed in file)!
   html_theme_path = osuosl_sphinxtheme.get_html_theme_path()
   html_static_path = ['_static', html_theme_path + '/osuosl/static/'] ##(must be changed in file)
   slide_theme_options = {'custom_css' : 'osuosl.css'}
   slide_footer = "<img src='_static/logo.png'>"

For the html_theme and html_static_path variables, you must find the defaults in the file and change them, as they will not be overridden by your declaration of them!

3. Make slides
