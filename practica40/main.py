from auto import Auto
from bote import Bote
from avion import Avion

def main():
    auto1 = Auto("Ford","K")
    bote1 = Bote("Wasser","Schewer")
    avion1 = Avion("Boeing","307")

    auto1.mensaje()
    bote1.navegar()
    avion1.flying()

if __name__ == "__main__":
    main()
