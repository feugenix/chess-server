"""
Server startup logic
"""

import asyncio
import websockets
from .settings import settings as app_settings
from .dispatcher.dispatcher import Dispatcher

USERS = set()

class App:
    """
    Main application class
    """
    def __init__(self):
        self._dispatcher = Dispatcher()

    def run(self):
        """
        Method for starting the ws server
        """
        start_server = websockets.serve(self.on_message, app_settings.HOST, app_settings.PORT)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_server)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            USERS.clear()
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

    def register(self, websocket):
        USERS.add(websocket)

    def unregister(self, websocket):
        USERS.discard(websocket)

    async def on_message(self, websocket):
        """
        Handler of socket messages
        """
        self.register(websocket)
        try:
            async for message in websocket:
                answer = self._dispatcher.dispatch(message)
                await websocket.send(answer)
        finally:
            self.unregister(websocket)


if __name__ == "__main__":
    App().run()
