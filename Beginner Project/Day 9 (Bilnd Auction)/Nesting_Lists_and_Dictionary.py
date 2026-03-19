# simple disctionary

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nested list in dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Shuttgart"]
}

#print Liile
print(travel_log["France"][1])

nested_list=["A","B",["C","D"]]

print(nested_list[2][1])


nested_travel_log = {
    "France" : {
        "Cities_visited" : ["Paris", "Lille", "Dijon"],
        "Num_times_visted" : "9",
    },
    "Germany" : {
        "Cities_visited" : ["Berlin", "Hamburg", "Shuttgart"],
        "Num_times_visted" : "18",
    }
}

print(nested_travel_log["France"]["Cities_visited"][0])
print(nested_travel_log["Germany"]["Cities_visited"][2])