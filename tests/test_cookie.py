import json
from .base_tmpl import BaseTmpl
from cookie_practice import app


class TestCookie(BaseTmpl):
    def setUp(self):
        super().setUp()
        self.client = app.test_client()

    def test_login(self):
        resp = self.client.post("/login", data={"name": "ming"})
        self.assertEventNumber(resp.status_code, 200),

    def test_del(self):
        resp = self.client.post("/delete_cookie", data={"name": "ming"})
        self.assertEventNumber(resp.status_code, 200)

    def test_get(self):
        resp = self.client.post("/get_cookie")
        self.assertEventNumber(json.loads(resp.data).get("msg"), "ming")
