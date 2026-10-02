# Gmail Account Automation Starter

This repository is a starter project for a Selenium-based Gmail account automation flow.

Important:
- Use this project only for controlled, lawful testing and local experimentation.
- Respect Google's terms of service, rate limits, and relevant policies.
- Do not use this project for mass automated account creation or abuse.

## Project purpose
This starter project is designed to help an automation agent or developer:
- understand the Gmail signup flow,
- build a controlled Selenium automation script,
- handle form input and waits,
- export created account data to CSV.

## Repo structure
- `main.py` — main automation flow
- `config.py` — configurable constants
- `requirements.txt` — Python dependencies
- `data/names.txt` — random sample names
- `README.md` — local setup guide
- `AGENT_TASK.md` — tasks for an automation agent

## Quick start

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project
   ```bash
   python main.py
   ```

## Notes
- Chrome/Chromium must be installed.
- The Selenium automation flow is intentionally modular for easier maintenance.
- This repo is meant to be extended by Hermes or another coding agent.
