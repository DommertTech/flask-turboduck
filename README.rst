Flask-Turboduck (Version 0.6.6)
============

Authors:

* Dommert (Dommert@Gmail.com)
* Coleifer (https://github.com/coleifer)




.. image:: http://deathproofduck.com/media/catalog/product/cache/1/image/346x/9df78eab33525d08d6e5fb8d27136e95/n/i/nickle-duck_1.jpg

Flask-Turboduck is a Flask extension for the PeeWee ORM (Object-Relational Mapping). It uses 'Zurb Foundation <http://foundation.zurb.com>'.
Flask-Turboduck provides a layer of integration between the `flask <http://flask.pocoo.org/>`_
web framework and the `PeeWee orm <http://peewee.readthedocs.org/>`_.

Batteries Included:

* Admin Interface (CRUD options)
* Authentication
* Rest API

Requirements:

* `flask <https://github.com/mitsuhiko/flask>`_
* `peewee <https://github.com/coleifer/peewee>`_
* `wtforms <https://github.com/wtforms/wtforms>`_
* `wtf-peewee <https://github.com/coleifer/wtf-peewee>`_
* python 2.5 or greater


check out the `documentation <http://flask-turboduck.readthedocs.org/>`_.

Admin Interface
---------------

influenced heavily by the `django <http://djangoproject.com>`_ admin, provides easy
create/edit/delete functionality for your project's models.

.. image:: http://i.imgur.com/EtzdO.jpg


Rest API
--------

influenced by `tastypie <https://github.com/toastdriven/django-tastypie>`_, provides
a way to expose a RESTful interface for your project's models.

::

    curl localhost:5000/api/v1/user/
    {
      "meta": {
        "model": "user", 
        "next": "", 
        "page": 1, 
        "previous": ""
      }, 
      "objects": [
        {
          "username": "admin", 
          "admin": true, 
          "email": "", 
          "join_date": "2011-09-16 18:34:49", 
          "active": true, 
          "id": 1
        }, 
        {
          "username": "coleifer", 
          "admin": false, 
          "email": "coleifer@gmail.com", 
          "join_date": "2011-09-16 18:35:56", 
          "active": true, 
          "id": 2
        }
      ]
    }


Installing
----------

I recommend installing in a virtualenv.  to get started::

    # create a new virtualenv
    virtualenv --no-site-packages project
    cd project/
    source bin/activate

    # install this project (will install dependencies as well)
    pip install flask-peewee


Example App
-----------

the project ships with an example app, which is a silly twitter clone.  to
start the example app, ``cd`` into the "example" directory and execute
the ``run_example.py`` script::

    cd example/
    python run_example.py

if you would like to test out the admin area, log in as "admin/admin" and navigate to:

http://127.0.0.1:5000/admin/

you can check out the REST api at the following url:

http://127.0.0.1:5000/api/message/

This project was Forked from Flask-PeeWee @ V.0.6.5.
