# Predict Future Sales

Final project for course: [How to Win a Data Science Competition: Learn from Top Kagglers](https://www.coursera.org/learn/competitive-data-science).

Kaggle [competition](https://www.kaggle.com/c/competitive-data-science-predict-future-sales).

Best result public/private: $0.995356$/$0.995798$.

## To reviewers

### Running order

In order to get my final submission:
1. 2.0-db-creating-dataset.ipynb
2. 1.0-db-EDA.ipynb
3. 4.0-db-text-features.ipynb
4. 5.0-db-lgb.ipynb
5. 7.0-db-ridge.ipynb
6. 8.0-db-stacking.ipynb

Some comments:
* The first notebook you should run have number of two in logical sense. We start solving task with investigation. In notebook 1 I also explore some results of notebook 2.
* Baseline model is not needed to create final solution.
* XGBoost model didn't contribute to final stacking because of too long computations.
* You can also read src files, class `TimeSeriesGroupSplit` helped me a lot.

### Reading order

In order to understand the logic:
1. 1.0-db-EDA.ipynb (before train exploration)
2. 2.0-db-creating-dataset.ipynb
3. 1.0-db-EDA.ipynb (after train exploration)
4. 4.0-db-text-features.ipynb
5. 5.0-db-lgb.ipynb
6. 7.0-db-ridge.ipynb
7. 8.0-db-stacking.ipynb

## Development

To install dependencies:
```bash
conda create --name <env> --file requirements.txt
```

To download the data you should enter the environment and place the config of Kaggle according to [documentation](https://github.com/Kaggle/kaggle-api). After this run:
```bash
snakemake data --cores 1
```
This will create all data folders and download competition data into data/raw.


## Project structure

------------

    ├── Snakefile           <- Snakefile with commands like `snakemake data` or `snakemake train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Documentation for the project
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `conda list -e > requirements.txt`
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        └──utils          <- Useful functions and classes for all project
