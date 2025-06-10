import unittest
from email_alert_sender import send_alert

class TestAlert(unittest.TestCase):
    def test_send_alert(self):
        self.assertIsNone(send_alert("Test Subject", "Test Body"))

if __name__ == '__main__':
    unittest.main()
