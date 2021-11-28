import json
from DesignPatterns.factory.plugins.character_abc import CharacterABC


def factory(path="plugins/characters.json"):
    with open(path) as file:
        modules_data = json.load(file)
    for name, module in modules_data.items():
        extract_from_module = module["extract_from_module"]
        file_path = module["file_path"]
        enabled = module["enabled"]


def func(characters: list[CharacterABC]):
    for character in characters:
        character.make_noise()
        character.move()


if __name__ == '__main__':
    factory()
