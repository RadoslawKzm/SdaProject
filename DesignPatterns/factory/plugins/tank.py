from DesignPatterns.factory.plugins.character_abc import CharacterABC


class Tank(CharacterABC):
    name = "Tank"

    def move(self):
        print(f"{self.name} is moving")

    def make_noise(self) -> None:
        print(f"{self.name} is making noise")
