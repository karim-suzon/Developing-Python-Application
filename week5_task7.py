#7. Create a short dictionary: e.g Finnish to English. Add some wordpairs to a list.
# Or as example, here are some English – Italian words:

#treaty patto, truck camion, trust trust, value valore, volunteer volontario, wage paga, wages ricompensa.
#wholesale ingrosso, work lavoro, work opera, work force manodopera, worker operaio, workman operaio, workplace posto di lavoro, worth valore

word_dictionary_fin_eng = {
    "sopimus" : "treaty",
    "kurmaauto" : "truck",
    "usko" : "trust",
    "arvo" : "value",
    "vapaaehtoiseksi" : "volunteer",
    "palkka" : "wage",
    "palkat" : "wages",
    "tukku"  : "wholesale",
    "työ"   : "work",
    "työvoimaa" : "manpower",
    "työntekijä" : "worker",
    "työpaikka"  : "workplace",
    "arvoinen"  : "worth",
    "morning"  : "amu",
    "päivä"    : "day",
    "loma" : "holiday",
}

print(word_dictionary_fin_eng["loma"])
print(word_dictionary_fin_eng.get("palkka"))
print(word_dictionary_fin_eng.get("hyvä"))