[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 6.3)

Avant de commencer, consultez les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Écrire un programme qui demande 10 valeurs à un utilisateur, puis les ordonne. Vous ne pouvez pas utiliser de liste ou la fonction reversed().
2. Supprimer le énième élément
   a) d'une pile
   b) d'une file
3. Trier
   a) une pile
   b) une file
4. Itérez sur la séquence de caractères fournie. Si le caractère courant est une lettre, ajoutez-le à la file.
Sinon, enlevez un élément de la file et ajoutez ce dernier à la pile. Quel est le résultat?

### À compléter
Vous devez compléter les fonctions suivantes du fichier [exercice.py](exercice.py).

```python
def reverse_data(data: list = None):
    if data is None:
        pass

    reversed_data = None

    return reversed_data

def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    return Stack()

def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    return Queue()

def sort_stack(data: Stack) -> Stack:
    return Stack()

def sort_queue(data: Queue) -> Queue:
    return Queue()

def string_and_structs(string: str) -> tuple:
    fifo, lifo = Queue(), Stack()

    return fifo, lifo
```

### Informations utiles

Les piles (stacks) et les files (queues) utilisées dans ces exercices correspondent respectivement aux structures LifoQueue et Queue de la librairie queue (https://docs.python.org/3/library/queue.html). Je les ai un peux modifiées dans le fichier structs pour y ajouter la possibiliter de les afficher et d'ajouter plusieurs éléments à la fois.
