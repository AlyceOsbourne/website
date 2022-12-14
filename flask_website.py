import pathlib
import flask
from github_tools import get_repos, OWNER_NAME

app = flask.Flask(__name__)
pathlib.Path(app.static_folder).mkdir(parents = True, exist_ok = True)
pathlib.Path(app.template_folder).mkdir(parents = True, exist_ok = True)


@app.route('/')
def index():
    return flask.render_template(
            'index.html',
            name = OWNER_NAME,
            repos = get_repos(),
    )


@app.route('/blog')
def blog():
    return flask.render_template('blog.html')


if __name__ == '__main__':
    app.run(debug = False)
