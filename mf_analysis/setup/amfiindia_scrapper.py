import os
from datetime import timedelta, date
from multiprocessing.pool import ThreadPool
from pathlib import Path
from urllib.request import urlopen

from mf_analysis.api.controller import APP


def fetch_url(url):
    try:
        response = urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, e


def scrape(from_date, to_date, skipped_dates):
    link = "https://www.amfiindia.com/spages/NAVAll.txt"
    urls = []

    delta = to_date - from_date
    for i in range(delta.days + 1):
        calculated_date = from_date + timedelta(days=i)
        if calculated_date not in skipped_dates:
            calculated_url = link + "?t=" + calculated_date.strftime('%d%m%Y')
            file_path = os.path.join(APP.config['AMFI_SCRAPE_FOLDER'], calculated_url.split("t=")[1] + ".mfnav")
            if not Path(file_path).is_file():
                urls.append(calculated_url)
            else:
                print("File already downloaded: ", file_path)

    results = ThreadPool(20).imap_unordered(fetch_url, urls)
    for url, response_data, error in results:
        file_path = os.path.join(APP.config['AMFI_SCRAPE_FOLDER'], url.split("t=")[1] + ".mfnav")
        if error is None:
            with open(file_path, "wb") as file:
                file.write(response_data)
                print("Downloaded file from URL: ", url)
        else:
            print("Error fetching %r: %s" % (url, error))


scrape(date(2016, 4, 2), date(2018, 3, 13), [])
