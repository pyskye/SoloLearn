jungle = {
    "Grr": "Lion",
    "Rawr": "Tiger",
    "Ssss": "Snake",
    "Chirp": "Bird"
}

noises = str(input())
noise_list = noises.split()

for x in noise_list:
    if x in jungle:
        print((jungle[x]), end=" ")