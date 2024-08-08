import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed"],
    search_term="engineer",
    location="Dallas, TX",
)
columns_returned = ["title","location", "job_url"]
columns_filtered = jobs[columns_returned]

print('Found {len(jobs)} jobs')
print(columns_filtered.columns.to_list())
print(columns_filtered.head())

export_path = "../data/CSV"
columns_filtered.to_csv(f"{export_path}/indeed.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)