# 2a_parseList.py
# Author: Taylor R. Schorlemmer
# Parses through each of the model HTML pages


import json
import os
import re
import sys

import git
from bs4 import BeautifulSoup
from jsonschema import validate


# Function to retrieve github link
def get_github_link(soup):
    try:
        return soup.find(string="View on Github").parent.parent["href"]
    except:
        return ""


# Function to retrieve colab link
def get_colab_link(soup):
    try:
        return soup.find(string="Open on Google Colab").parent.parent["href"]
    except:
        return ""


# Function to retrieve demo link
def get_demo_link(soup):
    try:
        return soup.find(string="Open Model Demo").parent.parent["href"]
    except:
        return ""


# Get the github, colab, and demo links
def get_links(soup):
    return (get_github_link(soup), get_colab_link(soup), get_demo_link(soup))


# Create a local repository location
def create_local_repo_path(link):
    match = match_github(link)
    return "../repos/" + match.group(2).replace("/", "_")


# Perform regex on raw github link
def match_github(link):
    regex_string = "(https://github.com/)([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)($|/)"
    return re.match(regex_string, link)


# Download the specific repository to the ../repos/ folder
def download_repo(link):

    # Perform regex matching on the link
    match = match_github(link)

    # Check to see if there was a valid github link
    if match:

        # Pull URL for GitHub repo
        github_url = match.group(0)

        # Create path to store the repo
        repo_path = create_local_repo_path(link)

        # Check to see if it was already cloned or not
        if os.path.exists(repo_path):
            print(repo_path + " was already cloned!")

        # If not, clone the repo
        else:
            print("Cloning " + github_url)
            # git.Repo.clone_from(github_url, repo_path) # Clone the repos normally
            # git.Repo.clone_from(github_url, repo_path, multi_options=['--depth=1']) # Clone with --depth=1
            git.Repo.clone_from(
                github_url, repo_path, multi_options=["--bare"]
            )  # Clone with --bare

    # Print a warnig if the link was strange
    else:
        print("***FAULTY GITHUB LINK***")


# returns the dictionary representing the general json
def gen_general_json(soup, ind):

    # offset used to seperate pytorch hub IDs from other hubs
    offset = 1000
    jumbotron = soup.find("div", attrs={"class": "jumbotron jumbotron-fluid"}).div

    with open("../html/model_urls.txt", "r") as file:

        x = {
            "id": offset + ind,
            "ModelHub": {"ModelHubName": "PyTorch Hub"},
            "ModelName": jumbotron.h1.string.strip(),
            "ModelOwner": jumbotron.div.div.p.string.strip()[3:],
            "ModelURL": file.readlines()[ind].strip(),
        }

    return x


# returns the dictionary representing the specific json
def gen_specific_json(soup, ind):

    jumbotron = soup.find("div", attrs={"class": "jumbotron jumbotron-fluid"}).div

    x = {
        "id": ind,
        "ModelName": jumbotron.h1.string.strip(),
        "Author": jumbotron.div.div.p.string.strip()[3:],
        "Summary": jumbotron.div.div.next_sibling.next_sibling.p.string.strip(),
        "GitHubLink": get_github_link(soup),
        "GitHubRepository": match_github(get_github_link(soup)).group(0),
        "LocalRepository": create_local_repo_path(get_github_link(soup)),
    }

    return x


# Load manifest file
model_manifest_path = "../html/manifest.txt"
with open(model_manifest_path, "r") as file:
    manifest = file.readlines()

# Strip newlines
manifest = [x.strip() for x in manifest]

# Arrays to hold each json entry
general_json = []
specific_json = []

# Iterate through all html files
for ind, x in enumerate(manifest):
    print("========================================")
    print(x)

    with open("../html/modelPages/" + x, "r") as file:

        # Convert to soup object
        soup = BeautifulSoup(file.read(), "html.parser")

        # Download Repo
        github_link = get_github_link(soup)
        print("Downloading repository at " + github_link)
        download_repo(github_link)

        # Create general JSON
        print("Parsing general JSON...")
        general_json.append(gen_general_json(soup, ind))

        # Create specific JSON
        print("Parsing specific JSON...")
        specific_json.append(gen_specific_json(soup, ind))


# Validate then save general json
try:
    # Validate the json before saving it
    # with open('../../schema.json') as schema:
    #     validate(instance=general_json, schema=json.loads(schema.read()))

    # Write JSON file
    general_path = "../json/general.json"
    print("Attempting to save general json to " + general_path)
    with open(general_path, "w") as file:
        file.write(json.dumps(general_json, indent=4))

except:
    print("***ERROR WITH GENERAL JSON - FILE NOT SAVED***")


# Validate then save specific json
try:
    # Validate the json before saving it
    with open("../PHTorrent.schema.json") as schema:
        validate(instance=specific_json, schema=json.loads(schema.read()))

    # Write JSON file
    specific_path = "../json/specific.json"
    print("Attempting to save specific json to " + specific_path)
    with open(specific_path, "w") as file:
        file.write(json.dumps(specific_json, indent=4))

except:
    print("***ERROR WITH SPECIFIC JSON - FILE NOT SAVED***")
