import json

# Reading from a JSON File

with open("Cars.json", "r") as infile:
        cars = json.load(infile)
      
# updating json data
new_car = {
            
        "manufacturer": "Skoda",
        "model": "Scala",
        "top_speed": 100,
        "age": 1
      }
      
cars.append(new_car)

with open("Cars.json", "w") as outfile:
            json.dump(cars, outfile, indent=4)

            print(cars)

 #filtering json Data

with open("Cars.json", "r") as infile:
    cars = json.load(infile)

fast_cars = [car for car in cars if car['top_speed'] > 200]
 
with open("fast_cars.json", "w") as outfile:
    json.dump(fast_cars, outfile, indent=4)

print(f"Filtered cars with top speed > 200 MPH have been created in 'fast_cars.json'.")

  


