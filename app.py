from flask import Flask
from src.routes import main
from src.db import get_database_connection, initialize_database, add_user_to_user_table
from src.user import User
from dotenv import load_dotenv
import os
from waitress import serve

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    
    # Load secret key from environment variable
    load_dotenv()
    app.secret_key = os.getenv("TOKEN_SECRET")
    
    return app

if __name__ == '__main__':
    # Development
    # Initialize SQLite database
    # initialize_database()
    # user = User(
    #     name=" ", 
    #     email=" ",
    #     password=" ",
    #     role="user" # admin, user, etc.
    # )
    #add_user_to_user_table(user)
    # app = create_app()
    # app.run(debug=True, host=os.getenv("LOCAL_IP"), port=3000)
    
    # Production    
    # Get port from environment or use default
    port = os.getenv("PORT")
    threads = os.getenv("WAITRESS_THREADS", "4")
    
    # Create the Flask application
    application = create_app()
    
    # Run with waitress
    print(f"Starting waitress server on port {port} with {threads} threads")
    serve(application, host='0.0.0.0', port=int(port), threads=int(threads))
    