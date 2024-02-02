import pytest
from app import app

@pytest.fixture
def client():
    # 创建一个测试客户端
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index_route(client):
    # 测试根路由
    response = client.get('/')
    assert response.status_code == 200
    assert b"ArgoCD Dashboard" in response.data
    assert b"Python-flask project v2." in response.data

def test_api_mock_route(client):
    # 测试/api/mock路由
    response = client.get('/api/mock')
    assert response.status_code == 200
    #data = response.get_json()
    #assert data["message"] == "Hi there, this app is running on eks/k8s cluster. change from test"
