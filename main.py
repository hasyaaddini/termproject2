mood_grouping = {
    "happy" : ["happy", "amazing", "wonderful", "excited", "contented", "cheerful", "cheery", 
              "joyful", "jolly", "gleeful", "delighted", "smiling", "beaming", "grinning", 
              "glowing", "satisfied", "blithe", "joyous", "beatific", "blessed", "thrilled", 
              "elated", "exhilarated", "ecstatic", "blissful", "euphoric", "overjoyed", 
              "on cloud nine", "over the moon", "glad", "fortunate", "lucky", "favourable",
               "good", "right"],

    "sad"   : ["sad", "terrible", "depressed", "unhappy", "sorrowful", "dejected", "miserable", "low",
               "down", "gloomy", "blue", "melancholy", "melancholic", "low-spirited", "heartbroken",
               "awful", "wretched", "sorry", "pitiful", "upset", "pathetic", "shameful", "dreadful"],

    "angry" : ["angry", "furious", "mad", "annoyed", "irritated", "displeased", "provoked", "resentful",
               "enraged", "fuming", "outraged", "bad-tempered", "hot-tempered", "short-tempered", 
               "riled", "pissed"]
}

def sentence_checker(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace("-", " ")

    for p in ["!", "@", "#", "$", "%", "^", "&", "*", "_", ".", ",", "?", ";", ":", "'"]:
        sentence = sentence.replace(p, "")

    sentence = " ".join(sentence.split())
    return sentence

training_input = []
training_mood = []

with open("training_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith('#'):
            continue
        input, mood = line.split(",")
        input_checked = sentence_checker(input)
        training_input.append(input_checked)
        training_mood.append(mood)

def mood_counter(input):
    emotion = {mood: 0 for mood in mood_grouping}

    for mood, group in mood_grouping.items():
        for word in group:
            if word in input:
                emotion[mood] += 1

    return emotion

def predicting_current_mood(input):
    emotion = mood_counter(input)
    max_value = max(emotion.values())

    if max_value == 0:
        return "neutral"
    
    tied_moods = [mood for mood, count in emotion.items() if count == max_value]

    if len(tied_moods) > 1:
        mood_options = " or ".join(tied_moods)
        user_choice = input(f"I’m sorry but could you clarify again once more whether you feel {mood_options}? ")
        return user_choice.lower()
    
    return tied_moods[0]
