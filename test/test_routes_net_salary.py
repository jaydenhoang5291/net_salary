import pytest
from fastapi.testclient import TestClient
from backend.main import application
from backend.services.calculator import NetSalaryCalculator
import pandas as pd
from io import BytesIO

client = TestClient(application)

class TestNetSalaryAPI:
    def test_single_api_valid_request(self):
        payload = {
            "gross": 25000000,
            "dependents": 2
        }
        expected = NetSalaryCalculator.calculate(**payload)
        res = client.post("/api/net/single", json=payload)
        assert res.status_code == 200
        data = res.json()
        assert round(data["net_salary"], 2) == round(expected.net_salary, 2)

    def test_bulk_api_with_excel(self, tmp_path):
        mock_data = {
            "Employee ID": [101, 102],
            "Name": ["Alice", "Bob"],
            "Gross Income": [18000000, 30000000],
            "Dependents": [0, 1]
        }
        df = pd.DataFrame(mock_data)
        file_path = tmp_path / "mock.xlsx"
        df.to_excel(file_path, index=False)

        with open(file_path, "rb") as f:
            res = client.post(
                "/api/net/batch",
                files={"file": ("mock.xlsx", f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
            )

        assert res.status_code == 200
        content = res.json()
        assert "data" in content
        assert len(content["data"]) == 2
        assert content["data"][0]["name"] == "Alice"

    def test_bulk_api_invalid_file(self):
        res = client.post(
            "/api/net/batch",
            files={"file": ("bad.txt", b"not excel", "text/plain")}
        )
        assert res.status_code == 400
        assert "Invalid file type" in res.json()["detail"]

#kiểm thử api