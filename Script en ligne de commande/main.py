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

def copy_file(input_file, destination_folder):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.copy(input_file, destination_folder)
        print(f"Le fichier {input_file} a bien été copié dans le dossier {destination_folder}")

    except FileNotFoundError:
        print("Erreur : fichier introuvable")

def remove_file(input_file):
    try:
        os.remove(input_file)
        print(f"Le fichier {input_file} a bien été supprimé")

    except FileNotFoundError:
        print("Erreur : fichier introuvable")

def remove_folder(input_dir):
    try:
        shutil.rmtree(input_dir)
        print(f"Le dossier {input_dir} a bien été supprimé")

    except FileNotFoundError:
        print("Erreur : dossier introuvable")

def main():
    parser = argparse.ArgumentParser(description='Permet de faire toute sorte d\'opérations sur des fichiers et des dossiers')
    parser.add_argument('--input_file', metavar='file', help='Nom du fichier d\'entrée')
    parser.add_argument('--output_file', metavar='file', help='Nom du fichier de sortie')
    parser.add_argument('--input_dir', metavar='dir', help='Nom du dossier d\'entrée')
    parser.add_argument('--output_dir', metavar='dir', help='Nom du dossier de sortie')
    parser.add_argument('--rename', action='store_true', help='Renomme un fichier ou un dossier')
    parser.add_argument('--dir_content', action='store_true', help='Liste le contenant d\'un dossier')
    parser.add_argument('--move', action='store_true', help='Déplace un fichier ou un dossier')
    parser.add_argument('--copy', action='store_true', help='Créée une copie d\'un fichier ou d\'un dossier')
    parser.add_argument('--remove', action='store_true', help='Supprime un fichier ou un dossier')

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
        move_folder(args.input_dir, args.output_dir)

    if args.input_file and args.output_dir and args.copy:
        copy_file(args.input_file, args.output_dir)

    if args.input_file and args.remove:
        remove_file(args.input_file)

    if args.input_dir and args.remove:
        remove_folder(args.input_dir)

if __name__ == "__main__":
    main()
