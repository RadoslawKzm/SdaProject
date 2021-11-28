from DesignPatterns.factory.plugins.character_abc import CharacterABC


class Bard(CharacterABC):
    name = "Bard"

    def make_noise(self):
        print(f"some weird {self.name} noises")

    def move(self):
        print(f"{self.name} is moving")
