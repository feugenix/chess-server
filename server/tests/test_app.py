from asynctest import TestCase, patch
from server.app import App

class AppTest(TestCase):
    @patch('server.app.Dispatcher')
    def test_ok(self, mockDispatcher):
        app = App()
        mockDispatcher.assert_called_with()

    @patch('server.app.USERS')
    def test_register(self, mockedUsers):
        app = App()
        app.register('<websocket>')
        mockedUsers.add.assert_called_with('<websocket>')

    @patch('server.app.USERS')
    def test_unregister(self, mockedUsers):
        app = App()
        app.unregister('<websocket>')
        mockedUsers.discard.assert_called_with('<websocket>')
