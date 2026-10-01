import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # OMP Yield Prediction - EDA

    ## Loading data

    We'll focus on OILPALM first
    """)
    return


@app.cell
def _():
    import pandas as pd
    from pathlib import Path

    data_dir = Path("data")

    # Load OILPALM data first
    try:
        oilpalm_df = pd.read_json(data_dir.joinpath("ds_data-OILPALM.json"))
    except Exception as e:
        print(f"could not read JSON file: {e}")

    return (oilpalm_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspect the data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Peek first 5 rows
    """)
    return


@app.cell
def _(oilpalm_df):
    oilpalm_df.head(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Observations:

    - The following columns contain missing values
      - `visDeficLCPK`
      - `LAI`
      - `trunkDiameter`
    - The following `str` type columns contain empty strings:
      - `canopyDev`
      - `soilAcidity`
    - `YEAR` is an int but will most likely need to be converted into a `datetime` object
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Get info on the DataFrame itself
    """)
    return


@app.cell
def _(oilpalm_df):
    oilpalm_df.info()
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Get summmary stats
    """)
    return


@app.cell
def _(oilpalm_df):
    oilpalm_df.describe()
    return


if __name__ == "__main__":
    app.run()
