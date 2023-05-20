from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="abcd")


@app.route("/search")
def hello():
    return render_template("search.html")


app.run("0.0.0.0")


# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs
# from file import save_to_file

# keyword = input("What do you wnat to search for?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr
# save_to_file(keyword, jobs)


# file = open(f"{keyword}.csv", "w", encoding="utf-8")
# file.write("Position,Company,Location,URL\n")

# for job in jobs:
#     file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

# file.close()
