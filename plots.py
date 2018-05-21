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

    yearly_summary = alt.Chart(data).mark_bar().encode(
        x="Year",
        y="count()",
        color="Type"
    )

    monthly_summary = alt.Chart(data).mark_bar().encode(
        alt.X("Date:T", timeUnit="month"),
        y="count()",
        color="Type"
    )

    charts = (attendance_chart | yearly_summary) & (monthly_summary)

    charts.save(OUTPUT_FILE)

if __name__ == "__main__":
    main()
