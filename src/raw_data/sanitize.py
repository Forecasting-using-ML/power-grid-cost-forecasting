"""Methods to sanitize raw data."""
import os
import pandas as pd
from tqdm import tqdm
from zipfile import ZipFile


def extract_dataframe(zip_file: ZipFile) -> pd.DataFrame:
    """
    Extract a data-frame from a zip file of homogeneous .csv files.

    Args:
        zip_file: the zip file to extract a data-frame from

    Returns:
        a single data-frame containing all the records in the .csv files

    """
    dfs = []
    # iterate over the filenames in the ZipFile
    for filename in zip_file.namelist():
        # ignore non .csv files
        if '.csv' not in filename:
            continue
        # load the data-frame from the zip file. assume a date time in the
        # 'Time Stamp' column. use inference to determine the stamp format and
        # speedup the date-time parsing by 5-10x
        dfs += [pd.read_csv(
            zip_file.open(filename),
            parse_dates=['Time Stamp'],
            infer_datetime_format=True,
        )]

    return pd.concat(dfs)


def extract_dataframes(directory: str) -> pd.DataFrame:
    """
    Extract data-frames from a directory of homogeneous zip files.

    Args:
        directory: the directory containing zip files with homogeneous
        .csv file in them

    Returns:
        a single data-frame from all the data in the directory

    """
    # a list to store the data-frame objects in
    dfs = []
    # iterate over the zip files in the given directory
    filenames = sorted(os.listdir(directory))
    for file in tqdm(filenames, unit='zip file'):
        # ignore non zip files
        if '.zip' not in file:
            continue
        # open the zip file and create a data-frame from it
        with ZipFile('{}/{}'.format(directory, file)) as zip_file:
            dfs += [extract_dataframe(zip_file)]

    return pd.concat(dfs)


# explicitly define the outward facing API of this module
__all__ = [
    extract_dataframe.__name__,
    extract_dataframes.__name__,
]
