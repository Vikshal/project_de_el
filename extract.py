import requests
import pandas as pd

def extract(url: str, timeout: int = 60) -> pd.DataFrame:
    data = []
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError:
        print("HTTPError")
    except requests.exceptions.JSONDecodeError:
        print("JSONDecodeError")
    except requests.RequestException as e:
        print(f"Error: {e}")

    return pd.DataFrame(data)

def save_to_csv(df:pd.DataFrame, path:str) -> None:
    if df.empty:
        print("No data")
        return
    try:
        df.to_csv(path, index=False, encoding="UTF-8")
        print(f"data saved successfully in the {path}")
    except PermissionError:
        print("No access")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    df = extract("https://jsonplaceholder.typicode.com/posts")
    print(df)
    save_to_csv(df, "extract_to_csv.csv")
