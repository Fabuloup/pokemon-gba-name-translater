import requests
from requests_negotiate_sspi import HttpNegotiateAuth
import time

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})
session.auth = HttpNegotiateAuth()

BASE_URL = "https://pokeapi.co/api/v2"

def get_all_resources(endpoint, query_limit=386):
    """Récupère toutes les ressources paginées d'un endpoint"""
    results = []
    url = f"{BASE_URL}/{endpoint}?limit={query_limit}"

    while url:
        response = session.get(url)
        response.raise_for_status()
        data = response.json()

        results.extend(data["results"])
        url = data["next"]

    return results


def get_french_name(url):
    """Récupère le nom français d'une ressource"""
    response = session.get(url)
    response.raise_for_status()
    data = response.json()

    for name in data.get("names", []):
        if name["language"]["name"] == "fr":
            return name["name"]

    return None


def build_dictionary():
    result = {
        "pokemon": {},
        "moves": {}
    }

    # --- Pokémon ---
    print("Récupération des Pokémon...")
    pokemons = get_all_resources("pokemon-species", 386)

    for p in pokemons:
        en_name = p["name"].upper()
        fr_name = get_french_name(p["url"])

        if fr_name:
            result["pokemon"][en_name] = fr_name.upper()

        time.sleep(0.05)  # éviter de spam l'API

    # --- Moves ---
    print("Récupération des attaques...")
    moves = get_all_resources("move", 354)

    for m in moves:
        en_name = m["name"].upper()
        fr_name = get_french_name(m["url"])

        if fr_name:
            result["moves"][en_name] = fr_name.upper()

        time.sleep(0.05)

    return result


if __name__ == "__main__":
    data = build_dictionary()

    print(data)

    import json
    with open("pokemon_moves_fr_en.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Fichier généré : pokemon_moves_fr_en.json")