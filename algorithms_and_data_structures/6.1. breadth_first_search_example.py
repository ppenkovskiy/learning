from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = ['s']


def person_is_seller(name):
    return 's' in name.lower()


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f"{person.capitalize()} is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    print("There's no mango sellers in your list of sellers.")
    return False


search("you")
