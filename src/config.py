import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration for DeepSeek API integration"""
    
    # API Configuration
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    DEEPSEEK_API_BASE = os.getenv('DEEPSEEK_API_BASE', 'https://api.deepseek.com/v1')
    
    # Model Configuration
    MODEL_NAME = os.getenv('DEEPSEEK_MODEL', 'deepseek-coder')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2048))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    
    # Server Configuration
    PORT = int(os.getenv('PORT', 8000))
    HOST = os.getenv('HOST', '0.0.0.0')
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = ENVIRONMENT == 'development'
    
    # Available endpoints
    CHAT_ENDPOINT = f"{DEEPSEEK_API_BASE}/chat/completions"


def validate_config():
    """Validate that required configuration is set"""
    if not Config.DEEPSEEK_API_KEY:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
    return True
