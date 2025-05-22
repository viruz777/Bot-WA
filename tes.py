x = input("masukan nama zat1: ")
y = input("masukan nama zat2: ")


def reaksi(zat1, zat2):
    if zat1 == "HCl" and zat2 == "NaOH":
        return "Reaksi netralisasi: NaCl + H2O"
    elif zat1 == "H2SO4" and zat2 == "BaCl2":
        return "Reaksi pengendapan: BaSO4 + 2HCl"
    else:
        return "Tidak ada reaksi yang diketahui."


print(reaksi(x, y))
