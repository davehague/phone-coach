from call_handler import initiate_call
from config import load_config

def main():
    config = load_config()
    initiate_call(config)

if __name__ == "__main__":
    main()
