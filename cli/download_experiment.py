import argparse
import pandas as pd
from firebase_utils import init_firebase, get_all_submissions

# Export the database

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="optional CSV filename")

    args = parser.parse_args()
    init_firebase()

    submissions = get_all_submissions()

    if not submissions:
        print("No experiments found.")
        return

    df = pd.DataFrame(submissions)

    print("Total experiments:", len(df))
    print(df[["experiment_name", "status", "submitted_at"]])

    if args.output:
        df.to_csv(args.output, index=False)
        print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
