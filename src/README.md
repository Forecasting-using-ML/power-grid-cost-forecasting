# National Grid Data

This package scrapes, engineers, and models a dataset of power grid data from
New York state.

## Raw Data

[raw_data](raw_data) contains packages to scrape and sanitize individual
datasets from several sources

## Feature Engineering

[feature_engineering](feature_engineering) contains modules to engineer a
machine learning dataset based on the data packages in [raw_data](raw_data).

## Modeling

[modeling](modeling) contains modules that attempt to correlate the
multivariate features to the price of energy.
