import os
import re
from io_common import get_file_path


class Faction:

    def __init__(self, name, link, new_file=False, debug=False):
        self.name = name
        self.link = link
        self.faction_path = get_file_path(self.link)
        self.summary = []

        if not (new_file or debug):
            self.parse()

    def parse(self):
        pass
