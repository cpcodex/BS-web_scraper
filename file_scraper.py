from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()
    # initiate beautifulsoup
    soup = BeautifulSoup(content, "lxml")
    course_html_tags = soup.find_all("h5")
    # iterate over course tags
    for course in course_html_tags:
        print(course.text)


with open("home.html", "r") as html_file:
    content = html_file.read()
    # initiate beautifulsoup
    soup = BeautifulSoup(content, "lxml")
    # define location to scarpe
    course_cards = soup.find_all("div", class_="card")
    # iterate over items within specified html class
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        # print results

        print(f"{course_name} costs {course_price}")
