#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    """
    finds two items whose sum of weights equals the weight limit `limit`
    """
    ht = HashTable(16)
    i = 1
    for num in range(len(weights) - 1):
        for num2 in range(len(weights)):
            id1 = 0
            id2 = 0
            if num2 > num:
                id1 = num2
                id2 = num
            elif num2 < num:
                id2 = num2
                id1 = num
            hash_table_insert(ht, weights[num] + weights[num2], (id1, id2))
    return hash_table_retrieve(ht, limit)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
