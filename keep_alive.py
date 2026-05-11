# file: keep_alive.py

import time
import requests
from datetime import datetime

URL = ""
INTERVAL = 300  # seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "",
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
