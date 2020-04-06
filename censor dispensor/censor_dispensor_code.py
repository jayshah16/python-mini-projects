# Sample emails to be censored.
email_one = open("data/email_one.txt", "r").read()
email_two = open("data/email_two.txt", "r").read()
email_three = open("data/email_three.txt", "r").read()
email_four = open("data/email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her",
                     "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed",
                  "out of control", "help", "unhappy", "bad", "upset", "awful", "broken",
                  "damage", "damaging", "dismal", "distressed", "distressed", "concerning",
                  "horrible", "horribly", "questionable"]


def censor_first(text, phrase):
    final = " "
    for x in phrase:
        if phrase == " ":
            return final
        else:
            final += "#"
    return text.replace(phrase, final)


def censor_second(text, lists):
    final = " "
    for word in lists:
        for x in range(0, len(word)):
            if word[x] == " ":
                final += " "
            else:
                final += "#"
        text = text.replace(word, final)
    return text


def censor_third(text, negative, proprietary):
    counter = {}
    for word in text.strip().split(" "):
        if word in negative:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        if word in proprietary:
            censor = len(word) * "#"
            text = text.replace(word, censor)

    for key, value in counter.items():
        if value > 2:
            censor = len(key) * "#"
            text = text.replace(key, censor)

    return text


def censor_fourth(text, censored_list):
    input_text_words = []
    for x in text.split(" "):
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    for i in range(0, len(input_text_words)):
        checked_word = input_text_words[i]
        if checked_word in censored_list:
            censored_word = " "
            censored_word = censored_word + "X"
            input_text_words[i] = input_text_words[i].replace(word, censored_word)

            # Censoring the word before the targeted word
            word_before = input_text_words[i - 1]
            censored_word_before = " "
            for x in range(0, len(word_before)):
                censored_word_before = censored_word_before + "X"
            input_text_words[i - 1] = input_text_words[i - 1].replace(word_before, censored_word_before)
            # Censoring the word after the targeted word
            word_after = input_text_words[i + 1]
            censored_word_after = ""
            for x in range(0, len(word_after)):
                censored_word_after = censored_word_after + "X"
            input_text_words[i + 1] = input_text_words[i + 1].replace(word_after, censored_word_after)

    return " ".join(input_text_words)

# censor_all = proprietary_terms + negative_words
# print((censor_first(email_one, "learning algorithms")))
# print((censor_second(email_two,proprietary_terms)))
# print((censor_third(email_three,negative_words,proprietary_terms )))
# print(censor_fourth(email_four, censor_all))
