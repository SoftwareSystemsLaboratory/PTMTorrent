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
def downloadRepo(link, name):

    # Check to see if it was already cloned or not
    if (os.path.exists('../repos/'+name)):
        print(name + ' was already cloned!')
    
    # Clone the file
    else:
        # Regex to find base directory of repo
        print(link)
        match = re.match('https://github.com/[a-zA-z_.-]+/[a-zA-z_.-]+$|/', link)
        print(match)

        if match:
            git.Repo.clone_from(match.group(0), '../repos/' + name) # Clone the repos normally

        else:
            print('Faulty GitHub Link!!!')

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
        downloadRepo(getGitHub(soup), x[:-5])

        # Create general JSON
        generalJSON(soup)

        # Create specific JSON
        specificJSON(soup)
