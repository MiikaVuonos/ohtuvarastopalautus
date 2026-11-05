from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        #print("---------------------------------------------------------------------------")


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tiedot = tomli.loads(content)

        #print(tiedot)
        #print("---------------------------------------------------------------------------")

        project = tiedot["project"]

        authors = [author["name"] for author in project["authors"]]

        return Project(
            project["name"],
            project["description"],
            project["license"],
            authors,
            project["dependencies"],
            tiedot["dependency-groups"]["dev"]
        )