import pathlib
from typing import NamedTuple
from datetime import date
import flask
import random
from github_tools import get_repos, OWNER_NAME
import json
import sqlalchemy

app = flask.Flask(__name__)

static_path = pathlib.Path('static')

artwork = static_path / 'artwork'
blog_entry_path = static_path / 'blog_entries'

artwork.mkdir(parents = True, exist_ok = True)
blog_entry_path.mkdir(parents = True, exist_ok = True)


class BlogPost(NamedTuple):
    title: str
    date: date
    content: str
    tags: list

    def to_json(self):
        return json.dumps(self._asdict())

    @classmethod
    def from_json(cls, json_string):
        return cls(**json.loads(json_string))


def get_artwork():
    return random.sample([str(image) for image in artwork.iterdir()], 3)


def get_blog_posts():
    return [BlogPost.from_json(post.read_text()) for post in blog_entry_path.iterdir()]


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
    return flask.render_template(
            'blog.html',
            posts = get_blog_posts(),
    )


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
