import os


def get_wiki_dir():
        return '{}.wiki'.format(os.path.dirname(os.path.realpath(__file__)))


def get_file_path(link):
    return os.path.join(get_wiki_dir(), '{}.md'.format(link))