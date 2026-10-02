from __future__ import annotations

import csv
import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from config import (
    OUTPUT_FILE,
    TARGET_URL,
    TIMEOUT_SECONDS,
    build_account_data,
    ensure_output_file,
)


def build_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1280,1024")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def save_account(account: dict) -> None:
    ensure_output_file()
    file_exists = OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0

    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["first_name", "last_name", "username", "password", "status"],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(account)


def wait_for_any(driver: webdriver.Chrome, selectors: list[tuple[str, str]], timeout: int = TIMEOUT_SECONDS):
    wait = WebDriverWait(driver, timeout)
    for by, value in selectors:
        try:
            return wait.until(EC.presence_of_element_located((by, value)))
        except Exception:
            continue
    raise TimeoutError(f"Tidak ada elemen yang cocok dari selector: {selectors}")


def fill_if_present(driver: webdriver.Chrome, selectors: list[tuple[str, str]], value: str) -> bool:
    for by, selector in selectors:
        try:
            element = driver.find_element(by, selector)
            element.clear()
            element.send_keys(value)
            return True
        except Exception:
            continue
    return False


def click_if_present(driver: webdriver.Chrome, selectors: list[tuple[str, str]]) -> bool:
    for by, selector in selectors:
        try:
            element = driver.find_element(by, selector)
            element.click()
            return True
        except Exception:
            continue
    return False


def create_account() -> dict:
    account = build_account_data()
    driver = build_driver()

    try:
        print(f"Membuka halaman signup: {TARGET_URL}")
        driver.get(TARGET_URL)
        time.sleep(2)

        # Form yang sering muncul di halaman Google Account signup.
        # Flow tetap manual pada langkah verifikasi / CAPTCHA / OTP karena Google memblokir otomatisasi.
        selectors_first = [
            (By.NAME, "firstName"),
            (By.ID, "firstName"),
            (By.XPATH, "//input[@name='firstName']"),
        ]
        selectors_last = [
            (By.NAME, "lastName"),
            (By.ID, "lastName"),
            (By.XPATH, "//input[@name='lastName']"),
        ]

        if not fill_if_present(driver, selectors_first, account["first_name"]):
            print("Field firstName tidak ditemukan. Harap lanjutkan secara manual.")

        if not fill_if_present(driver, selectors_last, account["last_name"]):
            print("Field lastName tidak ditemukan. Harap lanjutkan secara manual.")

        print("Data dasar sudah diisi bila field ditemukan.")
        print("Google bisa meminta CAPTCHA, verifikasi, atau OTP secara manual.")
        print("Silakan lanjutkan proses pembuatan akun di browser yang terbuka.")
        input("Tekan Enter setelah akun berhasil dibuat atau proses berhenti: ")

        account["status"] = "manual_review_required"
        save_account(account)
        return account

    except Exception as exc:
        account["status"] = f"error:{type(exc).__name__}"
        save_account(account)
        return account

    finally:
        try:
            driver.quit()
        except Exception:
            pass


if __name__ == "__main__":
    print("Memulai flow Gmail signup dengan pendekatan semi-otomatis.")
    result = create_account()
    print("Hasil:", result)
    print(f"Data akun tersimpan di: {OUTPUT_FILE}")
