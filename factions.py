import os
import re
from faction import Faction
from io_common import get_file_path


class Factions:

    def __init__(self, debug=False):
        self.factions_path = ''
        self.summary = []
        self.factions = {}

        if not debug:
            self.populate()

    def set_factions_path(self):
        self.factions_path = get_file_path('Factions')

    def parse(self):
        summary_set = False
        with open(self.factions_path) as f:
            for line in f:
                matched = re.match(r'##\[\[(?P<name>[\s\w]*)\|(?P<link>[\w\-]*)\]\]', line)
                if matched:
                    self.factions[matched.group('name')] = matched.group('link')
                    summary_set = True
                elif not summary_set:
                    self.summary.append(line)

    def instantiate_faction(self, name, link):
        self.factions[name] = Faction(name, link)

    def instantiate_factions(self):
        for name, link in self.factions.items():
            self.instantiate_faction(name=name, link=link)

    def populate(self):
        self.set_factions_path()
        self.parse()
        self.instantiate_factions()

    def add_faction(self, name, link):
        self.factions[name] = Faction(name=name, link=link, new_file=True)

    def write(self):
        with open(self.factions_path, 'w') as f:
            for line in self.summary:
                f.write(line)
            for faction in sorted(self.factions):
                f.write('##[[{}|{}]]\n'.format(faction, self.factions[faction].link))
                for line in self.factions[faction].summary:
                    f.write(line)
