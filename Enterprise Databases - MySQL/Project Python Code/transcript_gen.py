from faker import Faker
import random

fake = Faker()

grades = ["A", "A-", "B+", "B", "B-", "C", "C-", "F"]
degrees = [
    "Biology",
    "Accounting",
    "Psychology",
    "Computer Science",
    "Liberal Arts",
    "Art",
    "Communications",
    "Business",
    "Mathematics",
    "Chemistry",
    "Physics",
    "Engineering",
    "History",
    "Fashion",
    "Statistics",
    "Physical Educations",
    "Education",
    "Literature",
    "English",
    "Law",
    "Economics",
    "Geography",
    "Urban Studies",
    "Astronomy",
    "Information Systems",
    "Computer science"]

degree_type = ["Bachelor Degree", "Graduate Degree", "Associate Degree"]

season = ["Spring ", "Fall ", "Summer "]


def randscript(UID):
    my_dict = {}
    my_dict["first_name"] = fake.first_name()
    my_dict["last_name"] = fake.last_name()
    my_dict["UID"] = UID
    geo_lat = (random.randint(-821244, -811250)) / 10000.0
    my_dict["geo_lat"] = geo_lat
    geo_long = (random.randint(411359, 413552)) / 10000.0
    my_dict["geo_long"] = geo_long

    my_transcript = {}
    my_transcript["School"] = "Cleveland State University"
    my_transcript["Degree"] = random.choice(degrees)
    my_transcript["Program"] = random.choice(degree_type) + " in " + my_transcript["Degree"]
    my_transcript["GPA"] = round(random.uniform(1.5, 4.0), 2)
    my_transcript["Grad_Season"] = random.choice(season)
    my_transcript["Grad_Year"] = (random.randint(2000, 2020))

    classes = []
    for i in range(0, 31):
        my_classes = {}
        my_classes["Department"] = random.choice(degrees).upper()[0:3]
        my_classes["Code"] = random.randint(100, 699)
        my_classes["Description"] = fake.text(max_nb_chars=25)[:-1]
        my_classes["Grade"] = random.choice(grades)
        my_classes["Season"] = random.choice(season)
        my_classes["Year"] = random.randint(my_transcript["Grad_Year"]-5, my_transcript["Grad_Year"])
        classes.append(my_classes)

    my_transcript["Classes"] = classes
    my_dict["Transcript"] = my_transcript
    return my_dict
