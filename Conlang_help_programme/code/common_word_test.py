import os

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return [word.lower() for word in words]

def main():
    folder_paths = ['Conlang_help_programme/files/wordgroups/adjectives', 'Conlang_help_programme/files/wordgroups/adverbs', 'Conlang_help_programme/files/wordgroups/articles', 'Conlang_help_programme/files/wordgroups/conjunctions', 'Conlang_help_programme/files/wordgroups/determiners', 'Conlang_help_programme/files/wordgroups/interjunctions', 'Conlang_help_programme/files/wordgroups/nouns', 'Conlang_help_programme/files/wordgroups/prepositions', 'Conlang_help_programme/files/wordgroups/pronouns', 'Conlang_help_programme/files/wordgroups/verbs']  # Provide the full paths to your folders

    folder_files = {}

    for folder_path in folder_paths:
        folder_name = os.path.basename(folder_path)
        folder_files[folder_name] = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    common_words_dict = {}

    for i, folder1 in enumerate(folder_paths):
        for j, folder2 in enumerate(folder_paths[i + 1:], start=i + 1):
            for file1 in folder_files[os.path.basename(folder1)]:
                for file2 in folder_files[os.path.basename(folder2)]:
                    file1_path = os.path.join(folder1, file1)
                    file2_path = os.path.join(folder2, file2)

                    words1 = read_words_from_file(file1_path)
                    words2 = read_words_from_file(file2_path)

                    common_words = set(words1) & set(words2)

                    for word in common_words:
                        common_words_dict.setdefault(word, []).append((file1, file2))

    print("Common words and their occurrences:")
    for word, occurrences in common_words_dict.items():
        print(f"'{word}' appears in:")
        for occurrence in occurrences:
            print(f"- {occurrence[0]} and {occurrence[1]}")

if __name__ == "__main__":
    main()
