"""
Website to image colour palette generator
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_ckeditor import request
from forms import ToolsForm
from PIL import Image
import os
from dotenv import load_dotenv
from colour_palette_generator import colour_palette


# Demo tools
FILE_NAME = 'static/img/Hydrangeas.jpg'
PATH = "static/img/example.jpg"
no_colors_demo = 10
more_repeat_demo = colour_palette(FILE_NAME, no_colors_demo)


app = Flask(__name__)
load_dotenv('.env')
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


@app.route('/')
def demo():
    return render_template("index.html", image_name=FILE_NAME, colors_extract=more_repeat_demo,
                           no_colors=no_colors_demo, demo=True)


@app.route('/tools', methods=['GET', 'POST'])
def tools():
    if os.path.exists(PATH):
        os.remove(PATH)
    form = ToolsForm()
    if form.validate_on_submit():
        file_name = form.image.data
        image = Image.open(file_name)
        if '.png' in str(file_name):
            image = image.convert('RGB')
        image.save(PATH)
        colors = int(request.form.get('no_colors'))
        more_repeat = colour_palette(file_name, colors)
        return render_template("index.html", image_name=PATH, colors_extract=more_repeat, no_colors=colors, demo=False)
    return render_template("tools.html", form=form)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
