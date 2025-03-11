import sys
import time


class Place:
    def __init__(self, location, country, distance):
        self.location = location
        self.country = country
        self.distance = distance


array = [
    Place("Cork", "IE", 4581.05),
    Place("Mykonos", "GR", 6278.12),
    Place("Palma", "ES", 5579.51),
    Place("Sardinia", "IT", 5731.21),
    Place("Osaka", "JP", 4995.00),
    Place("Buenos Aires", "AR", 6912.28),
    Place("Melbourne", "AU", 8149.70),
    Place("Kishtwar", "IN", 6765.31),
    Place("Lyon", "FR", 5285.99),
]

text = open("data.txt", "w")
text.write("Location/Country/Distance" + "\n")
for i in range(len(array)):
    text.write(array[i].location + "/" + array[i].country + "/" + str(array[i].distance) + "\n")
text.close()

command = input("Enter 1 to export list to .csv, 2 to exit. ")

if command == "1":
    prompt = "run"
    text = open("export_service.txt", "w")
    text.write(prompt)
    text.close()

    time.sleep(1)
    text = open("export_response.txt", "r")
    print(text.read())
    text.close()
    text = open("export_response.txt", "w")
    text.close()
elif command == "2":
    prompt = "terminate"
    text = open("export_service.txt", "w")
    text.write(prompt)
    text.close()
    sys.exit()
