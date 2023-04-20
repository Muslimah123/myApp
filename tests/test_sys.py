# Import necessary libraries
import pytest
import requests
from app import app, bcrypt, mysql, preprocess_transaction
from datetime import date, datetime
import re

def test_transcripts_page():
    # Test that the transcripts page is accessible to logged in users
    response = requests.get('http://localhost:5000/transcripts', cookies={'loggedin': 'True', 'username': 'test_user', 'id': '1'})
    assert response.status_code == 200

def test_revenue_dashboard_page():
    # Test that the revenue dashboard page is accessible to logged in users
    response = requests.get('http://localhost:5000/revenue_dashboard', cookies={'loggedin': 'True', 'username': 'test_user', 'id': '1'})
    assert response.status_code == 200

def test_preprocess_transaction():
    # Test the preprocess_transaction function with a sample transcript
    transcript = 'bought 3 apples'
    transaction_type, amount, item = preprocess_transaction(transcript)
    assert transaction_type == 'bought'
    assert amount == 0
    assert item == 'apples'

def test_revenue_dashboard_with_data():
    # Test the revenue dashboard page with actual sales data in the database
    response = requests.post('http://localhost:5000/revenue_dashboard', cookies={'loggedin': 'True', 'username': 'test_user', 'id': '1'}, data={'start_date': '2022-01-01', 'end_date': '2022-12-31'})
    assert response.status_code == 200
 
    assert 'apples' in response.text
    assert 'oranges' in response.text