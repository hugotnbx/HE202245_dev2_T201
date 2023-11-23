import argparse
import os
import shutil

index_error_message = "\nErreur : argument manquant\n"
file_not_found_error_message = "\nErreur : fichier/dossier introuvable\n"


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
        print(f"\nLe {file_or_folder} {old_name} a bien été renommé {new_name}\n")

    except FileNotFoundError:
        print(file_not_found_error_message)


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
        print(file_not_found_error_message)
    except NotADirectoryError:
        print("\nErreur : ceci n'est pas un dossier\n")


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
        print(f"\nLe {file_or_folder} {input_item} a bien été déplacé dans le dossier {destination_folder}\n")

    except FileNotFoundError:
        print(file_not_found_error_message)


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

        print(f"\nLe {file_or_folder} {input_item} a bien été supprimé\n")

    except FileNotFoundError:
        print(file_not_found_error_message)


def main():
    command = ''
    start_message = ('\nVoici les commandes existantes :\n'
                     '- dir -> affiche le contenu du répertoire\n'
                     '- rename -> renomme un fichier/dossier\n'
                     '- move -> déplace un fichier/dossier dans un autre dossier\n'
                     '- remove -> supprime un fichier/dossier\n')

    print(start_message)

    while command != 'exit':
        command = input("Entrez une commande ou 'exit' pour quitter le programme : ")
        arguments = command.split()

        try:
            if arguments[0] == 'exit':
                print("\nVous avez quitté le programme\n")

            elif arguments[0] == 'dir':
                try:
                    list_content(arguments[1])
                except IndexError:
                    print(index_error_message)

            elif arguments[0] == 'rename':
                try:
                    rename_item(arguments[1], arguments[2])
                except IndexError:
                    print(index_error_message)

            elif arguments[0] == 'move':
                try:
                    move_item(arguments[1], arguments[2])
                except IndexError:
                    print(index_error_message)

            elif arguments[0] == 'remove':
                try:
                    remove_item(arguments[1])
                except IndexError:
                    print(index_error_message)

            else:
                print("\nCette commande n'est pas disponible")
                print(start_message)

        except IndexError:
            print("\nVous n'avez entré aucune commande\n")


if __name__ == "__main__":
    main()
