class Planet:
    counter = 0

    def __init__(self, *, name: str):
        self.name = name
        self.update_counter()

    def make_some_noise(self):
        print(f"{self.name} is making some noise")

    @classmethod
    def update_counter(cls):
        cls.counter += 1


if __name__ == "__main__":
    mars = Planet(name="mars")
    jowisz = Planet(name="jowisz")
    saturn = Planet(name="saturn")
    neptun = Planet(name="neptun")
    uran = Planet(name="uran")
    lst = [mars, jowisz, saturn, uran, neptun]
    dictio = {
        "mars": mars,
        "jowisz": jowisz,
        "saturn": saturn,
        "neptun": neptun,
        "uran": uran,
    }

    # lst = [
    #     Planet(name="mars"),
    #     Planet(name="jowisz"),
    #     Planet(name="saturn"),
    #     Planet(name="neptun"),
    #     Planet(name="uran"),
    # ]
    # dictio = {
    #     "mars": Planet(name="mars"),
    #     "jowisz": Planet(name="jowisz"),
    #     "saturn": Planet(name="saturn"),
    #     "neptun": Planet(name="neptun"),
    #     "uran": Planet(name="uran")
    # }
