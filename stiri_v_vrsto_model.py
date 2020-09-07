POLJE_SIRINA = 7
POLJE_VISINA = 6

class Polje:
    def __init__(self):
        # 0 = ni žetona, 1 = žeton igralca 1, 2 = žeton igralca 2
        self.polje = [[0 for i in range(POLJE_VISINA)] for j in range(POLJE_SIRINA)]

        self.igralec = 1  # Trenutni igralec
        self.zmaga = 0  # 0 = ni zmage, 1 = zmaga prvega, 2 = zmaga drugega

    def resetiraj(self):
        self.__init__()

    def dodaj_zeton(self, x):
        if self.zmaga != 0:
            raise Exception("Nekdo je že zmagal, ni možno igrati")

        # Najde prvo prosto mesto za žeton
        for y in range(0, POLJE_VISINA):
            if self.polje[x][y] == 0:
                self.polje[x][y] = self.igralec
                zmagal = self.__preveri_zmago(x, y)  # Vrne True, če je ta igralec zmagal

                if zmagal:
                    self.zmaga = self.igralec
                else:
                    if self.igralec == 1:  # Zamenja igralca
                        self.igralec = 2
                    else:
                        self.igralec = 1
                return None

        raise Exception("Na to pozicijo ni možno dati žetona")

    def __preveri_zmago(self, x, y):
        if self.__preveri_zmago_v_smeri(x, y, 1, 0):  # Vodoravno
            return True

        if self.__preveri_zmago_v_smeri(x, y, 0, 1):  # Navpično
            return True

        if self.__preveri_zmago_v_smeri(x, y, 1, 1):  # Prva diagonala
            return True

        if self.__preveri_zmago_v_smeri(x, y, 1, -1):  # Druga diagonala
            return True

        return False

    def __preveri_zmago_v_smeri(self, x, y, step_x, step_y):
        # Preveri, če je igralec, ki je na vrsti zmagal
        igralec = self.polje[x][y]
        stevilo = 1  # Trenutni žeton je prvi v vrsti

        stevilo += self.__stej_zetone(x, y, step_x, step_y, igralec)
        stevilo += self.__stej_zetone(x, y, -step_x, -step_y, igralec)  # Preveri še v drugo smer

        return stevilo >= 4  # Če so štirje v vrsti je zmagal

    def __stej_zetone(self, x, y, step_x, step_y, igralec):
        # Začnemo na 0 in gremo 3 naprej, tako da skupaj preverimo 4 žetone,
        # vrnemo število zaporednih žetonov istega igralca v določeni smeri
        stevilo = 0

        for i in range(3):
            x += step_x
            y += step_y

            if not self.__preveri_veljavno_polje(x, y): # Preveri, če so indeksi del polja
                break
            elif self.polje[x][y] == igralec: # Če je žeton od igralca, za katerega preverjamo
                stevilo += 1
            else:  # Žeton od nasprotnika ali pa prazno polje
                break

        return stevilo

    def __preveri_veljavno_polje(self, x, y):
        if x < 0 or y < 0:
            return False

        if x >= POLJE_SIRINA or y >= POLJE_VISINA:
            return False

        return True