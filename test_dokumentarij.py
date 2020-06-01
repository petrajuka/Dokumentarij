import unittest
from dokumentarij import  DokumentarijController, DokumentarijModel, DokumentarijView

class DokumentarijTestCase(unittest.TestCase):
    def test_list(self):
        game_test = DokumentarijController(DokumentarijModel(), DokumentarijView())
        name_list = game_test.model.names
        initial_list = len(name_list)
        game_test.get_new_name()
        after_list = len(name_list)
        self.assertGreater(initial_list, after_list, "Broj studenata u dokumentariju  mora biti veći nakon dodavanja imena " )

   




if __name__ == "__main__":
    unittest.main()
    