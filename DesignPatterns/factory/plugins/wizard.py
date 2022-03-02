from DesignPatterns.factory.plugins.character_abc import CharacterABC


class Wizard(CharacterABC):
    name = "Wizard"

    def make_noise(self):
        print(f"{self.name} is making noise")

    def move(self):
        print(f"{self.name} is moving")
