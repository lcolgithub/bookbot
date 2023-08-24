
def count_letters(text):
    letter_counts = {}
    for letter in text.lower():
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    return letter_counts


def get_number_words(text):
    words = text.split()
    return len(words)
    
def get_text_report(text, path_to_file):
    report = f"--- Begin report of {path_to_file} ---"
    report += f"\n {get_number_words(text)} words found in the document"
    letter_counts = count_letters(text)
    for letter in letter_counts:
        if letter.isalpha():
            report += f"\n The '{letter}' character was found {letter_counts[letter]} times"

    report += "\n--- End report ---"
    return report


def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(get_text_report(file_contents, path_to_file))

main()