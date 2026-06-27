"""PythonAnywhere WSGI entry point.

Set the WSGI file in your PythonAnywhere "Web" tab to this module's full path.
Inside that file, the standard pattern is:

    import sys
    path = '/home/<your-username>/kroma'
    if path not in sys.path:
        sys.path.insert(0, path)
    from wsgi import application  # noqa
"""
from app import app as application  # noqa: F401
