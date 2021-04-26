def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name

print(are_you_playing_banjo('Amy'))
print(are_you_playing_banjo('Riko'))
