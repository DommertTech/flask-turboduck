.. _database:

Database Wrapper
================

The turboduck database wrapper provides a thin layer of integration between flask
apps and the turboduck orm.

The database wrapper is important because it ensures that a database connection
is created for every incoming request, and closed upon request completion.  It
also provides a subclass of ``Model`` which works with the database specified
in your app's configuration.

Most features of ``flask-turboduck`` require a database wrapper, so you very likely
always create one.

The database wrapper reads its configuration from the Flask application.  The
configuration requires only two arguments, but any additional arguments will
be passed to the database driver when connecting:

`name`
    The name of the database to connect to (or filename if using sqlite3)

`engine`
    The database driver to use, must be a subclass of ``turboduck.Database``.

.. code-block:: python

    from flask import Flask
    from turboduck import *

    from flask_turboduck.db import Database

    DATABASE = {
        'name': 'example.db',
        'engine': 'turboduck.SqliteDatabase',
    }

    app = Flask(__name__)
    app.config.from_object(__name__) # load database configuration from this module

    # instantiate the db wrapper
    db = Database(app)

    # start creating models
    class Blog(db.Model):
        name = CharField()
        # .. etc

Other examples
--------------

To connect to MySQL using authentication:

.. code-block:: python

    DATABASE = {
        'name': 'my_database',
        'engine': 'turboduck.MySQLDatabase',
        'user': 'db_user',
        'passwd': 'secret password',
    }

If using a multi-threaded WSGI server:

.. code-block:: python

    DATABASE = {
        'name': 'foo.db',
        'engine': 'turboduck.SqliteDatabase',
        'threadlocals': True,
    }
