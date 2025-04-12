# 🔐 Selenium Authentication Tests

Automated test suite for verifying login functionality on [SauceDemo](https://www.saucedemo.com) using Selenium WebDriver and `pytest`.

---

## 📦 Requirements

Make sure you have Python installed, then install the required packages:

```bash
pip install -U pytest selenium
```

---

## 🚀 How to Run

### ▶️ Basic test run:

```bash
pytest
```

### 📝 Generate an HTML report:

```bash
pytest --html report-test.html
```

> This will create a file named `report-test.html` in your working directory. You can open it in any web browser to see a formatted test report.

---

## 🧪 Test Description

| Test Name             | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `test_authentication` | Tests login with valid credentials and checks redirection to inventory. |

---

## 🛠️ Stack

- 🐍 Python 3.x  
- 🧪 Pytest  
- 🌐 Selenium WebDriver  
- 🦊 Firefox (default — but can use Chrome/Edge)

---

## 📁 Project Structure

```
selenium-authentication-tests/
│
├── test_firstScript.py       # Main test file
├── report-test.html          # HTML report (generated after running tests)
├── requirements.txt          # (Optional) dependencies list
└── README.md                 # This file
```

---

## 👩‍💻 Author

Built with ❤️ by [Your Name Here]

---

## 📜 License

MIT — free to use, modify, and share. Just remember to credit and maybe buy a coffee ☕
