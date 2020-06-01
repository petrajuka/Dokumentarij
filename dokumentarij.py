# Dokumentarij je aplikacija za ispis i unos studenata
# na kolegiju Razvoj poslovnih aplikacija


class DokumentarijModel:
	def __init__(self):
		self.names = []
	
	@property
	def names(self):
		return self._names

	@names.setter
	def names(self, new_name):
		self._names = new_name


class DokumentarijView:
    def display_title_bar(self):
        print("\t**************************************************")
        print("\t*** Dokumentarij - Razvoj poslovnih aplikacija ***")
        print("\t**************************************************")

    def get_user_choice(self):
        # ispisujemo korisniku meni što može raditi u aplikaciji
        # na kraju ga pitamo i uzimamo njegov odabir te taj odabir vracamo 
        print("\n[1] Pogledaj listu studenata.")
        print("[2] Dodaj novog studenta.")
        print("[x] Izlaz.")

        return input("Što želite napraviti u dokumentariju?")

    def show_names(self, name):
        print(name.title())

    def put_new_name(self):
        # uzimamo kroz input od korisnika novo  ime te ga dodajemo u listu, ako to ime već nije u listi
        new_name = input("\n Unesite ime studenta: ")
        return new_name
        
class DokumentarijController:
    def __init__(self,model, view):
        self.model = model
        self.view = view
    
    def get_names(self):
        # prikazuje imena svih studenata dodanih u listu
        print("\n Ovo je popis studenata na kolegiju Razvoj poslovnih aplikacija: \n")
        for name in self.model.names:
            self.view.show_names(name)

    def get_new_name(self):
        # uzimamo kroz input od korisnika novo  ime te ga dodajemo u listu, ako to ime već nije u listi
        new_name = self.view.get_new_name()
        if new_name in self.model.names:
            print("\n{} je već upisan/a u dokumentariju.".format(new_name.title()))
        else:
            self.model.names.append(new_name)
            print("\n Dobrodošao/la {}!\n".format(new_name.title()))
    

    def play(self):
        choice = ''
        self.view.display_title_bar()
        while choice != 'x':
            choice = self.view.get_user_choice()
            self.view.display_title_bar()
            if choice == '1':
                self.get_names()
            elif choice == '2':
                self.get_new_name()
            elif choice == 'x':
                print("\nHvala na pregledu/uređivanju dokumentarija.Pozdrav!")
            else:
                print("Greška")
            
if __name__ == '__main__':
    game = DokumentarijController(DokumentarijModel(), DokumentarijView())
    game.play()            

