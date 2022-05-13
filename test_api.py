import unittest
import requests

api_url =  'http://127.0.0.1:5000/read'

class TestUser(unittest.TestCase):


    def test_read(self):
        response = requests.get(url=api_url)
        self.assertEqual(response.status_code, 200)
    
    def test_create(self):
        Create = requests.post("http://127.0.0.1:5000/create", json={"name":"coca cola"}).status_code
        self.assertEqual(Create, 200)
    
    # def test_update(self):
    #     product = requests.patch('http://127.0.0.1:5000/update/627ec2306af6f6ed7cc01a39', json = {"name": "ismail"})
    #     self.assertEqual(product.status_code, 200)

    # def test_delete(self):
    #     product = requests.delete('http://127.0.0.1:5000/delete/627ec2306af6f6ed7cc01a39')
    #     self.assertEqual(product.status_code, 200)

 
 


    


