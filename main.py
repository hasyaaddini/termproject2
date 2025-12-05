training_input = []
training_mood = []

with open("training_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith('#'):
            continue
        input, mood = line.split(",")
        training_input.append(input)
        training_mood.append(mood)