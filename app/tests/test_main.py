import unittest
from fastapi.testclient import TestClient
from app.main import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_winners(self):
        response = self.client.get("/winners")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("winners", data)
        self.assertEqual(len(data["winners"]), 3)


if __name__ == "__main__":
    unittest.main()
