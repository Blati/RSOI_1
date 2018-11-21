from django.test import Client, TestCase

class multiplyViewTest(TestCase):
    def setUp(self):
        self.c = Client()    
        
    def testNormalCase(self):
        response = self.c.get('/mult/', {'num1':'2', 'num2':'3'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(6, int(response.content))
        
    def testMissingParam(self):
        response = self.c.get('/mult/', {'num1':'2'})
        self.assertEqual(400, response.status_code)
        
        
class helloViewTest(TestCase):
    def setUp(self):
        self.c = Client()
        
    def testHelloWorld(self):
        response = self.c.get('/hello/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'<html><body>Hello world!!!</body></html>', response.content)