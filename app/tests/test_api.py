import json

from api import app


def test_app_hello_world_endpoint_returns_text():
    """Test whether the root endpoint returns expected output"""
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello World'


def test_app_intense_endpoint_returns_json():
    """Test whether the root endpoint returns expected output"""
    response = app.test_client().get('/intense?timeout=1')
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) == {'status': 'success', 'timeout': 1}
