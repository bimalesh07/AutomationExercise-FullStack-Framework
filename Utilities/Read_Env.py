import os
from pathlib import Path
from dotenv import load_dotenv

root_folder = Path(__file__).resolve().parents[1]
env_file_path = root_folder / '.env'
load_dotenv(dotenv_path=env_file_path, override=True)

class ReadEnv:
    @staticmethod
    def get_base_url():
        return os.getenv("base_url")
    
    @staticmethod  
    def get_base_api():
        return os.getenv("API_BASE_URL")
    
    @staticmethod
    def get_email():
        return os.getenv("email") 
    
    @staticmethod
    def get_password():
        return os.getenv("password")