from flask import Flask
from flask.ext.assets import Environment, Bundle

app = Flask(__name__, static_folder='static', static_url_path='')

# Load config.
app.config.from_object('config')

# Assets
assets = Environment()
css = Bundle('css/index.sass', filters='sass', depends=['css/**/*.sass', 'css/**/**/*.sass'], output='css/index.css')
assets.register('css_all', css)
assets.init_app(app)

# So we can use Jade templates.
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

from app import routes
