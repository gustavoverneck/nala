import os
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import requests
from .login import verify_user
from .token import generate_session_token
from .user import User
from .db import get_user_by_email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Send email notification
        
        # Email configuration
        sender_email = os.environ.get('CONTACT_EMAIL', '')
        receiver_email = os.environ.get('NOTIFICATION_EMAIL', '')
        password = os.environ.get('EMAIL_PASSWORD', '')
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Contato site DOM - Nova Mensagem de {name}"
        
        body = f"""
        Você recebeu uma nova mensagem do formulário de contato do site DOM Assessoria Empresarial:
        
        Nome: {name}
        Email: {email}
        
        Mensagem:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Connect to SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Adjust server settings as needed
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Email notification sent successfully")
        except Exception as e:
            print(f"Failed to send email notification: {e}")
        
        # For now, just return a success message
        return render_template('contato.html', success_message="Mensagem enviada com sucesso! Entraremos em contato em breve.")
    
    # This should not happen as the route only accepts POST
    return redirect(url_for('main.contato'))


@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@main.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')