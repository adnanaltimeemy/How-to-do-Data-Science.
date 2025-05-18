import pandas as pd

def clean_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

if __name__ == "__main__":
    cleaned_df = clean_data("data/data.csv")
    print(cleaned_df.head())
    cleaned_df.to_csv("data/cleaned_data.csv", index=False)
    print("Data cleaned and saved to cleaned_data.csv")
    cleaned_df = clean_data("data/data.csv")
    print(cleaned_df.head())
    cleaned_df.to_csv("data/cleaned_data.csv", index=False)
    print("Data cleaned and saved to cleaned_data.csv")
    cleaned_df = clean_data("data/data.csv")
    print(cleaned_df.head())
    cleaned_df.to_csv("data/cleaned_data.csv", index=False)
    print("Data cleaned and saved to cleaned_data.csv")
    cleaned_df = clean_data("data/data.csv")
    print(cleaned_df.head())