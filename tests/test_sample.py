import pytest


class TestBasicMath:
    """Basic math operations tests"""
    
    def test_addition(self):
        """Test addition operation"""
        assert 2 + 2 == 4
        assert 10 + 5 == 15
    
    def test_subtraction(self):
        """Test subtraction operation"""
        assert 10 - 5 == 5
        assert 100 - 50 == 50
    
    def test_multiplication(self):
        """Test multiplication operation"""
        assert 5 * 5 == 25
        assert 10 * 10 == 100
    
    def test_division(self):
        """Test division operation"""
        assert 10 / 2 == 5
        assert 100 / 10 == 10


class TestStringOperations:
    """String operations tests"""
    
    def test_string_concatenation(self):
        """Test string concatenation"""
        result = "Hello" + " " + "World"
        assert result == "Hello World"
    
    def test_string_upper(self):
        """Test string uppercase"""
        assert "hello".upper() == "HELLO"
    
    def test_string_lower(self):
        """Test string lowercase"""
        assert "HELLO".lower() == "hello"
    
    def test_string_length(self):
        """Test string length"""
        assert len("Jenkins") == 7
        assert len("CI/CD") == 5
