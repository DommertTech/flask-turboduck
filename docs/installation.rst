.. _installation:

Installing
==========

flask-turboduck can be installed very easily using `pip <http://www.pip-installer.org/en/latest/index.html>`_.

.. code-block:: shell

    pip install flask-turboduck

If you do not have the dependencies installed already, pip will install them
for you, but for reference they are:

* `flask <https://github.com/mitsuhiko/flask>`_
* `turboduck <https://github.com/coleifer/turboduck>`_
* `wtforms <https://bitbucket.org/simplecodes/wtforms>`_
* `wtf-turboduck <https://github.com/coleifer/wtf-turboduck>`_
* python 2.5 or greater


Using git
---------

If you want to run the very latest, feel free to pull down the repo from github
and install by hand.

.. code-block:: shell

    git clone https://github.com/coleifer/flask-turboduck.git
    cd flask-turboduck
    python setup.py install

You can run the tests using the test-runner::

    python setup.py test
