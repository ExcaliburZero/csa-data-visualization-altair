import pandas as pd

from .plots import create_charts
from .rendering import render_webpage_string

DATA_FILE = "data/meetings.csv"
OUTPUT_FILE = "plots.html"

def main() -> None:
    data = pd.read_csv(DATA_FILE)

    charts = create_charts(data)
    vegalite_spec = charts.to_json()

    webpage_content = render_webpage_string(vegalite_spec)

    with open(OUTPUT_FILE, "w") as webpage_file:
        webpage_file.write(webpage_content)

        print("Sucessfully created plot webpage at: " + OUTPUT_FILE)

if __name__ == "__main__":
    main()
