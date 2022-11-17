def meow(arr: list) -> int:
    najRastuci = 0
    rastuci = 0
    for x in range(1, len(arr)):
        if arr[x] > arr[x-1]:
            rastuci += 1
            if x == 1:
                rastuci += 1
        if arr[x] < arr[x-1] and rastuci > najRastuci:
            najRastuci = rastuci
            rastuci = 0
        if arr[x] < arr[x-1] and not rastuci > najRastuci:
            rastuci = 0
        if x == (len(arr) - 1):
            if rastuci > najRastuci:
                najRastuci = rastuci
    return najRastuci

print(meow([1,2,3,4,5]))