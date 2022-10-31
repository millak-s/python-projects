import requests
from bs4 import BeautifulSoup
from write_csv import csv


def web_scrapper(url, data=None):
    if data is None:
        data = []

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_list = soup.find_all(
        "div",
        class_="employer-job-listing-single premium-job box-shadow bg-white mb-3 p-3 job-spotlight job-listing job_position_featured grid",
    )

    for job_info in job_list:
        job = {}
        other_info = job_info.find_all("p", class_="text-muted")
        company_info = other_info[2].text.strip().split("·")
        date_line = other_info[0].text.strip().split("·")
        words = ["Expiré", "mois", "ans"]
        check = [True if w in date_line else False for w in words]

        if any(check):
            continue

        job["Job"] = job_info.find("h5").text.strip().replace(", ", "/")
        try:
            job["Date-line"] = date_line[1][-13:-1].replace(",", "")
        except IndexError:
            job["Date-line"] = "Not specified"

        job["Company"] = (
            "Not specified"
            if "Un Employeur" in company_info
            else company_info[0].strip()
        )

        job["Location"] = company_info[1].strip().replace(", ", "/")

        if "Non spécifié" in other_info[1]:
            job["Contract Type"] = "Not specified"
        else:
            job["Contract Type"] = other_info[1].text.split("·")[1].strip()

        job["Link"] = job_info.find("a")["href"]
        data.append(job)

    try:
        url = soup.find_all(class_="page-link")[-1]["href"]
    except KeyError:
        return
    web_scrapper(url, data)
    return data


url = "https://doojobs.net/search?page=1"
postings = web_scrapper(url)
csv("./doojobs.csv", postings)
