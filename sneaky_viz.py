import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import polars as pl
    from altair.datasets import data

    return (data,)


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
def _():
    return


if __name__ == "__main__":
    app.run()
