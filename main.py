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

mood_grouping = {
    "happy" : ["happy", "amazing", "wonderful", "excited", "contented", "cheerful", "cheery", 
              "joyful", "jolly", "gleeful", "delighted", "smiling", "beaming", "grinning", 
              "glowing", "satisfied", "blithe", "joyous", "beatific", "blessed", "thrilled", 
              "elated", "exhilarated", "ecstatic", "blissful", "euphoric", "overjoyed", 
              "on cloud nine", "over the moon", "glad", "fortunate", "lucky", "favourable",
               "good", "right"],

    "sad"   : ["sad", "terrible", "depressed", "unhappy", "sorrowful", "dejected", "miserable",
               "down", "gloomy", "blue", "melancholy", "melancholic", "low-spirited", "heartbroken",
               "awful", "wretched", "sorry", "pitiful", "upset", "pathetic", "shameful", "dreadful"],

    "angry" : ["angry", "furious", "mad", "annoyed", "irritated", "displeased", "provoked", "resentful",
               "enraged", "fuming", "outraged", "bad-tempered", "hot-tempered", "short-tempered", 
               "riled", "pissed"]
}

def sentence_checker(sen):
    sen = sen.lower()
    sen = sen.replace("-", " ")

    for p in ["!", "@", "#", "$", "%", "^", "&", "*", "_", ".", ",", "?", ";", ":", "'"]:
        sen = sen.replace(p, "")

    sen = " ".join(sen.split())
    return sen