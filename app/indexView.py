from flask import Blueprint, render_template, flash

indexBP = Blueprint('indexBP', __name__)

@indexBP.route('/')
def indexView():
    kwargs = {
        'titleRight':'Home',
        'contentTitle':'Page content'
    }

    return render_template('index.html', **kwargs)