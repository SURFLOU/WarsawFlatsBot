from flat import Flats
from telegram.ext import *

FlatOchota = Flats("Ochota")
FlatWlochy = Flats("Wlochy")
FlatMokotow = Flats("Mokotow")

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message == "ochota":
        return FlatOchota.isThereNewFlats()
    if user_message == "wlochy":
        return FlatWlochy.isThereNewFlats()
    if user_message == "mokotow":
        return FlatMokotow.isThereNewFlats()

    return "Zle polecenie"
 

