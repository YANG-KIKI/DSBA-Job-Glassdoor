# 🔬 ML Experiment Sharing Platform

A lightweight MLOps tool designed for collecting, uploading, and visualizing ML experiments.  
It integrates a Streamlit-based web app with Firebase for storage, and provides CLI tools for automation and scripting.

---

## 🚀 Project Purpose

This project aims to streamline the logging and sharing of machine learning experiments by combining:
- A **Streamlit web interface** for easy upload and browsing,
- A **Firebase backend** (Realtime + Firestore) for data storage,
- Lightweight **CLI tools** to support scripting and automation in real ML workflows.

This project embodies **MLOps principles** by supporting reproducibility, traceability, and automation in ML experiment tracking.

---

## 🛠️ Features

- ✅ Upload experiment JSON files via web or CLI
- 📊 Browse experiments with real-time updates
- 🔍 Filter by user (CLI)
- 📥 Export results to CSV
- 🧱 Docker support for reproducibility
- 🧪 End-to-end: Streamlit ➝ Firebase ➝ Export

---

## 👥 Roles & Responsibilities

| Name                  | Role & Contribution |
|-----------------------|---------------------|
| **Piangpim CHANCHARUNEE** | 🔹 Team Lead & UI/Infra Designer<br>Designed project architecture, Streamlit UI, and Firebase Realtime DB setup |
| **Kaushnav ROY** | 🔍 Long-term Backend Strategy<br>Researched and explored Firebase Firestore structure for future scalability |
| **Hanqi YANG** | 🚀 Deployment Specialist<br>Responsible for deploying and testing the Streamlit app |
| **Ming GAO** | 🐳 Containerization Expert<br>Wrote and configured the Dockerfile for portable setup |
| **I-Hsun LU** | 📋 Project Manager & Spec Author<br>Coordinated development, wrote `spec.md` and `README.md`, maintained GitHub workflow |

---

## ⚙️ Quickstart: Run the App

### 1. Clone the repository
```bash
git clone https://github.com/your-org/ml-experiment-sharing.git
cd ml-experiment-sharing

### 2. Install dependencies

Make sure you have Python 3.8+ installed.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### 3. Set up Firebase

To use Firebase as a backend, you’ll need a Firebase project with Firestore or Realtime Database enabled.

1. Go to [Firebase Console](https://console.firebase.google.com/), create a new project.
2. Navigate to **Project Settings > Service Accounts**.
3. Click **Generate new private key** to download the `firebaseKey.json`.
4. Place this file in the root directory of the project.

> **Important:** Do not upload `firebaseKey.json` to GitHub. It should remain private.

---

### 4. Run the Streamlit app locally

```bash
streamlit run streamlit.py
```

The app will be available at: [http://localhost:8501](http://localhost:8501)

---

### ✅ Try the hosted demo

You can also explore the deployed version of our app here:  
👉 [https://ml-experiment-sharing-mlops.streamlit.app/](https://ml-experiment-sharing-mlops.streamlit.app/)

---

## 👥 Contributors

Thanks to all the amazing contributors who made this project possible:

## 👥 Contributors

Thanks to all the amazing contributors who made this project possible:

- [@piangpimc](https://github.com/piangpimc) — Project Lead, Streamlit Designer, Firebase Realtime Setup  
- [@kaushnavGit](https://github.com/KaushnavGit) — Firebase Firestore Research & Long-Term Scalability  
- [@YANG-KIKI](https://github.com/YANG-KIKI) — Streamlit Deployment & Integration  
- [@GEMGM](https://github.com/GEMGM) — Dockerfile Author & Containerization  
- [@isha-lu](https://github.com/isha-lu) — Project Manager, Spec & README Author, GitHub Coordinator  



