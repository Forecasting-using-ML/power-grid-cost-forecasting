"""Methods to scrape files from the internet."""
import os
import requests
import pandas as pd
from tqdm import tqdm


def get_zip_file(
    endpoint: str,
    date: pd.Timestamp,
    output_dir: str
) -> None:
    """
    Query and save to disk data from the NYISO.

    Args:
        endpoint: the endpoint to format with a date time
        date: the date of the archived data to query
        output_dir: the directory to store the zip file in

    Returns:
        None

    """
    # make the build directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # format the endpoint with the given date
    url = endpoint.format(date.strftime('%Y%m%d'))
    # extract the filename from the URL
    file_name = url.split('/')[-1]
    # fetch the raw zip file data
    data = requests.get(url).content
    # write the bytes to disk
    with open('{}/{}'.format(output_dir, file_name), 'wb') as data_file:
        data_file.write(data)


def get_zip_files(
    endpoint: str,
    start: pd.Timestamp,
    finish: pd.Timestamp,
    output_dir: str
) -> None:
    """
    Query and save to disk data from the NYISO in a range of dates.

    Args:
        start: the start date of the archived data to query
        finish: the finish date of the archived data to query
        output_dir: the directory to store the zip files in

    Returns:
        None

    """
    # create a date range of the first days in each month
    date_range = pd.date_range(start, finish, freq='MS')
    # iterate over the first day in each month
    for date in tqdm(date_range, unit='dataset'):
        # query the data from the NY servers
        get_zip_file(endpoint, date, output_dir)


# explicitly define the outward facing API of this module
__all__ = [
    get_zip_file.__name__,
    get_zip_files.__name__,
]
