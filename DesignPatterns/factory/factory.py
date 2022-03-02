import importlib
import json

from DesignPatterns.factory.plugins.character_abc import CharacterABC


class Factory:
    modules: dict = {}
    characters: dict[str, CharacterABC] = {}

    def get_modules(self, *, file_path="plugins/characters.json"):
        with open(file_path) as file:
            self.modules_data = json.load(file)

    def import_modules(self):
        for module_properties in self.modules_data.values():
            module = importlib.import_module(module_properties["file_path"])
            if not module_properties["enabled"]:
                continue
            self.modules[module_properties["class_name"]] = (getattr(module, module_properties["class_name"]))

    def load_modules(self):
        for module_name, module_obj in self.modules.items():
            self.characters[module_name] = module_obj()
