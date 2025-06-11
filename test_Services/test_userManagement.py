
import subprocess

from Utilities.readSchemaUrl import ReadSchemaProperties
from authentication import get_access_token
import os

token = get_access_token()
os.makedirs("reports", exist_ok=True)

alerts_schema= ReadSchemaProperties.get_user_management_schema()
for name, url in alerts_schema.items():
    print(f"Running Schemathesis for schema: {name}")
    cmd = [
            "schemathesis", "run",
            "-H", f"Authorization: Bearer {token}",
            "--checks", "all",
            "--workers", "4",
            url,
        ]
    subprocess.run(cmd, check=True)