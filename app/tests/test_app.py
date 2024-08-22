import pytest
from app import app as testApp

@pytest.fixture
def client():
    # 创建一个测试客户端
    testApp.app.config['TESTING'] = True
    with testApp.app.test_client() as client:
        yield client

def test_index_route(client):
    # 测试根路由
    response = client.get('/')
    assert response.status_code == 200
    assert b"ArgoCD Dashboard" in response.data
    assert b"Python-flask" in response.data

def test_api_mock_route(client):
    # 测试/api/mock路由
    response = client.get('/api/mock')
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hi there, this app is running on eks/k8s cluster. change from test!!"

def test_api_postdata(client):
    # 测试/api/postdata
    payload = {"key":"value"}
    response = client.post('/api/postdata', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == payload


def test_api_postdata_invalid_method(client):
    # 测试无效的HTTP方法
    response = client.put('/api/postdata')
    assert response.status_code == 405  # Method Not Allowed
