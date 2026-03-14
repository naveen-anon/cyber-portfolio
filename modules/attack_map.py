
import random

def get_attack_points():

    attacks = []

    locations = [

        {"lat":37.77,"lng":-122.41},
        {"lat":28.61,"lng":77.20},
        {"lat":51.50,"lng":-0.12},
        {"lat":35.68,"lng":139.69},
        {"lat":55.75,"lng":37.61},
        {"lat":48.85,"lng":2.35},
        {"lat":-33.86,"lng":151.20}

    ]

    for loc in locations:

        attacks.append({

            "lat":loc["lat"],
            "lng":loc["lng"],
            "intensity":random.randint(1,5)

        })

    return attacks
