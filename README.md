# Instagram Dummy Account Brute-Force Simulator

⚠️ **Warning: This project is intended only for testing on your own Instagram dummy accounts. Do NOT use it on real accounts. Using it on real accounts can result in permanent account bans.**

---

## Overview

This Python tool simulates an Instagram password brute-force attack. It:

- Asks for a username
- Generates password combinations
- Attempts to log in using Selenium in a real browser
- Shows progress and indicates when the password is “found”

> Note: It is **designed for educational purposes** and to experiment safely with a **dummy/test account** only.

---

## Features

- Username input
- Password combination generation
- Selenium automation of Instagram login page
- Colored console output for attempts and success
- Safe testing on small password sets

---

## Requirements

- Python 3
- Selenium
- Chromium or Chrome browser
- ChromeDriver matching your browser version
- `colorama` for colored console output

---

## Installation

On Kali Linux:

```bash
sudo apt update
sudo apt install python3-pip chromium-chromedriver
pip3 install selenium colorama
