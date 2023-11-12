from rest_framework.test import APITestCase, APIClient
from iam.validation import get_user
import os


alter_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJsbWRXYzVzNjhMMkhSbUlGV25CQ29KSEExNnJFR0Fod3ZSbFVUOWdTY1ZvIn0.eyJleHAiOjE2OTgyMzgwMDEsImlhdCI6MTY5ODIzNjIwMSwianRpIjoiYzMzNjRhZWEtY2UxOC00OThhLTgyNTYtMWQ5ZGYzNTVlY2MzIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnZpc2FwaWNrLmNvbS9yZWFsbXMvbWFzdGVyIiwic3ViIjoiOTM3ZmQ4NzAtODQ3NS00ZmJiLTk0NjUtNDc2ZmRhZmNhZTlkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwic2Vzc2lvbl9zdGF0ZSI6IjQzN2RiMzVhLTJkYTktNGNhMC05ZDVlLWI3ZjI1NGViZWE1YyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zbWFydGFwcGx5bGVnYWwuY29tIiwiaHR0cHM6Ly9hcHBseS12aXNhcGljay52ZXJjZWwuYXBwIiwiaHR0cHM6Ly9hcHBseS52aXNhcGljay5jb20iLCJodHRwOi8vbG9jYWxob3N0OjMwMDAiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIjpwcm9maWxlOmdldCIsIm9mZmxpbmVfYWNjZXNzIiwidXNlciIsInRlc3QtcmVhbG0tcm9sZSIsIjpwcm9maWxlOnVwZGF0ZSJdfSwic2NvcGUiOiJyZWFkIHdlYmFwcC1kZWZhdWx0LXVzZXIgZW1haWwgd2ViLW9yaWdpbnMgb2ZmbGluZV9hY2Nlc3MgcHJvZmlsZSIsInNpZCI6IjQzN2RiMzVhLTJkYTktNGNhMC05ZDVlLWI3ZjI1NGViZWE1YyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiVXNlciBEZXZlbG9wZXIiLCJncm91cHMiOlsidXNlciJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ1c2VyQGRldi52aXNhcGljay5jb20iLCJnaXZlbl9uYW1lIjoiVXNlciIsImZhbWlseV9uYW1lIjoiRGV2ZWxvcGVyIiwiZW1haWwiOiJ1c2VyQGRldi52aXNhcGljay5jb20ifQ.DknlL0FIr_VQPU0EY5eHM_XDgCTbp-UEZBmpel4K18CWz2t1rQ3Hnm5L0tCLl6B8HTI9ad1D5oyN_StcExlZSUSgP0wiOzkxsWveHxHPJspVlaeWBZDcKQBeJANIDy2LLfaTHcVrU8MyBt3SPxxnqyC_6MCKFD2mpbcDrYVuGM8B8cMT4MFY8-wpKA9MsSjBnquJ9iEuBkuBX0fX79ULk_jCeGX4ajirgB2UA_zHCRtT1L47bgy9emk1n0SegPMSQRHfjNU0M4XG_rWFJBbjcAv_IvNyqhr6_-eUphTcBRy1by7_nrnq6I55Tl8Pbkk878vSVU0JwTbLkwFe27Gw1A"


class TestDjangoModelViewSet(APITestCase):
    def setUp(self) -> None:
        self.token = os.getenv("token", alter_token)
        self.invalid_token = self.token[:-2] + "x"
        self.user = get_user(self.token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        return super().setUp()

    def test_modelviewset_list(self):
        res = self.client.get("/model/")
        self.assertEqual(res.status_code, 403)

    def test_modelviewset_get(self):
        res = self.client.get("/model/1/")
        self.assertEqual(res.status_code, 200)

    def test_modelviewset_patch(self):
        res = self.client.patch("/model/1/", {})
        self.assertEqual(res.status_code, 200)

    def test_modelviewset_put(self):
        res = self.client.put("/model/1/", {"name": "new name"})
        self.assertEqual(res.status_code, 200)

    def test_modelviewset_delete(self):
        res = self.client.delete("/model/1/")
        self.assertEqual(res.status_code, 403)


class TestDjangoAPIView(APITestCase):
    def setUp(self) -> None:
        self.token = os.getenv("token", alter_token)
        self.invalid_token = self.token[:-2] + "x"
        self.user = get_user(self.token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        return super().setUp()

    def test_api_view_list(self):
        res = self.client.get("/api_view/")
        self.assertEqual(res.status_code, 403)
