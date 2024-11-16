import asyncio
import websockets
import json
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# WebSocket URL
SOCKET_URL = os.getenv('SOCKET_URL')

# CSV file path
CSV_FILE = "stock_data.csv"

# Batch size for performance optimization
BATCH_SIZE = 10


async def write_to_csv(data_batch):
    """Writes a batch of data to the CSV file."""
    # Check if the file exists to determine if headers are needed
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        # Write headers if the file is new
        if not file_exists:
            writer.writerow(["symbol", "price", "volume"])
        # Write each row of data
        writer.writerows(data_batch)


async def connect_and_store():
    """Connects to the WebSocket, receives data, and stores it in a CSV file."""
    while True:
        try:
            async with websockets.connect(SOCKET_URL) as websocket:
                print("Connected to WebSocket!")
                data_batch = []
                while True:
                    # Receive data from WebSocket
                    message = await websocket.recv()
                    data = json.loads(message)

                    # Process the received data
                    for symbol, price in data.items():
                        volume = 0 # Defining volume as 0 because the websocket does not provide the volume field
                        data_batch.append([symbol, price, volume])

                    # Write batch to CSV if batch size is reached
                    if len(data_batch) >= BATCH_SIZE:
                        await write_to_csv(data_batch)
                        print(f"Wrote {len(data_batch)} records to {CSV_FILE}.")
                        data_batch = []

        except (websockets.exceptions.ConnectionClosed, asyncio.TimeoutError) as e:
            print(f"Connection lost: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)  # Wait before reconnecting


if __name__ == "__main__":
    try:
        asyncio.run(connect_and_store())
    except KeyboardInterrupt:
        print("Program terminated by user.")
