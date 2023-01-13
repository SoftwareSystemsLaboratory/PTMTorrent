# 2a_parseList.py
# Author: Taylor R. Schorlemmer
# Parses through each of the model HTML pages


# Imports
from bs4 import BeautifulSoup
import git
import os
import re


# Load manifest file
model_manifest_path = '../html/manifest.txt'
with open(model_manifest_path, 'r') as file:
    manifest = file.readlines()

# Strip newlines
manifest = [x.strip() for x in manifest]






# Function to retrieve github link
def getGitHub(soup):
    try:
        return soup.find(string='View on Github').parent.parent['href']
    except:
        return ''

# Function to retrieve colab link
def getColab(soup):
    try:
        return soup.find(string='Open on Google Colab').parent.parent['href']
    except:
        return ''

# Function to retrieve demo link
def getDemo(soup):
    try:
        return soup.find(string='Open Model Demo').parent.parent['href']
    except:
        return ''

# Get the github, colab, and demo links
def getLinks(soup):
    return (getGitHub(soup), getColab(soup), getDemo(soup))

# Download the specific repository to the ../repos/ folder
def downloadRepo(link):

    # Regex to find base directory of repo
    match = re.match('(https://github.com/)([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)($|/)', link)

    # Check to see if there was a valid github link
    if match:

        # Pull URL for GitHub repo
        github_url = match.group(0)

        # Create path to store the repo
        repo_path = '../repos/' + match.group(2).replace('/','_')

        # Check to see if it was already cloned or not
        if (os.path.exists(repo_path)):
            print(repo_path + ' was already cloned!')
    
        # If not, clone the repo
        else:
            print('Cloning ' + github_url)
            # git.Repo.clone_from(github_url, repo_path) # Clone the repos normally
            # git.Repo.clone_from(github_url, repo_path, multi_options=['--depth=1']) # Clone with --depth=1
            git.Repo.clone_from(github_url, repo_path, multi_options=['--bare']) # Clone with --bare



    
    # Print a warnig if the link was strange
    else:
        print('***FAULTY GITHUB LINK***')

# Write to the general JSON to the ../json/general.json using provided soup
def generalJSON(soup):
    pass

# Write to the specific JSON to the ../json/specific.json using provided soup
def specificJSON(soup):
    pass







# Iterate through all html files
for x in manifest:
    print('========================================')
    print(x)

    with open('../html/modelPages/' + x, 'r') as file:
        
        # Convert to soup object
        soup = BeautifulSoup(file.read(), 'html.parser')

        # Download Repo
        gitHub_link = getGitHub(soup)
        print('Downloading repository at ' + gitHub_link)
        downloadRepo(gitHub_link)

        # Create general JSON
        generalJSON(soup)

        # Create specific JSON
        specificJSON(soup)
