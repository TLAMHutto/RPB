from jobspy import scrape_jobs

def main():
    # CLI starts
    keywords = input("Enter keywords: ")
    print("Keywords:", keywords)

    location = input("Enter Location: ")
    print("Location:", location)

    # Perform the job search using scrape_jobs function
    jobs = scrape_jobs(keywords=keywords, location=location)

    # Print the number of jobs returned and the job listings
    print(f"Number of jobs returned: {len(jobs)}")
    print("Job Listings:")
    for job in jobs:
        print(job)

if __name__ == "__main__":
    main()
