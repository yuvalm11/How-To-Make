import os
import json
import shutil
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/final.html')
def final():
    return render_template('final.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/weeks.html')
def weeks():
    # open the json file from the static folder
    json_file = os.path.join(os.path.dirname(__file__), 'static/weeks.json')
    with open(json_file) as file:
        weeks = json.load(file)
    
    weeks_to_render = []
    for week in weeks:
        filename = f'weeks/week{week["id"]}.html'
        if os.path.exists(os.path.join(os.path.dirname(__file__), 'templates', filename)):
            weeks_to_render.append(week)

    print(weeks_to_render)
    return render_template('weeks.html', weeks=weeks_to_render)


@app.route('/compile')
def compile():
    templates = {'index.html': index, 'final.html': final, 'weeks.html': weeks, 'contact.html': contact}

    output_dir = os.path.join(os.path.dirname(__file__), '../')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename, function in templates.items():
        rendered_template = function()
        rendered_template = rendered_template.replace('"/static', '"static')

        output_file = os.path.join(output_dir, filename)
        with open(output_file, 'w') as file:
            file.write(rendered_template)

    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    shutil.copytree(static_dir, output_dir + '/static', dirs_exist_ok=True)

    return 'Static HTML files generated successfully!'


if __name__ == '__main__':
    app.run(debug=True)
