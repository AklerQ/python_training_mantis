from sys import maxsize
import re


class Project:

    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and \
               self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self):
        return Project(id=self.id, name=re.sub("[ ]{1,}", " ", (self.name).strip()),
                       description=re.sub("[ ]{1,}", " ", (self.description).strip()))
