try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import re

with open("assetLibrary.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # print soup.find_all(match_class(["feeditemcontent", "cxfeeditemcontent"]))
    for folder in soup.find_all("li", {"class": "dd-folder"}):
        # Get the parent folder.
        folder_name = folder.find("div", {"class": "folder-title"})
        print("Folder:", folder_name.text)

        # Get all the children
        listItems = folder.find_all("li", {"class": "library-item"})
        for item in listItems:
            name = item.find("div", {"class": "namecontainer"})
            print ("{0}".format(name.text))
            regex = r"data-fullsizeurl=\"(https:\/\/s3\.amazonaws\.com\/files\.d20\.io\/marketplace\/\d+\/[\d\w-]+\/max.png\?\d+)\""

            test_str = "data-fullsizeurl=\"https://s3.amazonaws.com/files.d20.io/marketplace/14665/l6B57dHOGekSHDGEnE4UGg/max.png?1366969146\""

            matches = re.finditer(regex, test_str)

            for matchNum, match in enumerate(matches, start=1):
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    url= ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                    print(url)