def get_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96
    
def part_one():
    with open("input") as f:
        priorities = 0
        for line in f.readlines():
            length = int(len(line) / 2)
            parts = [line[:length],line[length:]]
            for letter in parts[0]:
                if letter in parts[1]:
                    priorities += get_priority(letter)
                    break
        print(priorities)

def part_two():
    with open("input") as f:
        priorities = 0
        page = f.read()
        lines = page.split("\n")
        for i in range(int(len(lines) / 3)):
            index = i * 3
            for letter in lines[index]:
                if letter in lines[index + 1] and letter in lines[index + 2]:
                    priorities += get_priority(letter)
                    break

        print(priorities)

if __name__ == "__main__":
    part_one()            
    part_two()        