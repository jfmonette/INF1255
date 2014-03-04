'''
Created on 2014-03-04

@author: moe
'''

'''
Vous ne trouverez pas ici de code. Vous trouverez plutôt des principes pouvant vous guider dans votre écriture de code.

Si je voulais faire de vous un ninja, je pourrais mettre à votre disposition tout un ensemble d'outils : un katana, 
des shurikens, des bombes fumigènes, etc. Toutefois, cela ferait de moi un bien mauvais maître de ne pas vous enseigner
comment les utilisez efficacement.

Il en va un peu de même si je veux faire de vous un programmeur. Je peux mettre à votre disposition tout un ensemble d'outils :
un langage de programmation, son paradigme, sa synthaxe, ses mots-clés, ses modules, etc. Encore une fois, cela ferait de moi
un mauvais maître de ne pas vous enseigner comment les utilisez efficacement.

Voici donc une courte présentation de ce que nous appelerons

Le Zen du code.
---------------
Lorsque vous nommez une variable, une fonction, un module ou quoique ce soit dans votre code, utilisez toujours un nom
qui révèle l'intention de cette chose.

Contre-exemple : int d # Temps écoulé en jours
Exemple : int temps_ecoule_en_jours
--------
Le nom d'une fonction devrait contenir un verbe.

Contre-exemple : def taxes(montant)
Exemple : def calculer_taxe(montant)
--------
Lorsque vous nommez une classe ou une variable, utilisez un nom.
--------
La première règle à respecter lorsque vous écrivez une fonction est que celle-ci doit être courte.
--------
La deuxième règle à respecter lorsque vous écrivez une fonction est que celle-ci doit être encore plus courte.
À combien de lignes de code est-ce que cette définition de courte correspond ? Il n'y a pas de chiffre magique.
Toutefois entre une et dix lignes devrait être suffisant. Surtout en python.
--------
La troisième règle à respecter lorsque vous écrivez une fonction est que celle-ci : une fonction ne devrait faire qu'une seule chose,
elle devrait bien le faire et ne faire que cela.
--------
À l'intérieur d'un module, les fonctions devraient être définies dans un ordre qui permet de les lire comme s'il s'agissait d'un roman
et non d'un livre dont vous êtes le héro. Le lecteur ne devrait, idéalement, pas à se promener de haut en bas et de bas en haut lors
de sa lecture afin de comprendre le module.
--------
Le nombre idéal de paramètres d'une fonction est zéro. Ensuite un. Puis deux. Finalement trois.
Si vous vous rendez à quatre paramètres, assurez-vous d'avoir une excellente raison.
--------
Mettre un booléen à l'intérieur des paramètres d'une fonction est mauvais. Cela indique clairement que cette fonction fait
plus qu'une seule chose.
--------
Une fonction devrait soit faire quelque chose ou retourner quelque chose. Jamais les deux en même temps.
--------
L'utilisation de commentaires représente notre échec à s'exprimer clairement avec le code. Ils sont toutefois un mal
nécessaire que l'on doit parfois se résigner à utiliser.
--------
Prenez de grandes respirations et méditez.
'''