import altair as alt

def create_charts(data) -> alt.Chart:
    """
    Creates some plots of the CSA meeting data and saves the plots to the
    output html file.
    """
    brush = alt.selection(type="multi", encodings=['x'])

    attendance_chart = (alt.Chart(data).mark_circle().encode(
        alt.X("Date:T", timeUnit="month"),
        y="count():O",
        color="Year"
    )).transform_filter(brush.ref()) + (alt.Chart(data).mark_line(
            opacity=0.4
        ).encode(
        alt.X("Date:T", timeUnit="month"),
        y="count():O",
        color="Year"
    )).transform_filter(brush.ref())

    yearly_summary = alt.Chart(data).mark_bar().encode(
        x="Year",
        y="count()"
    ).transform_filter(brush.ref())

    attendance_monthly_summary = alt.Chart(data).mark_bar().encode(
        alt.X("Date:T", timeUnit="month"),
        y="mean(Attendees)"
    ).transform_filter(brush.ref())

    attendance_yearly_summary = alt.Chart(data).mark_bar().encode(
        x="Year",
        y="mean(Attendees):Q"
    ).transform_filter(brush.ref())

    attendance_histogram = alt.Chart(data).mark_bar().encode(
        alt.X("Attendees:Q", bin=True),
        y="count()",
        color="Type",
        tooltip="Meeting"
    ).transform_filter(brush.ref())

    type_by_year = alt.Chart(data).mark_bar().encode(
        x="Type:N",
        y="count()",
        color="Year",
        opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.4))
    ).properties(
        selection=brush
    )

    charts = ((attendance_chart | yearly_summary | attendance_histogram) & (attendance_monthly_summary | attendance_yearly_summary | type_by_year))

    return charts
