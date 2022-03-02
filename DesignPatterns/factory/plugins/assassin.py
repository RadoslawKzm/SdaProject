from DesignPatterns.factory.plugins.character_abc import CharacterABC


class Assassin(CharacterABC):
    name = "Assassin"

    def make_noise(self):
        print(f"some weird {self.name} noises")

    def move(self):
        print(f"{self.name} is moving")
