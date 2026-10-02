# Hermes Agent Task

Goal:
Build a robust Gmail signup automation project that can create and track accounts via Selenium, with modular and maintainable code.

Scope:
- Review the starter project in this repo.
- Improve selectors and waiting logic for the signup flow.
- Add better error handling and retry logic.
- Add CSV export and account tracking.
- Keep code readable and maintainable.
- Respect site terms, rate limits, and local testing boundaries.

Acceptance criteria:
- `main.py` runs without syntax errors.
- `requirements.txt` installs successfully.
- The project produces a CSV output file in `output/accounts.csv`.
- The automation flow is broken into small helper functions.
- README instructions are kept clear and simple.

Helpful hints:
- Use Selenium `WebDriverWait` instead of fixed sleeps where possible.
- Keep selectors configurable in a single place.
- Add logging for debugging.
- Prefer batch-friendly account generation and CSV tracking.

Do not:
- Add malicious or abusive automation patterns.
- Bypass anti-abuse protections without explicit, lawful authorization.
- Ignore data safety and repo hygiene.
