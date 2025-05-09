import os
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import requests
from .login import verify_user
from .token import generate_session_token
from .user import User
from .db import get_user_by_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
                
        if verify_user(email, password):
            token = generate_session_token()
            user_info = get_user_by_email(email)
            session['token'] = token
            session['user_info'] = {'email': user_info.email, 'name': user_info.name}  # Store user information in session
            return redirect(url_for('main.dashboard'))
        return render_template('login.html', error="Invalid email or password.", show_popup=True)
    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    # Check if user is logged in (session contains token and user_info)
    if 'user_info' in session:
        user_info = session['user_info']
        return render_template('dashboard.html', user_info=user_info)
    return redirect(url_for('main.login'))

@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main.route('/contato')
def contato():
    return render_template('contato.html')

@main.route('/send_message', methods=['POST'])
def send_message():
    pass

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@main.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')