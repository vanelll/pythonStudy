from flask import Flask, render_template, request, Response
from bs4 import BeautifulSoup

app = Flask('ddong')


app.run(host="0.0.0.0", debug=True)