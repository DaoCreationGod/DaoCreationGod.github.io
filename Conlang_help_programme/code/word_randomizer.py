import os
import random

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words

def get_random_words(words_list, num_words):
    return random.sample(words_list, num_words)

def list_folders(main_path):
    folders = [item for item in os.listdir(main_path) if os.path.isdir(os.path.join(main_path, item))]
    return folders

def list_files(folder_path):
    files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
    return files

def main():
    chosen_words = set()
    main_path = "Conlang_help_programme/files/wordgroups"  # Specify the main path here

    while True:
        print("Choose an option (number):")
        print("1. Get random words from a specified sub-group (file)")
        print("2. Get random words from a whole group (folder)")
        print("3. Get random words from everything (all files in all folders)")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            folders = list_folders(main_path)
            print("Folders to choose from:")
            for idx, folder in enumerate(folders, start=1):
                print(f"{idx}. {folder}")
            
            folder_choice = int(input("Enter the number of the folder: ")) - 1
            if 0 <= folder_choice < len(folders):
                selected_folder = folders[folder_choice]
                folder_path = os.path.join(main_path, selected_folder)
                files = list_files(folder_path)
                print("Files to choose from:")
                for idx, file in enumerate(files, start=1):
                    print(f"{idx}. {file}")

                file_choice = int(input("Enter the number of the file: ")) - 1
                if 0 <= file_choice < len(files):
                    selected_file = files[file_choice]
                    file_path = os.path.join(folder_path, selected_file)
                    words = read_words_from_file(file_path)
                    num_words = min(5, len(words))
                    random_words = get_random_words(words, num_words)
                    print("Random words from the file:")
                    print(random_words)
                    chosen_words.update(random_words)
                else:
                    print("Invalid file choice.")
            else:
                print("Invalid folder choice.")
        
        elif choice == '2':
            folders = list_folders(main_path)
            print("Folders to choose from:")
            for idx, folder in enumerate(folders, start=1):
                print(f"{idx}. {folder}")
            
            folder_choice = int(input("Enter the number of the folder: ")) - 1
            if 0 <= folder_choice < len(folders):
                selected_folder = folders[folder_choice]
                folder_path = os.path.join(main_path, selected_folder)
                files = list_files(folder_path)
                selected_file = random.choice(files)
                words = read_words_from_file(os.path.join(folder_path, selected_file))
                num_words = min(5, len(words))
                random_words = get_random_words(words, num_words)
                print("Random words from the folder:")
                print(random_words)
                chosen_words.update(random_words)
            else:
                print("Invalid folder choice.")
        
        elif choice == '3':
            all_files = [os.path.join(folder_path, file) for folder, _, files in os.walk(main_path) for file in files if file.endswith(".txt")]
            words = []
            for file in all_files:
                words.extend(read_words_from_file(file))
            num_words = min(5, len(words))
            random_words = get_random_words(words, num_words)
            print("Random words from all files in all folders:")
            print(random_words)
            chosen_words.update(random_words)
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
