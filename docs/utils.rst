.. _utils:

Utilities
=========

flask-turboduck ships with several useful utilities.  If you're coming from the
django world, some of these functions may look familiar to you.


Getting objects
---------------

:py:func:`get_object_or_404`

    Provides a handy way of getting an object or 404ing if not found, useful
    for urls that match based on ID.

    .. code-block:: python
    
        @app.route('/blog/<title>/')
        def blog_detail(title):
            blog = get_object_or_404(Blog.select().where(Blog.active==True), Blog.title==title)
            return render_template('blog/detail.html', blog=blog)

:py:func:`object_list`

    Wraps the given query and handles pagination automatically. Pagination defaults to ``20``
    but can be changed by passing in ``paginate_by=XX``.

    .. code-block:: python
    
        @app.route('/blog/')
        def blog_list():
            active = Blog.select().where(Blog.active==True)
            return object_list('blog/index.html', active)
    
    .. code-block:: html
    
        <!-- template -->
        {% for blog in object_list %}
          {# render the blog here #}
        {% endfor %}
        
        {% if page > 1 %}
          <a href="./?page={{ page - 1 }}">Prev</a>
        {% endif %}
        {% if page < pagination.get_pages() %}
          <a href="./?page={{ page + 1 }}">Next</a>
        {% endif %}

:py:class:`PaginatedQuery`

    A wrapper around a query (or model class) that handles pagination.

    Example:

    .. code-block:: python
    
        query = Blog.select().where(Blog.active==True)
        pq = PaginatedQuery(query)
        
        # assume url was /?page=3
        obj_list = pq.get_list()  # returns 3rd page of results
        
        pq.get_page() # returns "3"
        
        pq.get_pages() # returns total objects / objects-per-page


Misc
----


.. py:function:: slugify(string)

    Convert a string into something suitable for use as part of a URL,
    e.g. "This is a url" becomes "this-is-a-url"

    .. code-block:: python
    
        from flask_turboduck.utils import slugify
        
        
        class Blog(db.Model):
            title = CharField()
            slug = CharField()
            
            def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(Blog, self).save(*args, **kwargs)

.. py:function:: make_password(raw_password)

    Create a salted hash for the given plain-text password

.. py:function:: check_password(raw_password, enc_password)

    Compare a plain-text password against a salted/hashed password
