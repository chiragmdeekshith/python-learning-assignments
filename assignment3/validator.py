import re
from bs4 import BeautifulSoup


class HtmlFileRead:
    def __init__(self):
        print("HtmlFileRead object instantiated")

    # the following can be made static, but the question states to use an object instance
    def read_html_file_as_string(self):
        html_string = ""

        with open("assignment3\\html.html", "r") as html_file:
            html_string = html_file.read()

        return html_string


class HtmlValidator:
    def __init__(self):
        print("HtmlValidator object instantiated")
        self.htmlFileRead = HtmlFileRead()

    def validate_html_string(self):
        # get all tags
        html_string = self.htmlFileRead.read_html_file_as_string()
        beautiful_soup = BeautifulSoup(html_string, "html.parser")

        tags = {'placeholder': 0}
        for tag in beautiful_soup.find_all():
            tags[tag.name] = len(beautiful_soup.find_all(tag.name))
        del tags['placeholder']

        # test matching of each tag
        for tag in tags:
            found = re.findall("<" + tag + ">([\S\s]*)</" + tag + ">", html_string)
            if len(found) != tags[tag]:
                print("Html file not valid")
                return False

        print("HTML file is valid")
        return True
