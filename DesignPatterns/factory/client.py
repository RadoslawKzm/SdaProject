from DesignPatterns.factory.plugins.character_abc import CharacterABC
from DesignPatterns.factory.factory import Factory


def func(characters: list[CharacterABC]):
    for character in characters:
        character.make_noise()
        character.move()


if __name__ == '__main__':
    fac = Factory()
    fac.get_modules()
    fac.import_modules()
    fac.load_modules()
    func(characters=list(fac.characters.values()))
