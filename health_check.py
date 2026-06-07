"""
Basic application health check.
"""

from app import app

client = app.test_client()

response = client.get("/health")

assert response.status_code == 200

print("Health endpoint OK")


