import unittest
from app import app # Replace 'your_flask_app_filename' with the name of your Python file containing the Flask app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('ArgoCD Dashboard', response.data.decode('utf-8'))

#    def test_api_mock(self):
#        response = self.app.get('/api/mock')
#        self.assertEqual(response.status_code, 200)
#        data = json.loads(response.data.decode('utf-8'))
#        self.assertIn('message', data)
#        self.assertEqual(data['message'], "Hi there, this app is running on eks/k8s cluster. change from test")
#
#    def test_api_postdata_get_method(self):
#        response = self.app.get('/api/postdata')
#        self.assertEqual(response.status_code, 200)
#        data = json.loads(response.data.decode('utf-8'))
#        self.assertIn('message', data)
#        self.assertEqual(data['message'], "Hi there, flask app, postdata api echo message.")
#
#    def test_api_postdata_post_method(self):
#        mock_data = {"key": "value"}
#        response = self.app.post('/api/postdata', data=json.dumps(mock_data), content_type='application/json')
#        self.assertEqual(response.status_code, 200)
#        data = json.loads(response.data.decode('utf-8'))
#        self.assertIn('message', data)
#        self.assertDictEqual(data['message'], mock_data)

if __name__ == '__main__':
    unittest.main()
