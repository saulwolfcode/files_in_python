import json

# file = open("friends_json.txt","r")
# file_content=json.load(file)
# file.close()

with open("friends_json.txt","r") as file:
    file_content=json.load(file)

print(file_content["friends"][0])

cars = [
    {
        "make":"Ford","model":"Fiesta"
    },
    {
        "make":"Ford","model":"Focus"
    }

]

# file = open("friends_json.txt","r")
# file_content=json.load(file)
# file.close()

with open("cars_json.txt","w") as file:
    json.dump(cars,file)

my_json_string= '[{"name": "Alfa Romeo", "released": "1950"}]'

incorrect_car=json.loads(my_json_string)
print(incorrect_car[0]["name"])


