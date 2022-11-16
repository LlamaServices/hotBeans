def inverseDict(d: dict) -> dict:
    '''
    • Позив процедуре инверзниРечник({1:10, 2:20, 3:30}) враћа {10: [1], 20: [2], 30: [3]}.
    • Позив инверзниРечник({1:10, 2:20, 3:30, 4:30}) враћа {10: [1], 20: [2], 30: [3, 4]}.
    • Позив процедуре инверзниРечник({4:True, 0:True, 2:True}) ће вратити {True: [0, 2, 4]}.
    '''
    # Mislim da moze i bez ove linije, ali me mrzi da pravim liste usput
    invd = {v: [] for k, v in d.items()}
    
    for key, val in d.items():
        for invkey, invval in invd.items():
            if val == invkey:
                invd[invkey].append(key)

    # Sortiranje
    for key, val in invd.items():
        invd[key].sort()

    return invd

print(inverseDict({4:True, 0:True, 2:True}))