import string


def remove_punctuation(text: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


def count_unique_words(text: str) -> dict[str, int]:
    words = {}
    for word in text.split():
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] += 1
    return words


def main() -> int:
    text = input()
    processed_text = remove_punctuation(text).replace("  ", " ")

    total_words_count = len(processed_text.split())
    unique_words_count = count_unique_words(processed_text)

    print(f"total words: {total_words_count}")
    print(f"unique words: {unique_words_count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

