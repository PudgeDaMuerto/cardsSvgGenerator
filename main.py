import os
import bs4 as bs

TEMPLATE_DIR_NAME = f"templates"
SAVE_DIR_NAME = f"output"

CUR_PATH = os.path.abspath(os.path.curdir)
TEMPLATE_PATH = os.path.join(CUR_PATH, TEMPLATE_DIR_NAME)
OUTPUT_PATH = os.path.join(CUR_PATH, SAVE_DIR_NAME)


def generate_cards(template_file):
    with open(os.path.join(TEMPLATE_PATH, template_file)) as file:
        source = file.read()

    for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        bs_source = bs.BeautifulSoup(source, 'html.parser')
        for tag in bs_source.findAll('text'):
            tag.string = str(value)

            with open(os.path.join(OUTPUT_PATH, f"{value}{template_file}"), 'w') as file:
                file.write(str(bs_source))


if __name__ == '__main__':
    suits = os.listdir(TEMPLATE_PATH)
    for suit in suits:
        generate_cards(suit)
