from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {
    "python": [],
}


@app.route("/")
def home():
    return render_template("home.html", name="abcd")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.args("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/serch?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


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
