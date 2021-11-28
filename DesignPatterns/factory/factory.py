from DesignPatterns.factory.plugins.character_abc import CharacterABC


def factory(path="plugins/characters.json"):
    with open(path) as f:
        print("pass")




def func(characters: list[CharacterABC]):
    for character in characters:
        character.make_noise()
        character.move()


if __name__ == '__main__':
   factory()
