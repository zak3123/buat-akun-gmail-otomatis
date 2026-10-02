from __future__ import annotations

import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

TARGET_URL = "https://accounts.google.com/signup"
TIMEOUT_SECONDS = 20
MAX_RETRIES = 3

FIRST_NAMES = [
    "Ayu",
    "Budi",
    "Citra",
    "Dewi",
    "Eko",
    "Fajar",
    "Gita",
    "Hendra",
    "Indra",
    "Jasmine",
]

LAST_NAMES = [
    "Santoso",
    "Wijaya",
    "Rahmawati",
    "Pratama",
    "Nugroho",
    "Putri",
    "Ramadhan",
    "Sari",
    "Permana",
    "Kusuma",
]


def random_name() -> tuple[str, str]:
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return first, last


def random_password(length: int = 12) -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))


def random_username(base_first: str, base_last: str) -> str:
    suffix = random.randint(100, 9999)
    return f"{base_first.lower()}.{base_last.lower()}{suffix}"


def build_account_data() -> dict:
    first, last = random_name()
    username = random_username(first, last)
    return {
        "first_name": first,
        "last_name": last,
        "username": username,
        "password": random_password(),
    }
