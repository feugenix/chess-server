"""
Tests for the app module
"""

from asynctest import TestCase, patch
from server.app import App

class AppTest(TestCase):
    """
    App test case
    """
    @patch('server.app.Dispatcher')
    def test_ok(self, mock_dispatcher):
        """
        Test for the constructor
        """
        App()
        mock_dispatcher.assert_called_with()

    @patch('server.app.USERS')
    def test_register(self, mocked_users):
        """
        Test for the method register
        """
        app = App()
        app.register('<websocket>')
        mocked_users.add.assert_called_with('<websocket>')

    @patch('server.app.USERS')
    def test_unregister(self, mocked_users):
        """
        Test for the method unregister
        """
        app = App()
        app.unregister('<websocket>')
        mocked_users.discard.assert_called_with('<websocket>')
