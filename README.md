# 🛡️ **PhishGuard — AI Powered Phishing Protection**

> Real-time machine learning Chrome extension that flags malicious websites before they steal your data — protecting users from phishing safely, silently & intelligently.

---

### 🔗 Tech Stack
| Component | Technology |
|----------|------------|
| Browser  | Chrome Extension |
| Backend  | Flask API |
| Model    | Random Forest |
| Domain   | Cybersecurity |

---

<p align="center">
  <img src="extension/PhishGuardLogo.PNG" width="200">
</p>


## 🚀 Features
✔ Real-time URL safety scanning  
✔ AI model trained on labeled phishing datasets  
✔ Chrome badge indicator (🟢 safe | 🟠 suspicious | 🔴 malicious)  
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

## 📸 Conditions

| 🟢 Safe URL | 🟠 Suspicious URL | 🔴 Malicious URL |
|------------|------------------|-----------------|
|These URL are safe to access.|These URL are Suspecious.|These URL are Malicious and you must avoid them.|

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
Move that file → `backend/model.pkl`

---

## 🧿 Vision

PhishGuard was built to **reduce phishing attacks using open-source AI** — a lightweight security layer that runs locally and respects privacy.

---

## 🤝 Contributing

PRs, feature requests, research suggestions — all welcome.

---

## 🧍 Author

**[Nitanshu Tak](https://in.linkedin.com/in/nitanshu-tak-89a1ba289)**
B.Tech — Cloud Computing & Virtualization
Cybersecurity + AI Research

---

## ⭐ Support

If you like this project
→ Star ⭐ the repo
→ Share it so more students & developers learn cybersecurity 🔥

---

<p align="center">🛡️ PhishGuard — Protect before it’s too late.</p>

---
