from plugins.bard import Bard
from plugins.wizard import Wizard
from plugins.tank import Tank

tank = Tank()
wizard = Wizard()
bard = Bard()

characters = [tank, wizard, bard]
for character in characters:
    character.make_noise()