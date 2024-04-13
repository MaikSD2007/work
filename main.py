meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta comun a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobacion",
            "CREEPY": "Algo aterrador o siniestro",
            "AGGRO": "Ponerse agresivo o enojado",
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (!con mayúsculas¡): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No se ha encontrado la palabra , escribe otra palabra")
