from flask import Flask
from src.routes import main
from src.db import get_database_connection, initialize_database, add_user_to_user_table
from src.user import User
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    # Load secret key from environment variable
    load_dotenv()
    app.register_blueprint(main)
    app.secret_key = os.getenv("TOKEN_SECRET")
    
    # Set server name from environment variable
    server_name = os.getenv("SERVER_NAME")
    if server_name:
        app.config['SERVER_NAME'] = server_name
        app.config['SESSION_COOKIE_DOMAIN'] = '.dom.cnt.br'
    
    return app
    
app = create_app()
if __name__ == '__main__':
    # Render
    app.run(debug=False)
