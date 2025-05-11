from flask import Flask
from src.routes import main
from src.db import get_database_connection, initialize_database, add_user_to_user_table
from src.user import User
from dotenv import load_dotenv
import os
import subprocess
from waitress import serve

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    
    # Load secret key from environment variable
    load_dotenv()
    app.secret_key = os.getenv("TOKEN_SECRET")
    
    return app

# Create application for WSGI servers like Gunicorn to import
application = create_app()

if __name__ == '__main__':
    # Development
    # # Initialize SQLite database
    # initialize_database()

    # Regular Flask run
    # application.run(debug=False, port=os.getenv("PORT"), host=os.getenv("LOCAL_IP"))

    # Production    
    # Get port from environment or use default
    port = os.getenv("PORT")
    threads = os.getenv("WAITRESS_THREADS", "4")
    
    # Run with waitress
    print(f"Starting waitress server on port {port} with {threads} threads")
    serve(application, host='0.0.0.0', port=int(port), threads=int(threads))