from bs4 import BeautifulSoup
import requests
import time


def find_job():
    # create requests URL pathway
    html_text = requests.get("https://motionrecruitment.com/tech-jobs/python").text

    # create BS instance
    soup = BeautifulSoup(html_text, "lxml")
    # page items to be scraped
    jobs = soup.find_all("li", class_="JobItem_jobItem__IZ5bL")

    # iterate over items
    for index, job in enumerate(jobs):
        company_name = job.find("h2", class_="JobItem_title__mJtrY").text
        employment_type = job.find("b").text
        job_location = job.find("p").text
        more_info = job.a["href"]

        # write and save to file
        with open(f"posts/{index}.txt", "w") as f:
            f.write(f"Location: {job_location}\n")
            f.write(f"Job Title: {company_name}\n")
            f.write(f"Job type: {employment_type}\n")
            f.write(f"Job Description: https://motionrecruitment.com{more_info}\n")
        print(f"File Saved: {index}")

        # print results
        print(f"Location: {job_location}")
        print(f"Job Title: {company_name}")
        print(f"Job type: {employment_type}")
        print(f"Job Description: https://motionrecruitment.com{more_info}")
        print()


if __name__ == "__main__":
    find_job()
