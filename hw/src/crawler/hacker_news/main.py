import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  order_by = request.args.get("order_by")
  if order_by == 'new':
      get_request = requests.get(new)
      sts = "new"
  else:
      get_request = requests.get(popular)
      sts = "popular"
  json = get_request.json()
  hits= json['hits']
  db[sts]= hits

  return render_template("index.html", hits=hits, sts=sts)

app.run(host="0.0.0.0")