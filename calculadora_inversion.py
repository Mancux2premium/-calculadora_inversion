print("Interes anual 95%")
interes_anual = 95
dinero_a_invertir = int(input("Ingrese la cantidad que desea invertir:"))
plazo_de_inversion = int(input("ingrese un plazo, en años:"))

ganancia = (dinero_a_invertir * 0.95) * plazo_de_inversion

rendimiento = dinero_a_invertir + ganancia

print("Felizidades por el plazo de: ",plazo_de_inversion, "años, obtuviste un rendimiento de", ganancia, "\n""Lo que da un saldo total de: ",rendimiento)


