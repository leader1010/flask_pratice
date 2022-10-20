from converter_pratice import app
from unittest import TestCase


class TestConverter(TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_url(self):
        resp = self.client.get("/super")
        self.assertEquals(resp.data.decode('utf8'), "<a href=/3/123>converter to_url</a>")

    def test_to_python(self):
        resp = self.client.get("/3/111")
        self.assertEqual(resp.data.decode('utf8'), "hello 3 666")
