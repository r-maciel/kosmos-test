import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST', 'localhost') # Valor predeterminado 'localhost' si no existe .env
PORT = int(os.getenv('PORT', 5000)) # Valor predeterminado '5000'  si no existe .env