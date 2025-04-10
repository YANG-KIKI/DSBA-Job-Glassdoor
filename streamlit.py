import streamlit as st
import pandas as pd
from datetime import datetime
from dateutil import parser

# Firebase functions
from firebase_utils import (
    init_firebase,
    save_submission,
    has_valid_submission,
    get_all_submissions,
)

# Setup the app
st.set_page_config(layout="wide")
init_firebase()
st.title("Experiment Submission & Tracker")

# Submission form
email = st.text_input("Enter your email")
if email:
    valid = has_valid_submission(email)
    show_submission_form = False

    if valid:
        st.success("You have access to the experiment log.")
        show_submission_form = st.checkbox("Submit another experiment")

    if not valid:
        st.warning("You don’t currently have access to the experiment log. Please submit a new experiment.")
        show_submission_form = True

    if show_submission_form:
        st.subheader("Submit a New Experiment")

        experiment_name = st.text_input("Experiment Name (e.g. CNN-v1)")
        experiment_type = st.selectbox("Experiment Type", ["Classification", "Regression", "Clustering", "Other"])
        data_source = st.selectbox("Data Source", ["Kaggle", "Internal Dataset", "Simulated", "Other"])
        parameters = st.text_area("Key Parameters (e.g. model type, hyperparams)")
        results = st.text_area("Results Summary (e.g. accuracy, loss)")
        status = st.selectbox("Status", ["Success", "Failed", "In Progress"])
        notes = st.text_area("Extra Notes (optional)")

        if st.button("Submit"):
            if not (experiment_name and parameters and results):
                st.error("Please fill in all required fields: experiment name, parameters, and results.")
            else:
                data = {
                    "email": email,
                    "experiment_name": experiment_name,
                    "experiment_type": experiment_type,
                    "data_source": data_source,
                    "parameters": parameters,
                    "results": results,
                    "status": status,
                    "notes": notes or "N/A",
                    "submitted_at": datetime.utcnow().isoformat()
                }

                save_submission(email, data)
                st.success("Thanks! Your experiment was submitted and you now have access to the log.")
                st.rerun()

    # Show the submissions if user has access
    if valid:
        st.subheader("View Submitted Experiments")
        submissions = get_all_submissions()
    
        if submissions:
            all_entries = []
    
            # Sort the submissions by date
            submissions = sorted(
                submissions,
                key=lambda x: parser.parse(x["submitted_at"]) if "submitted_at" in x else datetime.min
            )
    
            for entry in submissions:
                all_entries.append({
                    "Experiment": entry.get("experiment_name", "N/A"),
                    "Type": entry.get("experiment_type", "N/A"),
                    "Data Source": entry.get("data_source", "N/A"),
                    "Parameters": entry.get("parameters", "N/A"),
                    "Results": entry.get("results", "N/A"),
                    "Status": entry.get("status", "N/A"),
                    "Notes": entry.get("notes", "N/A"),
                    "Submitted": entry.get("submitted_at", "N/A"),
                })
    
            df = pd.DataFrame(all_entries)
            st.dataframe(df, use_container_width=True)
    
        else:
            st.info("No submissions yet.")
