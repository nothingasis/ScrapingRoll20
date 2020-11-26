try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import re
import requests
import os

def download_file(url, filename='', foldername='misc', copy=0):
    try:
        if os.path.isdir(foldername):
            pass
        else:
            os.makedirs(foldername)

        if os.path.isfile(foldername + "/" + filename):
            copy = copy + 1
            filename = filename + str(copy)
            print ("File exist... renaming to: ", filename)
            download_file(url, filename=filename, foldername=foldername, copy=copy)
        else:
            pass
                
        # So that requests saves the file into the right folder...
        # append the foldername to the filename
        filename = foldername + "/" + filename
        print("Downloading ", filename, " from: ", url)
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None

# Open our asset library html file
with open("assetLibrary.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    # Traverse through each collapsible folder in the side-pane
    for folder in soup.find_all("li", {"class": "dd-folder"}):
        # Get the folder name.
        folder_name = folder.find("div", {"class": "folder-title"}).text

        # Get all the items inside the folder
        listItems = folder.find_all("li", {"class": "library-item"})
        for item in listItems:
            # Get the filename
            name = item.find("div", {"class": "namecontainer"})
            name = ("{0}".format(name.text))

            # Get the file url with regex
            regex = r"data-fullsizeurl=\"(https:\/\/s3\.amazonaws\.com\/files\.d20\.io\/marketplace\/\d+\/[\d\w-]+\/max.png\?\d+)\""
            test_str = str(item)
            matches = re.finditer(regex, test_str)
            for matchNum, match in enumerate(matches, start=1):
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    url= ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                    download_file(url=url, filename=name, foldername=folder_name)
