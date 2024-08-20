import math

# Solicita e lê o valor do Bulbo Seco em °C.
bulboSeco = float(input("Digite o valor do Bulbo Seco (°C): "))

# Solicita e lê o valor da Umidade Relativa em %.
umidadeRelativa = float(input("Digite o valor da Umidade Relativa (%): "))

# Solicita e lê a temperatura do meio refrigerado em °C.
tempMeioRefri = float(input("Digite a temperatura do meio refrigerado (°C): "))

# Solicita e lê a condutividade térmica do isolamento em W/(m.K).
condutividade = float(input("Digite a condutividade térmica do isolamento (W/(m.K)): "))

# Solicita e lê o coeficiente de convecção interno em W/m²°C.
convInterno = float(input("Digite o coeficiente de convecção interno (W/m²°C): "))

# Solicita e lê o coeficiente de convecção externo em W/m²°C.
convExterno = float(input("Digite o coeficiente de convecção externo (W/m²°C): "))

# Procedimento para calcular a temperatura de orvalho.
tempOrvalho = (109.8 + bulboSeco) * pow(umidadeRelativa / 100, 0.1247) - 109.8

# Procedimento do cálculo c1.
c1 = (tempOrvalho - tempMeioRefri) / (bulboSeco - tempOrvalho)

# Procedimento para calcular o comprimento da espessura do material isolante em milímetros.
comprimento = 1000 * condutividade * (c1 * (1 / convInterno) - (1 / convExterno))

# Resultado final.
print(f"Espessura do material isolante: {comprimento:.2f} mm")