# Funktion zum Einlesen der Eingabedatei
def read_input(file_path):
    with open(file_path) as file:
        input_text = file.read()
    return input_text


# Funktion, die das Hopsen-Spiel implementiert
def get_winner(text, buchstaben_werte, amira, bela):
    pos_amira = amira
    pos_bela = bela
    len_text = len(text)

    # solange iterieren bis es ein Ergebnis gibt
    while True:
        # aktueller buchstabe von Amira und Bela
        a_buchstabe = text[pos_amira]
        b_buchstabe = text[pos_bela]

        # Positionen von Amira und Bela aktualisieren
        pos_amira += buchstaben_werte[a_buchstabe]
        pos_bela += buchstaben_werte[b_buchstabe]

        # überprüfen, ob es ein Ergebnis gibt
        if pos_amira >= len_text and pos_bela >= len_text:
            return "Unentschieden"
        elif pos_amira >= len_text:
            return "Amira"
        elif pos_bela >= len_text:
            return "Bela"
