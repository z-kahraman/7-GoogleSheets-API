import sys
import os

# Mevcut çalışma dizinini al
current_dir = os.getcwd()
# Bir üstteki dizine geç
parent_dir = os.path.dirname(current_dir)
os.chdir(parent_dir)
# Yeni çalışma dizinini al
# Ana proje klasörünün yolunu alın
project_folder = os.getcwd()

# Ana proje klasörünü modül arama yoluna ekleyin
sys.path.insert(0, project_folder)

# main.py dosyasını import edin
from main import app
import unittest
from fastapi.testclient import TestClient

client = TestClient(app)

class TestEndpoints(unittest.TestCase):
    
    def test_testdbconnection(self):
        response = client.get("/api/testdbconnection")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "DB connection successful"})
    
    def test_listfiles(self):
        response = client.get("/api/testlistfiles")
        self.assertEqual(response.status_code, 200)
        # Assert the desired structure or properties of the response JSON
        self.assertIn("result", response.json())
    
    def test_getsheettable(self):
        response = client.get("/api/getSheetTable")
        self.assertEqual(response.status_code, 200)
        # Assert the desired structure or properties of the response JSON
        self.assertIn("result", response.json())
    
    def test_syncdata(self):
        response = client.get("/api/syncData")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Data synchronized successfully"})

if __name__ == '__main__':
    unittest.main()
