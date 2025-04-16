class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, v, w):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[v].append(w)

        if w not in self.adjacency_list:
            self.adjacency_list[w] = []
        self.adjacency_list[w].append(v)

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")



if __name__ == "__main__":
    graph = Graph()
    while True:
        print("\n1. Add edge")
        print("2. Display graph")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            v = input("Enter the first vertex: ")
            w = input("Enter the second vertex: ")
            graph.add_edge(v, w)
        elif choice == "2":
            graph.display()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
