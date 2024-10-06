""" cette fonction transforme en ASCII et vice versa"""
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    # Parcours de la chaîne de caractères
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            # Ajoute le tuple (caractère, nombre d'occurrences)
            result.append((current_char, count))
            current_char = s[i]
            count = 1

    # N'oublie pas d'ajouter le dernier groupe
    result.append((current_char, count))

    return result




def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

    for i in range(len(s)-1):
        if s[i+1] != s[i]:
            return [(s[i], i+1)] + artcode_r(s[i+1:])
    return [(s[0], len(s))]
# Fonction de test principale pour vérifier le fonctionnement
def main():
    " fonction de test"
    test_string = "MMMMaaacXolloMM" * 100  # Chaîne beaucoup plus longue pour tester
    print("Taille de la chaîne d'entrée :", len(test_string))
    # Test de la version avec découpage
    encoded_r = artcode_r(test_string)
    print("Résultat du découpage récursif:",encoded_r[:10],"...")
    # Affiche seulement les 10 premiers tuples

# Exécuter la fonction principale pour tester
if __name__ == "__main__":
    main()
