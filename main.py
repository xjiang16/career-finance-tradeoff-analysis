from src.clean_salary_data import clean_salary_data


def main() -> None:
    df = clean_salary_data(
        "data/raw/salary_raw.csv",
        "data/processed/salary_cleaned.csv",
    )

    print("\nCleaned salary data preview:\n")
    print(df.to_string(index=False))

    print("\nSummary by role:\n")
    print(df[["location", "role", "median_annual_usd", "median_annual_cny"]].to_string(index=False))


if __name__ == "__main__":
    main()