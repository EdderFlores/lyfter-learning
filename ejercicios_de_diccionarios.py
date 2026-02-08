#Ejercicio 1

hotel_inforation = {
    "name": "Hotel California",
    "stars": 5,
    "total_rooms": 0,
    "rooms": [
        {
            "number": 1001,
            "floor": 10,
            "rate_per_night": 200
        },
        {
            "number": 1002,
            "floor": 10,
            "rate_per_night": 250
        },
        {
            "number": 1003,
            "floor": 10,
            "rate_per_night": 300
        },
        {
            "number": 1004,
            "floor": 10,
            "rate_per_night": 350
        },
        {
            "number": 1005,
            "floor": 10,
            "rate_per_night": 400
        },
        {
            "number": 1006,
            "floor": 10,
            "rate_per_night": 450
        },
        {
            "number": 1007,
            "floor": 10,
            "rate_per_night": 500
        },
        {
            "number": 1008,
            "floor": 10,
            "rate_per_night": 550
        },
        {
            "number": 1009,
            "floor": 10,
            "rate_per_night": 600
        },
        {
            "number": 1010,
            "floor": 10,
            "rate_per_night": 650
        }
    ]
}



#Ejercicio 2

employee_details_dictionary = {}

main_details = [
    "first_name",
    "last_name",
    "age",
    "role"
]

employee_information = [
    "Edder",
    "Flores",
    "26",
    "Software Engineer"
]

for detail in range(0, len(main_details)):
    employee_details_dictionary[main_details[detail]] = employee_information[detail]


#Ejercicio 3

main_dictionary = {
    "hotel_name": "Welton Lodge",
    "hotel_location": "New York",
    "hotel_rating": 4,
    "hotel_amenities": [
        "Free Wi-Fi",
        "Swimming Pool",
        "Fitness Center",
        "Restaurant",
        "Bar"
    ]
}

keys_to_remove = [
    "hotel_location",
    "hotel_rating"
]

for key in keys_to_remove:
    main_dictionary.pop(key)