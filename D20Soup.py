try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match

with open("assetLibrary.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # print soup.find_all(match_class(["feeditemcontent", "cxfeeditemcontent"]))
    for tag in soup.find_all("li", {"class": "library-item"}):
        name = tag.find("div", {"class": "namecontainer"})        
        print("Name: ", name)