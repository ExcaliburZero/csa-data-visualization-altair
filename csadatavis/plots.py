import altair as alt
import pandas as pd

def create_charts(data: pd.DataFrame) -> alt.Chart:
    """
    Creates some plots of the CSA meeting data and returns the resulting chart.
    """
    brush = alt.selection(type="multi", encodings=['x'])

    monthly_summary = create_monthly_summary(data, brush)
    yearly_summary = create_yearly_summary(data, brush)

    attendance_monthly_summary = create_attendance_monthly_summary(data, brush)
    attendance_yearly_summary = create_attendance_yearly_summary(data, brush)

    attendance_histogram = create_attendance_histogram(data, brush)
    meeting_type_summary = create_meeting_type_summary(data, brush)

    charts = ((monthly_summary | yearly_summary | attendance_histogram) & (attendance_monthly_summary | attendance_yearly_summary | meeting_type_summary))

    return charts

def create_monthly_summary(data: pd.DataFrame, brush: alt.selection) -> alt.Chart:
    """
    Creates a summary of the number of meetings by month broken down by
    academic year.

    Uses a scatter plot with a line plot overlayed in order to make it easier
    to see how the meeting count differs between years. Ideally the line would
    jump down to zero for months without any meetings, but I am unsure how to
    implement this in Altair.
    """
    monthly_summary = alt.Chart(data).encode(
        alt.X("Date:T", timeUnit="month"),
        y="count():O",
        color="Year"
    ).transform_filter(brush.ref())

    points = monthly_summary.mark_circle()
    lines = monthly_summary.mark_line(opacity=0.4)

    return points + lines

def create_yearly_summary(data: pd.DataFrame, brush: alt.selection) -> alt.Chart:
    """
    Creates a bar chart that summarizes of the number of meetings by academic
    year.
    """
    return alt.Chart(data).mark_bar().encode(
            x="Year",
            y="count()"
        ).transform_filter(brush.ref())

def create_attendance_monthly_summary(data: pd.DataFrame, brush: alt.selection) -> alt.Chart:
    """
    Creates a bar chart of the average meeting attendance by month.

    It averages together over all of the years in order to give a general idea
    of how attendance varies by month.
    """
    return alt.Chart(data).mark_bar().encode(
            alt.X("Date:T", timeUnit="month"),
            y="mean(Attendees)"
        ).transform_filter(brush.ref())

def create_attendance_yearly_summary(data: pd.DataFrame, brush: alt.selection) -> alt.Chart:
    """
    Creates a bar chart of the average meeting attendance by year.
    """
    return alt.Chart(data).mark_bar().encode(
            x="Year",
            y="mean(Attendees):Q"
        ).transform_filter(brush.ref())

def create_attendance_histogram(data: pd.DataFrame, brush: alt.selection) -> alt.Chart:
    """
    Creates a histogram that shows the distribution of meeting attendance along
    with color information showing how the different types of meetings
    correspond with attendance.
    """
    return alt.Chart(data).mark_bar().encode(
            alt.X("Attendees:Q", bin=True),
            y="count()",
            color="Type",
            tooltip="Meeting"
        ).transform_filter(brush.ref())

def create_meeting_type_summary(data: pd.DataFrame, brush: alt.selection) -> alt.Chart:
    """
    Creates a bar chart of the number of each different type of meeting broken
    down by year.

    Also allows the user to filter down all of the other plots to specific
    meeting types.
    """
    return alt.Chart(data).mark_bar().encode(
            x="Type:N",
            y="count()",
            color="Year",
            opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.4))
        ).properties(
            selection=brush
        )
