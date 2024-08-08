import requests
from lxml import html
import mysql.connector

def fetch_job_description(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    
    # Define XPath expressions
    title_xpath = '/html/body/div[2]/div[1]/div/span/div[4]/div[5]/div[2]/div/section/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/h2/span/text()'
    description_xpath = '//*[@id="jobDescriptionText"]//text()'
    
    # Extract job title and description using XPath
    title = tree.xpath(title_xpath)
    description = tree.xpath(description_xpath)
    
    if title and description:
        # Join list of description texts into a single string
        description_text = '\n'.join(description).strip()
        return title[0].strip(), description_text
    else:
        raise ValueError("Unable to find job title or description on the page. Check the XPath expressions.")

def save_to_database(title, description):
    try:
        connection = mysql.connector.connect(
            host='*******',
            user='*******',     # Update with your MySQL username
            password='root', # Update with your MySQL password
            database='job_database'
        )
        cursor = connection.cursor()
        query = "INSERT INTO jobs (title, description) VALUES (%s, %s)"
        cursor.execute(query, (title, description))
        connection.commit()
        print("Save successful")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    url = input("Paste the URL: ").strip()
    try:
        title, description = fetch_job_description(url)
        print(f"Job Title: {title}")
        print(f"Job Description: {description[:200]}...")  # Print a preview of the description
        save = input("Save to database? [Y/N]: ").strip().lower()
        if save == 'y':
            save_to_database(title, description)
        else:
            print("Job not saved to database")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
