#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    output an array of strings with the entire route of your trip. For the above example, it should look like this:
    ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
    """
    hashtable = HashTable(length)
    route = [None] * length
    # LOOP THROUGH TICKETS ARRAY
    for i in tickets:
        # INSERT SOURCE, DESTINATION INTO HASHTABLE
        if i.source is not None:
            hash_table_insert(hashtable, i.source, i.destination)
            # HASHTABLE === [<(PIT, ORD)>, <(XNA, CID)>...]
            # FIND NONE == SOURCE
            # ADD DESTINATION TO ROUTE
            # [LAX, NONE, NONE, NONE...]
            if i.source == 'NONE':
                route[0] = i.destination
    # LOOP THROUGH ROUTE ARRAY
    for travel in range(len(route)):
    # KEY = ROUTE[I] // RETRIEVE VALUE
        if route[travel] is not None:
            next_route = hash_table_retrieve(hashtable, route[travel])
            # print(next_route)
    # PLACE VALUE IN NEXT ROUTE INDEX IF NOT NONE
        if next_route is not 'NONE' and next_route is not None:
            print(next_route)
            route[travel + 1] = next_route
    print(route[:-1])
    return route[:-1]

