import argparse
import pandas as pd
from firebase_utils import init_firebase, get_all_submissions

# Get all experiments from one user

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", required=True)
    parser.add_argument("--output", help="optional CSV file")

    args = parser.parse_args()
    init_firebase()

    all_data = get_all_submissions()
    user_data = [item for item in all_data if item.get("email") == args.email]

    if not user_data:
        print(f"No data found for {args.email}")
        return

    df = pd.DataFrame(user_data)
    print(f"{len(df)} experiment(s) found for {args.email}")
    print(df[["experiment_name", "status", "submitted_at"]])

    if args.output:
        df.to_csv(args.output, index=False)
        print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
