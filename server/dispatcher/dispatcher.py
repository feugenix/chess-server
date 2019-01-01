"""
File with dispatcher class
"""

import json

#pylint: disable=R0903
class Dispatcher:
    """
    Class responsible for dispatching commands
    """
    #pylint: disable=R0201
    def dispatch(self, text: str) -> str:
        """
        Logic of dispatching
        """
        return json.dumps({"status": "ok", "original": text})
