import pandas as pd

INPUT_PATH = "data/jobposts.csv"
OUTPUT_PATH = "data/jobs_clean.csv"

def main():
    df = pd.read_csv(INPUT_PATH)
    print(df.columns)
    df = df[["Title", "JobDescription", "JobRequirment"]]

    df = df.dropna()
    df["full_text"] = (
        df["Title"].astype(str) + " "
        +
        df["JobDescription"].astype(str) + " "
        +
        df["JobRequirment"].astype(str)
    )

    df = df.reset_index(drop=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print("clean dataset saved:", df.shape)

if __name__ == "__main__":
    main()    
