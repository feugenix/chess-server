"""
Settings module.
Also tries to import the local settings
"""

HOST = 'localhost'
PORT = 8765

try:
    #pylint: disable=W0611
    import settings_local
except ImportError:
    pass
