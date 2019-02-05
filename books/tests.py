#import unittest
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from . import views
from .views import index
from django.test.client import RequestFactory

class ModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_healthcheck(self):
        """Test the api can response health check"""
        response = self.client.get('/api/hello/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

class MyViewTest(TestCase):
    def test_get_request(self):
        rf = RequestFactory()
        # /test/ をGETメソッドでリクエストした場合のオブジェクト
        request = rf.get('/api/hello/')
        # view関数呼び出し
        response = index(request)
        b'\xE2\x82\xAC'.decode('UTF-8')

        print(response.content)

        # 結果を検証
        #self.assertEqual(response.content, "OK")
        self.assertEqual(response.content, b'[{\"msg\": \"Hello World!\"}]')


