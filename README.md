````md
<h1 align="center">🛡️ PhishGuard — AI Powered Phishing Protection</h1>

<p align="center">
  <img src="extension/logo.png" width="180" alt="PhishGuard Logo"/>
</p>

<p align="center">
  <b>Real-time machine learning Chrome extension that flags malicious websites before they steal your data.</b><br>
  Protecting users from phishing → safely, silently & intelligently.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Chrome-Extension-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Backend-Flask-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Model-RandomForest-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Category-Cybersecurity-red?style=flat-square"/>
</p>

---

## 🚀 Features
✔ Real-time URL safety scanning  
✔ AI model trained on labeled phishing datasets  
✔ Chrome badge indicator (🟢 safe | 🟡 suspicious | 🔴 malicious)  
✔ Popup panel showing URL + malicious score  
✔ Offline fallback heuristics if ML model not available  
✔ Open-source — easy to modify, extend and deploy

---

## 🧠 How It Works (Architecture)
```mermaid
graph TD;
    Browser-->Extension;
    Extension-->FlaskAPI;
    FlaskAPI-->MLModel;
    MLModel-->FlaskAPI;
    FlaskAPI-->Extension;
    Extension-->UserBadge;
````

1️⃣ **Browser opens a webpage**
2️⃣ Extension extracts the active URL
3️⃣ Sends it to local Flask backend
4️⃣ Backend converts URL → numerical feature vector
5️⃣ ML model predicts safety level
6️⃣ Result returned to browser & displayed instantly

---

## 📸 Screenshots

| Safe URL             | Malicious URL             |
| -------------------- | ------------------------- |
| 🟢 `OK — Safe`       | 🔴 `X — Malicious`        |
| ![](assets/safe.png) | ![](assets/malicious.png) |

*(Optional: replace with your own screenshots)*

---

## 📦 Repository Structure

```
PhishGuard/
│
├── backend/                # Flask API + ML model loader
│   ├── app.py
│   ├── features.py
│   └── pkl_model/          # (model.pkl goes here)
│
├── ml/                     # Training environment
│   ├── train_model.py
│   └── urlset.csv
│
├── extension/              # Chrome extension
│   ├── background.js
│   ├── popup.js
│   ├── popup.html
│   ├── manifest.json
│   └── logo.png
│
└── README.md
```

---

## 🧪 Running the Project

### 1️⃣ Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2️⃣ Start the API

```bash
python app.py
```

Runs at → `http://127.0.0.1:5000`

### 3️⃣ Load the Chrome Extension

```
Chrome → Manage Extensions → Developer Mode → Load Unpacked
Select: /extension
```

🎉 Now open any website and the badge updates instantly.

---

## ⚙️ Training & Updating the Model

Dataset is inside → `/ml/urlset.csv`

To retrain:

```bash
cd ml
python train_model.py
```

This generates → `model.pkl`
Move that file → `backend/pkl_model/model.pkl`

---

## 🧿 Vision

PhishGuard was built to **reduce phishing attacks using open-source AI** — a lightweight security layer that runs locally and respects privacy.

---

## 🤝 Contributing

PRs, feature requests, research suggestions — all welcome.

---

## 🧍 Author

**Nitanshu Tak**
B.Tech — Cloud Computing & Virtualization
Cybersecurity + AI Research

---

## ⭐ Support

If you like this project
→ Star ⭐ the repo
→ Share it so more students & developers learn cybersecurity 🔥

---

<p align="center">🛡️ PhishGuard — Protect before it’s too late.</p>
```

---
