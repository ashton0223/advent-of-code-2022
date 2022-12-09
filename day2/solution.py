def part_one():
    win = {
        "A":"Y",
        "B":"Z",
        "C":"X",
    }
    lose = {
        "A":"Z",
        "B":"X",
        "C":"Y",
    }
    choices = {
        "X":1,
        "Y":2,
        "Z":3
    }
    points = 0
    with open("input") as f:
        page = f.read()
        lines = page.split("\n")
        for line in lines:
            picks = line.split(" ")
            if win[picks[0]] == picks[1]:
                points += 6
            elif lose[picks[0]] != picks[1]:
                points += 3
            points += choices[picks[1]]
        
        print(points)

def part_two():
    win = {
        "A":"B",
        "B":"C",
        "C":"A",
    }
    lose = {
        "A":"C",
        "B":"A",
        "C":"B",
    }
    choices = {
        "A":1,
        "B":2,
        "C":3
    }
    points = 0
    with open("input") as f:
        page = f.read()
        lines = page.split("\n")
        for line in lines:
            parts = line.split(" ")
            answer = ""
            if parts[1] == "X":
                answer = lose[parts[0]]
            elif parts[1] == "Y":
                answer = parts[0]
                points += 3
            elif parts[1] == "Z":
                answer = win[parts[0]]
                points += 6
            points += choices[answer]
        print(points)

if __name__ == "__main__":
    part_one()
    part_two()