import argparse
from datetime import datetime
from firebase_utils import init_firebase, save_submission

# Submit an entry to the database

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--type", default="Other")
    parser.add_argument("--data", default="Other")
    parser.add_argument("--params", required=True)
    parser.add_argument("--results", required=True)
    parser.add_argument("--status", default="Success")
    parser.add_argument("--notes", default="")

    args = parser.parse_args()

    init_firebase()

    exp_data = {
        "email": args.email,
        "experiment_name": args.name,
        "experiment_type": args.type,
        "data_source": args.data,
        "parameters": args.params,
        "results": args.results,
        "status": args.status,
        "notes": args.notes if args.notes else "N/A",
        "submitted_at": datetime.utcnow().isoformat()
    }

    save_submission(args.email, exp_data)
    print("Experiment submitted!")

if __name__ == "__main__":
    main()
