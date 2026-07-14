from typing import Dict

class Config:
    def __init__(self):
        pass

    def load_config(self, config_file: str) -> Dict:
        try:
            with open(config_file, 'r') as file:
                import json
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f'Config file {config_file} not found')
        except json.JSONDecodeError as e:
            raise ValueError(f'Invalid JSON in config file: {e}')