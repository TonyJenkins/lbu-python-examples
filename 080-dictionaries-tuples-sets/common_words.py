#!/usr/bin/env python3


def get_words_from_sentence(sentence):
    sentence = "".join([c.lower() for c in sentence if c.isalpha() or c == " "])

    return sentence.split(" ")


def common_words(sentence_one, sentence_two):
    word_list_one, word_list_two = get_words_from_sentence(
        sentence_one
    ), get_words_from_sentence(sentence_two)

    return ", ".join(set(word_list_one) & set(word_list_two))


if __name__ == "__main__":
    for test_pair in [
        (
            "Bold Sir Robin ran away.",
            "Do you want milk with that, sir?",
        ),
        (
            "This cheese is very nice.",
            "The Nice is a much under-rated biscuit.",
        ),
        (
            "What is your favourite colour?",
            "What is your favourite cheese?",
        ),
        (
            "",
            "",
        ),
    ]:
        first, second = test_pair
        print(f"{test_pair} -> {common_words(first, second)}")
