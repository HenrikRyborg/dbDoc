from flask import Flask, render_template, redirect
import flask_sijax
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import jinja2_highlight

# Setup Flask and read config from ConfigClass defined above
class MyFlask(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions',[]).append('jinja2_highlight.HighlightExtension')

app = MyFlask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Flask-sijax
flask_sijax.Sijax(app)

# Flask-bootstrap
Bootstrap(app)

# Flask-ckeditor 
ckeditor = CKEditor(app)

## import blueprints
from .indexView import indexBP

## Register blueprints
app.register_blueprint(indexBP, url_prefix='')