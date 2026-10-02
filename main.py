from __future__ import annotations

from config import TARGET_URL, TIMEOUT_SECONDS
from main import create_account


if __name__ == "__main__":
    print(f"Opening signup flow: {TARGET_URL}")
    result = create_account()
    print(result)
