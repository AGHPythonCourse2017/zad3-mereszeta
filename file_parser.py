import csv


class KeyProvider:
    def __init__(self, path):
        file = open(path, 'r')
        self.name = file.readline()
        self.key = file.readline()
    def print(self):
        print('name')
        print(self.name)
        print('key')
        print(self.key)


class ListOfWebsitesProvider:
    def __init__(self, path):
        with open(path, 'r') as csvf:
            col_headers = ['site', ]
            reader = csv.reader(csvf, delimiter=',')
            self.list_of_sites = []
            for line in reader:
                self.list_of_sites.append({'Website': line[0], 'Tags': [tag for tag in line if
                                                                        tag != line[0] and tag != ' ' and tag!='' and tag != line[
                                                                            len(line)-2]],
                                           'Desc': line[len(line)-2]})
            self.list_of_sites.pop(0)

    def print(self):
        for site in self.list_of_sites:
            print('website')
            print(site['Website'])
            print('tags')
            print(site['Tags'])
            print('desc')
            print(site['Desc'])