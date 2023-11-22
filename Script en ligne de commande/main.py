import argparse
import os
import shutil


def rename_item(old_name, new_name):
    """
    :pre:
    - Le nom du fichier/dossier a renommer
    - Le nouveau nom du fichier/dossier
    :post:
    - Renomme le fichier/dossier avec le nouveau nom et affiche un message de succès de l'opération
    :raises:
    - Affiche un message d'erreur si il ne trouve pas le fichier/dossier
    """
    file_or_folder = ''

    try:
        if os.path.isfile(old_name):
            file_or_folder = 'fichier'

        elif os.path.isdir(old_name):
            file_or_folder = 'dossier'

        os.rename(old_name, new_name)
        print(f"Le {file_or_folder} {old_name} a bien été renommé {new_name}")

    except FileNotFoundError:
        print(f"Erreur : fichier/dossier introuvable")


def list_content(folder):
    """
    :pre:
    - Le nom du dossier
    :post:
    - Affiche le contenu du dossier
    :raises:
    - Affiche un message d'erreur si il ne trouve pas le dossier
    - Affiche un message d'erreur si autre chose qu'un dossier est donné en paramètre
    """
    try:
        dir_content = os.listdir(folder)
        for element in dir_content:
            print(element)

    except FileNotFoundError:
        print("Erreur : dossier introuvable")
    except NotADirectoryError:
        print("Erreur : ceci n'est pas un dossier")


def move_item(input_item, destination_folder):
    """
    :pre:
    - Le nom du fichier/dossier a déplacer
    - Le nom du dossier où le fichier/dossier sera déplacé
    :post:
    - Déplace le fichier/dossier dans le dossier et affiche un message de succès de l'opération
    :raises:
    - Affiche un message d'erreur si il ne trouve pas le fichier/dossier
    """
    file_or_folder = ''

    try:
        if os.path.isfile(input_item):
            file_or_folder = 'fichier'

        elif os.path.isdir(input_item):
            file_or_folder = 'dossier'

        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(input_item, destination_folder)
        print(f"Le {file_or_folder} {input_item} a bien été déplacé dans le dossier {destination_folder}")

    except FileNotFoundError:
        print("Erreur : fichier/dossier introuvable")


def copy_item(input_item, destination_folder):
    """
    :pre:
    - Le nom du fichier a copier
    - Le nom du dossier où le fichier sera copié
    :post:
    - Créée une copie du fichier dans le dossier et affiche un message de succès de l'opération
    :raises:
    - Affiche un message d'erreur si il ne trouve pas le fichier
    """
    try:
        os.makedirs(destination_folder, exist_ok=True)
        shutil.copy(input_item, destination_folder)
        print(f"Le fichier {input_item} a bien été copié dans le dossier {destination_folder}")

    except FileNotFoundError:
        print("Erreur : fichier introuvable")


def remove_item(input_item):
    """
    :pre:
    - Le nom du fichier/dossier a supprimer
    :post:
    - Supprime le fichier/dossier et affiche un message de succès de l'opération
    :raises:
    - Affiche un message d'erreur si il ne trouve pas le fichier/dossier
    """
    file_or_folder = ''

    try:
        if os.path.isfile(input_item):
            file_or_folder = 'fichier'
            os.remove(input_item)

        elif os.path.isdir(input_item):
            file_or_folder = 'dossier'
            shutil.rmtree(input_item)

        print(f"Le {file_or_folder} {input_item} a bien été supprimé")

    except FileNotFoundError:
        print("Erreur : fichier/dossier introuvable")


def main():
    parser = argparse.ArgumentParser(description='Permet de faire toute sorte d\'opérations sur des fichiers et des dossiers')
    parser.add_argument('--input', metavar='file/dir', help='Nom du fichier/dossier d\'entrée')
    parser.add_argument('--output', metavar='file/dir', help='Nom du fichier/dossier de sortie')
    parser.add_argument('--rename', action='store_true', help='Renomme un fichier ou un dossier')
    parser.add_argument('--dir_content', action='store_true', help='Liste le contenant d\'un dossier')
    parser.add_argument('--move', action='store_true', help='Déplace un fichier ou un dossier')
    parser.add_argument('--copy', action='store_true', help='Créée une copie d\'un fichier dans un dossier')
    parser.add_argument('--remove', action='store_true', help='Supprime un fichier ou un dossier')

    args = parser.parse_args()

    if args.input and args.output and args.rename:
        rename_item(args.input, args.output)

    if args.input and args.dir_content:
        list_content(args.input)

    if args.input and args.output and args.move:
        move_item(args.input, args.output)

    if args.input and args.output and args.copy:
        copy_item(args.input, args.output)

    if args.input and args.remove:
        remove_item(args.input)


if __name__ == "__main__":
    main()
