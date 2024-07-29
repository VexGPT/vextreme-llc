import asyncio
import websockets
from Modules.processing import process_message
from utils.config_loader import load_config

config = load_config()

async def handler(websocket, path):
    async for message in websocket:
        # Process the incoming message
        response = process_message(message)
        await websocket.send(response)

async def main():
    async with websockets.serve(handler, "localhost", config['websocket_port']):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())