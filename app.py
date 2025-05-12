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
    
if __name__ == '__main__':
    # Development
    # Initialize SQLite database
    # initialize_database()
    # user = User(
    #     name="Administrador", 
    #     email="admin@admin.com",
    #     password="admin",
    #     role="admin" # admin, user, etc.
    # )
    # add_user_to_user_table(user)
    
    # # Print users from database
    # conn = get_database_connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users")
    # users = cursor.fetchall()
    # print("Users in database:")
    # for user in users:
    #     print(user)
    # conn.close()

    # # Start app    
    # app = create_app()
    # app.run(debug=True, host=os.getenv("LOCAL_IP"), port=3000)

    # # # Production    
    # port = os.getenv("PORT")
    # threads = os.getenv("WAITRESS_THREADS", "4")
    
    # # Create the Flask application
    # application = create_app()
    
    # # Run with waitress
    # print(f"Starting waitress server on port {port} with {threads} threads")
    # serve(application, host='0.0.0.0', port=int(port), threads=int(threads))
    # print("Ending server connection.")
    
    # Render
    app = create_app()
    app.run(debug=False)
