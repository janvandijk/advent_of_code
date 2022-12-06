f = open("input.txt", "r")

def make_int_range(section):
    from_to = section.split("-")
    return set(range(int(from_to[0]), int(from_to[1])+1))

aantal_omvat = 0
aantal_overlap = 0

for x in f:
    sections = x.strip().split(",")
    section_one = make_int_range(sections[0])
    section_two = make_int_range(sections[1])
    if section_one.issubset(section_two) or section_two.issubset(section_one):
        aantal_omvat += 1
    if not section_one.isdisjoint(section_two):
        aantal_overlap += 1

print("Antwoord 1: " + str(aantal_omvat))
print("Antwoord 2: " + str(aantal_overlap))