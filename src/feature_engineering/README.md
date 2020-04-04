# Feature Engineering

[feature-engineering.ipynb](feature-engineering.ipynb) loads the fuel output
data and hourly price data and engineers a single dataframe
([dataset.gz](dataset.gz)) with aligned timestamps.

## Train Test

[train-test.ipynb](train-test.ipynb) splits the dataframe in
[dataset.gz](dataset.gz) into separate train ([train.gz](train.gz)) and test
([test.gz](test.gz)) datasets. The train dataset contains data before Jan. 1,
2018 and the test dataset contains all the data after Jan. 1 2018.

## Visualize

[visualize.ipynb](visualize.ipynb) visualizes the individual curves in
[train.gz](train.gz) and [test.gz](test.gz).
