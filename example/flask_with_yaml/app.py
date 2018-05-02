# coding: utf-8

from flask import Flask, render_template
from dynaconf import FlaskDynaconf


# create your app
app = Flask(__name__)

FlaskDynaconf(
    app,
    ENVVAR_FOR_DYNACONF="MYSITE_SETTINGS_MODULE",
    DYNACONF_NAMESPACE='MYSITE',
    SETTINGS_MODULE_FOR_DYNACONF='settings.yml,.secrets.yml',
    EXTRA_VALUE='You can add aditional config vars here'
)


@app.route('/')
def index():
    return render_template('dynaconf.html')


if __name__ == '__main__':
    app.run()
