from colorama import Fore, init
import os
from bs4 import BeautifulSoup
import requests
from sys import platform

print("""
====================================
BIENVENIDO A LA CALCULADORA DE DOLAR
====================================
""")

print("Actualizando precio USD...\n")


init(autoreset=True)

url = "https://www.dolarhoy.com/cotizaciondolarblue"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

btc = soup.find_all('div', class_="value")

btcprice = list()

for i in btc:
    btcprice.append(i.text)

venta= btcprice[1]
calc= venta.replace("$", "0")
calc= float(calc)

def calcu():
    print("""Opciones:
    1.- Calcular PESO a DOLAR
    2.- Calcular DOLAR a PESO\n""")
    opcion=int(input("Elija una opción: "))
    while opcion != 1 and opcion != 2:
        print("Error, seleccione 1 o 2")
        opcion=int(input("Elija una opción: "))
    if opcion == 1:
        print("\nOpcion seleccionada: PESO a DOLAR")
        a=float(input("\nIngrese los pesos que desea pasar a dolar: "))
        print(f"\n${a} pesos equivalen a " + Fore.RED + f"${round(a/calc,3)} USD\n")
    elif opcion ==2:
        print("\nOpcion seleccionada: DOLAR a PESO")
        a=float(input("\nIngrese los USD que desea pasar a pesos: "))
        print(f"\n${a} USD equivalen a " + Fore.RED + f"${round(a*calc,3)} pesos \n")
    
    
    print("""Desea realizar otra operación?
    1.- SI
    2.- NO \n""")

    x = int(input("Seleccione una opción: "))

    while x != 1 and x != 2:
        print("Error, seleccione 1 o 2")
        x=int(input("Elija una opción: "))
    if x == 1:
        calcu()
    elif x == 2:
        if platform == "linux" or platform == "linux2":
            os.system("clear")

        elif platform == "darwin":
            os.system("clear")

        elif platform == "win32":
            os.system("cls")

calcu()
