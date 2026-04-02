from flask import Flask, render_template

app = Flask(__name__)

# 🔥 CONFIG - YOU CAN MODIFY THIS ANYTIME  - Ramesh -bhu - luvly - happy
SECTIONS = {
    "Docker": {
        "Day 4 Revision": "docker-day4-revision.html",
        "Day 3 Revision": "docker-day3-revision.html",
        "Day 2 Revision": "docker-day2-revision.html",
        "Day 1 Revision": "docker-day1-revision.html",
        "Mastery Tracker": "docker-mastery-tracker.html",
    },
    "Kubernetes": {
        "SRE Dashboard": "k8s-sre-dashboard.html",
    },
    "Python": {
        "SRE Tracker": "sre_python_tracker.html",
    }
}

@app.route("/")
def home():
    return render_template("layout.html", sections=SECTIONS)

@app.route("/view/<section>/<subsection>")

# editing the code to check wether the cahges are reflecting or not 
def view(section, subsection):
    file_name = SECTIONS.get(section, {}).get(subsection)
    return render_template("viewer.html", file=file_name, sections=SECTIONS)

if __name__ == "__main__":
    app.run(debug=True)

# changing the code to validate
