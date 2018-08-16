#!/usr/bin/python3
"""The / route"""

from models import storage
from models.state import State


if __name__ == "__main__":
    from flask import Flask
    import flask

    app = Flask(__name__)

    @app.route('/states_list/', strict_slashes=False)
    def states_list():
        """list states from database"""
        states = storage.all(State)
        stateidname = []
        for state in states:
            stateidname.append((states[state].id, states[state].name))
        return flask.render_template('7-states_list.html',
                                     stateidname=stateidname)

    app.run(host='0.0.0.0')

    @app.teardown_appcontext
    def teardown_appcontext():
        storage.close()
