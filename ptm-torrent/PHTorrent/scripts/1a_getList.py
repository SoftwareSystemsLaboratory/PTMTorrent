# 1a_getList.py
# Author: Taylor R. Schorlemmer
# Retrieves the base model list from the PyTorch Hub website


# Imports
import requests
from bs4 import BeautifulSoup

# Get HTML from the page that lists all the models
pt_base_url = "https://pytorch.org"
pth_model_list_url = "/hub/research-models/compact"
pth_model_list_html = requests.get(pt_base_url + pth_model_list_url).text

# Convert to a BS object
soup_pth = BeautifulSoup(pth_model_list_html, "html.parser")

# Extract a list of all the compact model cards (still in html format)
model_list = soup_pth.find_all("div", "col-md compact-hub-card-wrapper")

# Extract links to the pages for each model
model_urls = [model.a["href"] for model in model_list]

# Create full urls
full_model_urls = [pt_base_url + x for x in model_urls]

# Save url's to a file in ../html/
model_urls_path = "../html/model_urls.txt"
print("Saving model urls to " + model_urls_path)

with open(model_urls_path, "w") as file:
    for x in full_model_urls:
        file.write(x + "\n")

# Grab the html pages for each model
model_html_path = "../html/modelPages/"
print("Saving the html pages for each model in " + model_html_path)

model_html_list = [requests.get(x).text for x in full_model_urls]

# Save each of the pages in ../html/modelPages/
for ind, x in enumerate(model_html_list):
    with open(model_html_path + model_urls[ind][5:-1] + ".html", "w") as file:
        file.write(x)

# Create a manifest file in ../html/
model_manifest_path = "../html/manifest.txt"
print("Saving a manifest to " + model_manifest_path)

with open(model_manifest_path, "w") as file:
    for x in model_urls:
        file.write(x[5:-1] + ".html\n")
