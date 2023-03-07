with open("sammud.txt", "r") as f:
    sammud = [int(line) for line in f]
kokku =sum(sammud)
print(f"Nädala sammude summa: {kokku}")
keskmiselt = [sum(sammud[i:i+1])/1 for i in range(len(sammud))]
print (f"Keskmised sammud päevas: {keskmiselt}")
koige_rohkem = max(sammud)
koige_rohkem_indeks = sammud.index(koige_rohkem) + 1
koige_vahem = min(sammud)
koige_vahema_indeks = sammud.index(koige_vahem) + 1
print(f"Kõige rohkem samme arv oli {koige_rohkem} päeval {koige_rohkem_indeks}")
print(f"Kõige vähem oli samme {koige_vahem} päeval {koige_vahema_indeks}")
f.close()