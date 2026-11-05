def pluralizer():
    es_endings = ["s", "x", "ch", "sh"]
    vowels = "aeiou"
    exceptions = {
    # Vowel change
    "man": "men",
    "woman": "women",
    "foot": "feet",
    "tooth": "teeth",
    "goose": "geese",
    "mouse": "mice",
    "louse": "lice",

    # -en endings
    "child": "children",
    "ox": "oxen",

    # Different word entirely
    "person": "people",
    "die": "dice",

    # Unchanged in the plural
    "sheep": "sheep",
    "deer": "deer",
    "moose": "moose",
    "swine": "swine",
    "bison": "bison",
    "fish": "fish",
    "salmon": "salmon",
    "trout": "trout",
    "cod": "cod",
    "squid": "squid",
    "shrimp": "shrimp",
    "aircraft": "aircraft",
    "spacecraft": "spacecraft",
    "hovercraft": "hovercraft",
    "series": "series",
    "species": "species",
    "offspring": "offspring",
    "means": "means",
    "headquarters": "headquarters",
    "crossroads": "crossroads",
    "barracks": "barracks",
    "corps": "corps",
    "chassis": "chassis",
    }

    word = input (">")
    if word in exceptions:
        print(exceptions[word])
    elif word[-1] in es_endings or word[:-2] in es_endings:
        print(word + "es")
    else: 
        print(word + "s")   


    
pluralizer()
