from pathlib import Path
from request_practice import app
from .base_tmpl import BaseTmpl
import json

resources = Path(__file__).parent / "my_resources"


class TestRequest(BaseTmpl):
    def setUp(self) -> None:
        super().setUp()
        self.client = app.test_client()

    def test_request(self):
        resp = self.client.post("/upload")
        resp_data = json.loads(resp.data)
        self.assertEventNumber(405, resp_data.get("code"))

    def test_request_success(self):
        resp = self.client.post("/upload", data={"pic": (resources / "pic.png").open("rb")})
        resp_data = json.loads(resp.data)
        self.assertEventNumber(200, resp_data.get("code"))
