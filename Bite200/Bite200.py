from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"

roman_value = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}


class Enchantment:
    """Minecraft enchantment class

    Implements the following:
        id_name, name, max_level, description, items
    """
    def __init__(self, id_name, name, max_level, description):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = []
        try:
            self.arabic_number = roman_value[self.max_level]
        except KeyError:
            self.arabic_number = self.max_level

    def __str__(self):
        result = self.name.title()+' ('+str(self.arabic_number)+'): '+self.description
        return result

    def __repr__(self):
        return '['+str(self.arabic_number)+'] '+self.id_name


class Item:
    """Minecraft enchantable item class

    Implements the following:
        name, enchantments
    """
    def __init__(self, name):
        self.name = name.title()
        self.enchantments = []

    def __str__(self):
        enhancements = '\n  '.join(self.enchantments)

        result = f'{self.name}:\n  {enhancements}'
        return result


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects

    With the key being the id_name of the enchantment.
    """
    enchantment_dict = {}
    enchantment_table = soup.find(id='minecraft_items').find_all('tr')
    for row in enchantment_table[1:]:
        cells = row.find_all('td')
        item_id = cells[0].text.split('(')[-1].replace(')', '')
        item_name = cells[0].text.split('(')[0]
        max_level = cells[1].text
        description = cells[2].text
        items_list = cells[4].find_all('img')[0].attrs['data-src'].split(('/'))[-1].replace('.png', '')\
            .replace('enchanted', '').replace('iron', '').replace('sm', '').split('_')
        enchantment_dict[item_id] = Enchantment(
            item_id,
            item_name,
            max_level,
            description,
        )
        for item in items_list:
            if item != '':
                enchantment_dict[item_id].items.append(item)

    return enchantment_dict


def generate_items(data):
    """Generates a dictionary of Item objects

    With the key being the item name.
    """
    item_dict = {}
    item_list = []
    for i in data.keys():
        for item in data[i].items:
            if item not in item_list:
                item_list.append(item)

    for i in sorted(item_list):
        item_dict[i.title()] = Item(i.title())
        for j in data.keys():
            if i in data[j].items:
                item_dict[i.title()].enchantments.append(data[j].__repr__())
    return item_dict


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)
        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.

    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""