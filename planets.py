planet_list = ["Mercury", "Mars"]
spacecraft = [('Cassini', 'Jupiter'), ('Voyager I', 'Saturn'), ('Voyager I', 'Neptune'), ('Mariner 9', 'Mars')]

planet_list.append("Jupiter")
planet_list.append("Saturn")
# print(planet_list)

planet_list.extend(["Uranus", "Neptune"])
# print(planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
# print(planet_list)

planet_list.append("Pluto")
# print(planet_list)

rocky_planets = planet_list[0:4]
# print(rocky_planets)

del planet_list[-1]
# print(planet_list)

for planet in planet_list:
	for sc in spacecraft:
		if sc[1] == planet:
			print('{0} landed on {1}'.format(sc[0], planet))