import pandas as pd

import plots

DATA_FILE = "data/meetings.csv"
OUTPUT_FILE = "plots.html"

def main() -> None:
    data = pd.read_csv(DATA_FILE)

    charts = plots.create_charts(data)

    charts.save(OUTPUT_FILE)

    print("Sucessfully created plot webpage at: " + OUTPUT_FILE)

if __name__ == "__main__":
    main()
