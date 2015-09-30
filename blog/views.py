from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
    return  render(request,"blog/home.html")


def ret_json(request):
    a={
    "t": {
        "p": {
            "o": [
                {
                    "a": "Elemental HERO Absolute Zero",
                    "b": "Monster/Fusion/Effect",
                    "c": "WATER",
                    "d": "1 'HERO' monster + 1 WATER monster",
                    "e": "Blows up your field, sucks for you",
                    "f": "NULL",
                    "g": "8",
                    "h": "0",
                    "i": "2500",
                    "j": "2000",
                    "n": "YG04",
                    "k": "001",
                    "l": "40854197"
                },
                {
                    "a": "Elemental HERO Air Neos",
                    "b": "Monster/Fusion/Effect",
                    "c": "WIND",
                    "d": "Hummingbird + Neos",
                    "e": "Returns to extra at end phase",
                    "f": "NULL",
                    "g": "7",
                    "h": "0",
                    "i": "2500",
                    "j": "2000",
                    "n": "STON",
                    "k": "034",
                    "l": "11502550"
                },
                {
                    "a": "Cyber Jar",
                    "b": "Monster/Effect",
                    "c": "DARK",
                    "d": "NULL",
                    "e": "destroys all monsters on the field",
                    "f": "NULL",
                    "g": "3",
                    "h": "0",
                    "i": "900",
                    "j": "900",
                    "n": "MRL",
                    "k": "077",
                    "l": "34124316"
                },
                {
                    "a": "Wind-Up Carrier Zenmaity",
                    "b": "MACHINE/Xyz/Effect",
                    "c": "WATER",
                    "d": "2 Level 3 monsters",
                    "e": "Special summon a wind-up from your hand or deck.",
                    "f": "NULL",
                    "g": "0",
                    "h": "3",
                    "i": "1500",
                    "j": "1500",
                    "n": "ORCS",
                    "k": "044",
                    "l": "81122844"
                },
                {
                    "a": "BRAIN CONTROL",
                    "b": "Spell",
                    "c": "Spell",
                    "d": "NULL",
                    "e": "Pay 800 Life Points to target 1 face-up monster your opponent controls; take control of that target until the End Phase.",
                    "f": "Normal",
                    "g": "0",
                    "h": "0",
                    "i": "0",
                    "j": "0",
                    "n": "LCYW",
                    "k": "074",
                    "l": "87910978"
                },
                {
                    "a": "Ring of Destruction",
                    "b": "Trap",
                    "c": "Trap",
                    "d": "NULL",
                    "e": "Target 1 face-up monster on the field; destroy that target, and if you do, inflict damage to both players equal to that target's ATK.",
                    "f": "Normal",
                    "g": "0",
                    "h": "0",
                    "i": "0",
                    "j": "0",
                    "n": "YG04",
                    "k": "001",
                    "l": "40854197"
                }
            ]
        },
        "v": "2/3/2013"
    }
}
    data = {'arr': "me", 'hello': 'world'}
    d = {
    'first_name': 'Guido',
    'second_name': 'Rossum'
    #'titles': ['BDFL', 'Developer']

}

    return HttpResponse(json.dumps(a), content_type='application/json')