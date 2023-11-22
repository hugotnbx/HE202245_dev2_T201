import argparse
import os
import shutil

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Le fichier {old_name} a bien été renommé {new_name}")

    except FileNotFoundError:
        print("Erreur : fichier introuvable")

def rename_folder(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Le dossier {old_name} a bien été renommé {new_name}")

    except FileNotFoundError:
        print("Erreur : dossier introuvable")

def list_content(input_dir):
    try:
        dir_content = os.listdir(input_dir)
        for element in dir_content:
            print(element)

    except FileNotFoundError:
        print("Erreur : dossier introuvable")

def move_file(input_file, destination_folder):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(input_file, destination_folder)
        print(f"Le fichier {input_file} a bien été déplacé dans le dossier {destination_folder}")

    except FileNotFoundError:
        print("Erreur : fichier introuvable")

def move_folder(input_dir, destination_folder):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(input_dir, destination_folder)
        print(f"Le dossier {input_dir} a bien été déplacé dans le dossier {destination_folder}")

    except FileNotFoundError:
        print("Erreur : dossier introuvable")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', metavar='file', help='Nom du fichier d\'entrée')
    parser.add_argument('--output_file', metavar='file', help='Nom du fichier de sortie')
    parser.add_argument('--input_dir', metavar='dir', help='Nom du dossier d\'entrée')
    parser.add_argument('--output_dir', metavar='dir', help='Nom du dossier de sortie')
    parser.add_argument('--rename', action='store_true', help='Renomme un fichier ou un dossier')
    parser.add_argument('--dir_content', action='store_true', help='Liste le contenant d\'un dossier')
    parser.add_argument('--move', action='store_true', help='Déplace un fichier ou un dossier')
    parser.add_argument('--sort_by_extension', action='store_true', help='Trie les fichiers et dossiers d\'un dossier')

    args = parser.parse_args()

    if args.input_file and args.output_file and args.rename:
        rename_file(args.input_file, args.output_file)

    if args.input_dir and args.output_dir and args.rename:
        rename_folder(args.input_dir, args.output_dir)

    if args.input_dir and args.dir_content:
        list_content(args.input_dir)

    if args.input_file and args.output_dir and args.move:
        move_file(args.input_file, args.output_dir)

    if args.input_dir and args.output_dir and args.move:
        move_file(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()

"""
input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)

    dir_content = os.listdir(input_dir)

    if args.sort_by_extension and args.input_dir and args.output_dir:
        for element in dir_content:
            split_element = element.split('.')

            if len(split_element) > 1:
                extension = split_element[1]
                element_path = os.path.join(input_dir, element)
                folder = os.path.join(output_dir, extension)

                os.makedirs(folder, exist_ok=True)
                shutil.move(element_path, os.path.join(folder, element))
"""