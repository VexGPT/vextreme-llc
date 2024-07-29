import os
from utils.config_loader import load_config

def start_services():
    # Start the API Gateway
    os.system("python Modules/communication/api_gateway.py &")
    # Start the WebSocket handler
    os.system("python Modules/communication/websocket_handler.py &")

def main():
    config = load_config()
    
    print("Starting Vex GPT Services...")
    start_services()
    print("Services started successfully.")
    print(f"API Gateway running at {config['api_gateway_url']}")
    print(f"WebSocket Handler running at {config['websocket_url']}")

if __name__ == "__main__":
    main()