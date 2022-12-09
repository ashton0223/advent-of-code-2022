def part_one():
    with open('input') as f:
        highest = 0
        page = f.read()
        elves = page.split("\n\n")
        for elf in elves:
            sum = 0
            items = elf.split("\n")
            for item in items:
                sum += int(item)
            
            highest = sum if sum > highest else highest
        print(highest)

def part_two():
    with open("input") as f:
        page = f.read()
        elves_calories = []

        elves = page.split("\n\n")
        for elf in elves:
            sum = 0
            items = elf.split("\n")
            for item in items:
                sum += int(item)
            elves_calories.append(sum)
        
        elves_calories.sort()
        elves_calories.reverse()
        sum = 0
        for i in elves_calories[0:3]:
            sum += i
        print(sum)


if __name__ == "__main__":
    part_one()
    part_two()