# file: keep_alive.py

import time
import requests
from datetime import datetime

URL = "https://8080-firebase-idx-vps-1778525463513.cluster-h4khin2zjvavytgeaz7qjiy7nw.cloudworkstations.dev/"
INTERVAL = 300  # seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "WorkstationJwtPartitioned=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmdvb2dsZS5jb20vd29ya3N0YXRpb25zIiwiYXVkIjoiZmlyZWJhc2UtaWR4LXZwcy0xNzc4NTI1NDYzNTEzLmNsdXN0ZXItaDRraGluMnpqdmF2eXRnZWF6N3FqaXk3bncuY2xvdWR3b3Jrc3RhdGlvbnMuZGV2IiwiaWF0IjoxNzc4NTI4Mjc3LCJleHAiOjE3Nzg2MTQ2Nzd9.YBdW_j_asl4uTBsONDLMcvLhkBRMvyq5dDCjZLsBZerBW3gOEoKEOv4lc4qR5wkJIxtCdeq02zgsSE3XRQ-Ncevj2ODHmwjj2yd0IaKti7D04HZAvGCOyWfq66_0MorhmY1C57KVOYTjYbAWtzLoF7mt6Lc0TOGeP-zE8IkWCEEJrvdKcYKrjQ0E17_r1XKiky7oBcyDxDPWy9ii0iiarIt28dFympWA77_wHmXLaxlQU0a8Q5mA2IYDr3VBlBKj4D9Edacol0wPz0e8CpgUhsi4l4CZpiNSMJoLbowwzv1q27T5vYxnTT5GonNbMYInNJzwrpDlwXvjPElteJrcVw",
}


def now() -> str:
    return datetime.now().strftime("%H:%M")


def main() -> None:
    print("[start] keep-alive running", flush=True)

    with requests.Session() as session:
        session.headers.update(HEADERS)

        while True:
            try:
                r = session.get(URL, timeout=10)
                status = "OK" if r.status_code == 200 else str(r.status_code)
                print(f"[{now()}] {status}", flush=True)
                r.close()

            except KeyboardInterrupt:
                print("\n[stop] user exit", flush=True)
                break

            except Exception:
                print(f"[{now()}] error", flush=True)

            time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
