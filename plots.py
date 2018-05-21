import altair as alt
import pandas as pd

DATA_FILE = "data/meetings.csv"
OUTPUT_FILE = "plots.html"

def main() -> None:
    """
    Creates some plots of the CSA meeting data and saves the plots to the
    output html file.
    """
    data = pd.read_csv(DATA_FILE)

    attendance_chart = alt.Chart(data).mark_circle().encode(
        x="Date:T",
        y="Attendees",
        color="Type",
        tooltip="Meeting"
    ).interactive()

    histogram = alt.Chart(data).mark_bar().encode(
        x="Year",
        y="count()",
        color="Type",
        tooltip="Meeting"
    )

    charts = attendance_chart & histogram

    charts.save(OUTPUT_FILE)

if __name__ == "__main__":
    main()
