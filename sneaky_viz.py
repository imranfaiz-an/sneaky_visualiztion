import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import polars as pl
    from altair.datasets import data
    from datetime import datetime

    return alt, data


@app.cell
def _(data):
    movies_df = data.movies()
    return (movies_df,)


@app.cell
def _(movies_df):
    movies_df
    return


@app.cell
def _(movies_df):
    movies_df.select("Release Date").max()
    return


@app.cell
def _(alt, movies_df):
    movies_chart = alt.Chart(movies_df)
    movies_chart.ma
    return


@app.cell
def _(alt, movies_df):
    # replace _df with your data source
    _chart = (
        alt.Chart(movies_df)
        .mark_bar()
        .encode(
            x=alt.X(field='US DVD Sales', type='quantitative'),
            y=alt.Y(field='Worldwide Gross', type='quantitative'),
            tooltip=[
                alt.Tooltip(field='US DVD Sales', format=',.0f'),
                alt.Tooltip(field='Worldwide Gross', format=',.0f')
            ]
        )
        .properties(
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': False
                }
            }
        )
    )
    _chart
    return


@app.cell
def _(alt, movies_df):
    # replace _df with your data source
    _chart = (
        alt.Chart(movies_df)
        .mark_bar(color="orange")
        .encode(
            x=alt.X(field='Major Genre', type='nominal'),
            y=alt.Y(field='Rotten Tomatoes Rating', type='quantitative', aggregate='sum', title="Total Rotten Tomato Rating"),
            tooltip=[
                alt.Tooltip(field='Major Genre'),
                alt.Tooltip(field='Rotten Tomatoes Ratings', aggregate='sum', format=',.0f')
            ]
        )
        .properties(
            title="Genres and Ratings 😈",
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': False,
                    'labelAngle': 10,
                }
            }
        )
    )
    _chart
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
