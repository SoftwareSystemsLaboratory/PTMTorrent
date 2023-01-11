# 1a_getList.py
# Author: Taylor R. Schorlemmer
# Retrieves the base model list from the PyTorch Hub website


# Imports
import requests
from bs4 import BeautifulSoup

# Get HTML from the page that lists all the models
pth_models_url = 'https://pytorch.org/hub/research-models/compact'
pth_models_html = requests.get(pth_models_url).text

# Convert to a BS object
soup_pth = BeautifulSoup(pth_models_html, 'html.parser')

# Extract a list of all the compact model cards (still in html format)
model_list = soup_pth.find_all('div', 'col-md compact-hub-card-wrapper')

# Extract links to the pages for each model
model_url_extensions = [model.a['href'] for model in model_list]
