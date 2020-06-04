import unittest
from dokumentarij import  DokumentarijController, DokumentarijModel, DokumentarijView

class DokumentarijTestCase(unittest.TestCase):
    def test_if_name_is_added_in_list(self):
        game_test = DokumentarijController(DokumentarijModel(), DokumentarijView())
        list = game_test.model.names
        initial_list = len(list)
        game_test.get_new_name()
        after_list = len(list)
        self.assertLess(initial_list, after_list , "Broj studenata u dokumentariju  mora biti veći nakon dodavanja imena " )

   




if __name__ == "__main__":
    unittest.main()
    