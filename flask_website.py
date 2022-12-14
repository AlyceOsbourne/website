import pathlib
import flask
import random
from github_tools import get_repos, OWNER_NAME

app = flask.Flask(__name__)
pathlib.Path(app.static_folder).mkdir(parents = True, exist_ok = True)
pathlib.Path(app.template_folder).mkdir(parents = True, exist_ok = True)
static_path = pathlib.Path('static')
artwork = static_path / 'artwork'


def get_artwork():
    return random.sample([str(image) for image in artwork.iterdir()], 3)


@app.route('/')
def index():
    return flask.render_template(
            'index.html',
            name = OWNER_NAME,
            repos = get_repos(),
            images = get_artwork(),
    )


@app.route('/blog')
def blog():
    return flask.render_template('blog.html')


if __name__ == '__main__':
    app.run(debug = True)
