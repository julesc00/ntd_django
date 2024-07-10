"""
response = [
    {'name': 'Hoth', 'population': None, 'terrains': ['tundra', 'ice caves', 'mountain ranges'], 'climates': ['frozen']}
    {'name': 'Dagobah', 'population': None, 'terrains': ['swamp', 'jungles'], 'climates': ['murky']}0
    {'name': 'Bespin', 'population': 6000000, 'terrains': ['gas giant'], 'climates': ['temperate']}
    {'name': 'Endor', 'population': 30000000, 'terrains': ['forests', 'mountains', 'lakes'], 'climates': ['temperate']}
    {'name': 'Naboo', 'population': 4500000000, 'terrains': ['grassy hills', 'swamps', 'forests', 'mountains'],
     'climates': ['temperate']}
    {'name': 'Coruscant', 'population': 1000000000000, 'terrains': ['cityscape', 'mountains'],
     'climates': ['temperate']}
    {'name': 'Kamino', 'population': 1000000000, 'terrains': ['ocean'], 'climates': ['temperate']}
    {'name': 'Geonosis', 'population': 100000000000, 'terrains': ['rock', 'desert', 'mountain', 'barren'],
     'climates': ['temperate', 'arid']}
    {'name': 'Utapau', 'population': 95000000, 'terrains': ['scrublands', 'savanna', 'canyons', 'sinkholes'],
     'climates': ['temperate', 'arid', 'windy']}
    {'name': 'Mustafar', 'population': 20000, 'terrains': ['volcanoes', 'lava rivers', 'mountains', 'caves'],
     'climates': ['hot']}
    {'name': 'Kashyyyk', 'population': 45000000, 'terrains': ['jungle', 'forests', 'lakes', 'rivers'],
     'climates': ['tropical']}
    {'name': 'Polis Massa', 'population': 1000000, 'terrains': ['airless asteroid'],
     'climates': ['artificial temperate']}
    {'name': 'Mygeeto', 'population': 19000000, 'terrains': ['glaciers', 'mountains', 'ice canyons'],
     'climates': ['frigid']}
    {'name': 'Felucia', 'population': 8500000, 'terrains': ['fungus forests'], 'climates': ['hot', 'humid']}
    {'name': 'Cato Neimoidia', 'population': 10000000, 'terrains': ['mountains', 'fields', 'forests', 'rock arches'],
     'climates': ['temperate', 'moist']}
    {'name': 'Saleucami', 'population': 1400000000, 'terrains': ['caves', 'desert', 'mountains', 'volcanoes'],
     'climates': ['hot']}
    {'name': 'Stewjon', 'population': None, 'terrains': ['grass'], 'climates': ['temperate']}
    {'name': 'Eriadu', 'population': 22000000000, 'terrains': ['cityscape'], 'climates': ['polluted']}
    {'name': 'Corellia', 'population': 3000000000, 'terrains': ['plains', 'urban', 'hills', 'forests'],
     'climates': ['temperate']}
    {'name': 'Rodia', 'population': 1300000000, 'terrains': ['jungles', 'oceans', 'urban', 'swamps'],
     'climates': ['hot']}
    {'name': 'Nal Hutta', 'population': 7000000000, 'terrains': ['urban', 'oceans', 'swamps', 'bogs'],
     'climates': ['temperate']}
    {'name': 'Dantooine', 'population': 1000, 'terrains': ['oceans', 'savannas', 'mountains', 'grasslands'],
     'climates': ['temperate']}
    {'name': 'Bestine IV', 'population': 62000000, 'terrains': ['rocky islands', 'oceans'], 'climates': ['temperate']}
    {'name': 'Ord Mantell', 'population': 4000000000, 'terrains': ['plains', 'seas', 'mesas'],
     'climates': ['temperate']}
    {'name': 'unknown', 'population': None, 'terrains': ['unknown'], 'climates': ['unknown']}
    {'name': 'Trandosha', 'population': 42000000, 'terrains': ['mountains', 'seas', 'grasslands', 'deserts'],
     'climates': ['arid']}
    {'name': 'Socorro', 'population': 300000000, 'terrains': ['deserts', 'mountains'], 'climates': ['arid']}
    {'name': 'Mon Cala', 'population': 27000000000, 'terrains': ['oceans', 'reefs', 'islands'],
     'climates': ['temperate']}
    {'name': 'Chandrila', 'population': 1200000000, 'terrains': ['plains', 'forests'], 'climates': ['temperate']}
    {'name': 'Sullust', 'population': 18500000000, 'terrains': ['mountains', 'volcanoes', 'rocky deserts'],
     'climates': ['superheated']}
    {'name': 'Toydaria', 'population': 11000000, 'terrains': ['swamps', 'lakes'], 'climates': ['temperate']}
    {'name': 'Malastare', 'population': 2000000000, 'terrains': ['swamps', 'deserts', 'jungles', 'mountains'],
     'climates': ['arid', 'temperate', 'tropical']}
    {'name': 'Dathomir', 'population': 5200, 'terrains': ['forests', 'deserts', 'savannas'], 'climates': ['temperate']}
    {'name': 'Ryloth', 'population': 1500000000, 'terrains': ['mountains', 'valleys', 'deserts', 'tundra'],
     'climates': ['temperate', 'arid', 'subartic']}
    {'name': 'Aleen Minor', 'population': None, 'terrains': ['unknown'], 'climates': ['unknown']}
    {'name': 'Vulpter', 'population': 421000000, 'terrains': ['urban', 'barren'], 'climates': ['temperate', 'artic']}
    {'name': 'Troiken', 'population': None, 'terrains': ['desert', 'tundra', 'rainforests', 'mountains'],
     'climates': ['unknown']}
    {'name': 'Tund', 'population': 0, 'terrains': ['barren', 'ash'], 'climates': ['unknown']}
    {'name': 'Haruun Kal', 'population': 705300, 'terrains': ['toxic cloudsea', 'plateaus', 'volcanoes'],
     'climates': ['temperate']}
    {'name': 'Cerea', 'population': 450000000, 'terrains': ['verdant'], 'climates': ['temperate']}
    {'name': 'Glee Anselm', 'population': 500000000, 'terrains': ['lakes', 'islands', 'swamps', 'seas'],
     'climates': ['tropical', 'temperate']}
    {'name': 'Iridonia', 'population': None, 'terrains': ['rocky canyons', 'acid pools'], 'climates': ['unknown']}
    {'name': 'Tholoth', 'population': None, 'terrains': ['unknown'], 'climates': ['unknown']}
    {'name': 'Iktotch', 'population': None, 'terrains': ['rocky'], 'climates': ['arid', 'rocky', 'windy']}
    {'name': 'Quermia', 'population': None, 'terrains': ['unknown'], 'climates': ['unknown']}
    {'name': 'Dorin', 'population': None, 'terrains': ['unknown'], 'climates': ['temperate']}
    {'name': 'Champala', 'population': 3500000000, 'terrains': ['oceans', 'rainforests', 'plateaus'],
     'climates': ['temperate']}
    {'name': 'Mirial', 'population': None, 'terrains': ['deserts'], 'climates': ['unknown']}
    {'name': 'Serenno', 'population': None, 'terrains': ['rainforests', 'rivers', 'mountains'], 'climates': ['unknown']}
    {'name': 'Concord Dawn', 'population': None, 'terrains': ['jungles', 'forests', 'deserts'], 'climates': ['unknown']}
    {'name': 'Zolan', 'population': None, 'terrains': ['unknown'], 'climates': ['unknown']}
    {'name': 'Ojom', 'population': 500000000, 'terrains': ['oceans', 'glaciers'], 'climates': ['frigid']}
    {'name': 'Skako', 'population': 500000000000, 'terrains': ['urban', 'vines'], 'climates': ['temperate']}
    {'name': 'Muunilinst', 'population': 5000000000, 'terrains': ['plains', 'forests', 'hills', 'mountains'],
     'climates': ['temperate']}
    {'name': 'Shili', 'population': None, 'terrains': ['cities', 'savannahs', 'seas', 'plains'],
     'climates': ['temperate']}
    {'name': 'Kalee', 'population': 4000000000, 'terrains': ['rainforests', 'cliffs', 'canyons', 'seas'],
     'climates': ['arid', 'temperate', 'tropical']}
    {'name': 'Umbara', 'population': None, 'terrains': ['unknown'], 'climates': ['unknown']}
]
"""