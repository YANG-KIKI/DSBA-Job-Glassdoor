# ML Experiment Sharing Platform

A lightweight MLOps tool designed for collecting, uploading, and visualizing ML experiments.
It integrates a **Streamlit** web app with **Firebase** for storage, and provides **CLI tools** for scripting and automation. This project also includes a Dockerized setup for reproducibility.

---

##  Project Purpose

This platform streamlines logging and sharing of ML experiments by combining:

- A Streamlit web interface for uploading and browsing experiments
- A Firebase backend (Realtime DB) for storing experiment logs
- CLI tools to support automation and local development workflows

It supports MLOps principles like **traceability**, **reproducibility**, and **team collaboration**.

---

## Features

- Upload experiment JSONs via Web UI or CLI
- Real-time dashboard with Streamlit
- Query and filter by user (via CLI)
- Export logs to CSV (via CLI)
- Docker support for local reproducibility
- Access control: view-only after submission

---

## Team & Contributions

| Name                   | Role & Contribution                                                   |
|------------------------|------------------------------------------------------------------------|
| Piangpim CHANCHARUNEE | Team Lead, Infra Designer, CLI author, Streamlit UI, Firebase setup |
| Kaushnav ROY          | Backend Research, Firebase Firestore Strategy                        |
| Hanqi YANG            | Streamlit App Deployment (Streamlit Cloud)                           |
| Ming GAO              | Dockerfile Author, Containerization                                  |
| I-Hsun LU             | Project Manager, README + spec.md author                             |

---

## CLI Tools

Located in the `/cli/` folder. Run with `python` from the root directory.

### Submit an Experiment
```bash
python cli/upload_experiment.py   --email "kiki@example.com"   --name "Transformer Run"   --params "{"lr": 0.001}"   --results "{"acc": 0.92}"   --type "NLP"   --data "WikiText"   --status "Success"   --notes "First baseline"
```

### Download All Experiments
```bash
python cli/download_experiment.py --output all_experiments.csv
```

### Filter by User
```bash
python cli/get_submissions_from_user.py --email kiki@example.com --output user.csv
```

---

## Firebase Setup

> Required for both CLI and Streamlit.

1. Go to [Firebase Console](https://console.firebase.google.com/), create a project.
2. Enable Realtime Database.
3. Navigate to **Project Settings > Service Accounts**.
4. Generate a new private key: save it as `firebaseKey.json`.
5. Place the key at project root or inside `.streamlit/secrets.toml`.

```toml
# Example .streamlit/secrets.toml
firebase_key = "your_key_path.json"
```

Do NOT commit this file to GitHub.

---

## Run Locally (with Docker)

### 1. Clone & Build
```bash
git clone https://github.com/YANG-KIKI/MLOPS-ml-experiment-sharing.git
cd MLOPS-ml-experiment-sharing
docker build -t mlops-dashboard .
```

### 2. Run Container
```bash
docker run -p 8501:8501 -v $PWD/.streamlit:/app/.streamlit mlops-dashboard
```

Or without Docker:
```bash
pip install -r requirements.txt
streamlit run streamlit.py
```

---

## Deployed App

Try it here: [Hosted App on Streamlit Cloud](https://ml-experiment-sharing-mlops.streamlit.app/)

---

## Acknowledgements

Thanks to the MLOps course by Joachim Zentici at CentraleSupélec / ESSEC.

---

## License

MIT License. Feel free to fork, clone, and adapt!
