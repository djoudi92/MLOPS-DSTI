import os
import sys
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from register import *

def test_validate_username():
    assert validate_username("DjoudiAbd")
    assert not validate_username("")
    assert not validate_username("Djoudi Abd")  # No spaces allowed
    assert validate_username("user_123")  # Underscores allowed

def test_validate_password():
    assert validate_password("Abcdef1!")  # Valid password
    assert not validate_password("12345678")  # No letters
    assert not validate_password("abcdefgh")  # No numbers
    assert not validate_password("Abcdh")  # Too short
    assert not validate_password("Abcdefg1")  # No special char

def test_validate_email():
    assert validate_email("user@example.com")
    assert not validate_email("userexample.com")  # Missing '@'
    assert not validate_email("user@examplecom")  # Missing '.'
    assert not validate_email("user@.com")  # Invalid domain

def test_get_user_input(monkeypatch):
    """Simulates user input and verifies the returned dictionary."""
    mock_input = io.StringIO("TestUser\ntest@example.com\nStrongPass1!\n")
    monkeypatch.setattr("sys.stdin", mock_input)

    user_data = get_user_input()
    
    assert user_data["username"] == "TestUser"
    assert user_data["email"] == "test@example.com"
    assert user_data["password"] == "StrongPass1!"
