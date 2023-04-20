import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from app import app

@pytest.fixture
def client():
    # Create a test client
    test_client = app.test_client()

    # Set up any test data or configuration here, if necessary

    # Return the test client
    return test_client

def test_index_page(client):
    # Send a GET request to the index page
    response = client.get('/')

    # Check that the response status code is 200 OK
    assert response.status_code == 200

    # Check that the response data contains the expected text
    assert b"Welcome" in response.data

def test_login(client):
    response = client.post('/login', data={
        'username': 'Hidaya',
        'password': 'Ashesi@2023'
    }, follow_redirects=True)
    
    assert response.status_code == 200
   
    #  assertions to test the behavior of your application after a successful login
    assert b"Record" in response.data

def test_registration(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'Password@2023'
        
    }, follow_redirects=True)

    assert response.status_code == 200