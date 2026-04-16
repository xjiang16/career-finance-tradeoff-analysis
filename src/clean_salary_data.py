from pathlib import Path
import pandas as pd

USD_TO_CNY = 6.9


def annualize_salary(row: pd.Series, value_col: str) -> float:
    value = row[value_col]
    if row["period"] == "month":
        return value * row["pay_months"]
    if row["period"] == "year":
        return value
    raise ValueError(f"Unexpected period: {row['period']}")


def to_usd(amount: float, currency: str) -> float:
    if currency == "USD":
        return amount
    if currency == "CNY":
        return amount / USD_TO_CNY
    raise ValueError(f"Unexpected currency: {currency}")


def to_cny(amount: float, currency: str) -> float:
    if currency == "CNY":
        return amount
    if currency == "USD":
        return amount * USD_TO_CNY
    raise ValueError(f"Unexpected currency: {currency}")


def clean_salary_data(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    required_cols = [
        "location",
        "role",
        "experience_level",
        "salary_low",
        "salary_high",
        "period",
        "currency",
        "pay_months",
        "source",
    ]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    cleaned = df.copy()

    cleaned["salary_low_annual_local"] = cleaned.apply(
        lambda row: annualize_salary(row, "salary_low"), axis=1
    )
    cleaned["salary_high_annual_local"] = cleaned.apply(
        lambda row: annualize_salary(row, "salary_high"), axis=1
    )

    cleaned["median_annual_local"] = (
                                             cleaned["salary_low_annual_local"] + cleaned["salary_high_annual_local"]
                                     ) / 2

    cleaned["median_annual_usd"] = cleaned.apply(
        lambda row: to_usd(row["median_annual_local"], row["currency"]), axis=1
    )
    cleaned["median_annual_cny"] = cleaned.apply(
        lambda row: to_cny(row["median_annual_local"], row["currency"]), axis=1
    )

    cleaned = cleaned.rename(
        columns={
            "currency": "currency_original",
            "period": "period_original",
            "salary_low": "salary_low_raw",
            "salary_high": "salary_high_raw",
        }
    )

    output_cols = [
        "location",
        "role",
        "experience_level",
        "source",
        "currency_original",
        "period_original",
        "pay_months",
        "salary_low_raw",
        "salary_high_raw",
        "salary_low_annual_local",
        "salary_high_annual_local",
        "median_annual_local",
        "median_annual_usd",
        "median_annual_cny",
    ]

    cleaned = cleaned[output_cols]

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(output_path, index=False)

    return cleaned


if __name__ == "__main__":
    result = clean_salary_data(
        "data/raw/salary_raw.csv",
        "data/processed/salary_cleaned.csv",
    )
    print(result)