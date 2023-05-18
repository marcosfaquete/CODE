import speedtest

test = speedtest.speedtest()

# Faz o teste de Download e converte em mb/s
down = test.dowload()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

# Faz o teste de Upload e converte em mb/s
upload = test.upload()
rsUP = round(upload)
fUp = int(rsUP / 1e+6)

# Mostra resultados
print(f"Sua velocidade de Dowload é de: {fDown} mb/s")
print("\n")
print(f"Sua velocidade de Upload é de: {fUp} mb/s")
