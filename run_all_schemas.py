# run_all_schemas.py
import subprocess
from schemas import SCHEMA_MAP
from authentication import get_access_token
import os

token = get_access_token()
os.makedirs("reports", exist_ok=True)

for name, url in SCHEMA_MAP.items():
    print(f"Running Schemathesis for schema: {name}")
    cmd = [
        "schemathesis", "run",
        "-H", f"Authorization: Bearer {token}",
        "--checks", "all",
        "--workers", "4",
        "--junit-xml", f"reports/{name}-report.xml",
        "--report", f"reports/{name}-report.html",
        "--report", f"reports/{name}-report.json",
        url,
    ]
    subprocess.run(cmd, check=True)
