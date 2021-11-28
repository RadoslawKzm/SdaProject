from DesignPatterns.factory.plugins.character_abc import CharacterABC
from plugins.bard import Bard
from plugins.wizard import Wizard
from plugins.tank import Tank

tank = Tank()
wizard = Wizard()
bard = Bard()


# characters = [tank, wizard, bard]
# for character in characters:
#     character.make_noise()

def func(characters: list[CharacterABC]):
    for character in characters:
        character.make_noise()
        character.move()


if __name__ == '__main__':
    func([tank, wizard, bard])
