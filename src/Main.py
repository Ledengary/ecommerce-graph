import matplotlib.pyplot as plt
import time
import Main
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None

class Queue:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.size = 0

    def getSize(self):
        return self.size

    def enqueue(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            if self.size == 1:
                returnable = self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return returnable.data
            else:
                next_node = self.head
                after = next_node.next
                after.last = None
                self.head = after
                self.size -= 1
                return next_node.data
        else:
            return "NULL"

    def getFirst(self):
        if self.size != 0:
            return self.head.data
        else:
            return "NULL"

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head is None and self.tail is None and self.size == 0:
            return True
        else:
            return False

    def display(self):
        the_list = [0 for x in range(self.getSize())]
        if self.getSize() == 0:
            return the_list
        counter = 0
        current_node = self.head
        while current_node is not None:
            the_list[counter] = current_node.data
            current_node = current_node.next
            counter += 1
        return the_list

class array_list_node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None

class array_list():
    def __init__(self):
        self.head = array_list_node()
        self.tail = array_list_node()
        self.size = 0

    def __len__(self):
        return self.size

    def getSize(self):
        return self.size

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = array_list_node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def update(self, index, given_data):
        counter = 0
        current_node = self.head
        while current_node is not None:
            if counter == index:
                current_node.data = given_data
                break
            current_node = current_node.next
            counter += 1

    def display(self):
        the_list = [0 for x in range(self.getSize())]
        if self.getSize() == 0:
            return the_list
        counter = 0
        current_node = self.head
        while current_node is not None:
            the_list[counter] = current_node.data
            current_node = current_node.next
            counter += 1
        return the_list

    def delete(self, value):
        if self.head.data == value:
            self.deleteFirst()
        elif self.tail.data == value:
            self.deleteLast()
        else:
            self._delete(value)

    def deleteLast(self):
        if self.size != 0:
            if self.size ==1:
                self.head = None
                self.tail = None
            else:
                last_node = self.tail
                before = last_node.last
                before.next = None
                self.tail = before
            self.size -= 1

    def deleteFirst(self):
        if self.size != 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                next_node = self.head
                after = next_node.next
                after.last = None
                self.head = after
            self.size -= 1

    def _delete(self, value):
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == value:
                last_node = current_node.last
                next_node = current_node.next
                last_node.next = next_node
                next_node.last = last_node
                self.size -= 1
                break
            current_node = current_node.next

    def sorted_list(self):
        return sorted(self.display())

    def is_in_list(self, value):
        if value in self.display():
            return True
        else:
            return False

class Vertext:
    def __init__(self, data):
        self.name = data
        self.neighbors = array_list()
        self.visited = False

    def add_neighbor(self, value):
        if self.neighbors.is_in_list(value) is False:
            self.neighbors.append(value)

    def del_neighbor(self, value):
        if self.neighbors.is_in_list(value) is True:
            self.neighbors.delete(value)

class Graph:
    def __init__(self):
        self.vertices = array_list()
        self.dfs_list = [None]
        self.bridges_list = [None]
        self.Time = 0
        self.quick_sort_time_taken = None
        self.insertion_sort_time_taken = None
        self.merge_sort_time_taken = None
        self.speed_complexitivity = None
        self.space_complexitivity = 0

    def get_vertex(self, value):
        for each_vertex in self.vertices.display():
            if each_vertex.name == value:
                return each_vertex

    def I_arraylistofvertexes_O_arrayofvertexnames(self, given_list):
        returnable_list = [0 for x in range(len(given_list))]
        counter = 0
        for each in given_list:
            returnable_list[counter] = each.name
            counter += 1
        return returnable_list

    def add_vertex(self, data):
        if data is not None and data != "":
            new_vertex = Vertext(data)
            if isinstance(new_vertex, Vertext) and new_vertex.name not in self.vertices.display():
                self.vertices.append(new_vertex)
        else:
            print("_ADD VERTEX NONE CAME")

    def add_edge(self, u_value, v_value):
        u_vertex = self.get_vertex(u_value)
        v_vertex = self.get_vertex(v_value)
        if u_vertex in self.vertices.display() and v_vertex in self.vertices.display():
            for each_vertex in self.vertices.display():
                if each_vertex == u_vertex:
                    each_vertex.add_neighbor(v_vertex)
                if each_vertex == v_vertex:
                    each_vertex.add_neighbor(u_vertex)

    def del_edge(self, element):
        element_parts = element.split("_")
        u_vertex = self.get_vertex(int(element_parts[0]))
        v_vertex = self.get_vertex(int(element_parts[1]))
        if u_vertex in self.vertices.display() and v_vertex in self.vertices.display():
            for each_vertex in self.vertices.display():
                if each_vertex == u_vertex:
                    each_vertex.del_neighbor(v_vertex)
                if each_vertex == v_vertex:
                    each_vertex.del_neighbor(u_vertex)


    def print_graph(self):
        for each_vertex in self.vertices.display():
            print(each_vertex.name, ":", self.I_arraylistofvertexes_O_arrayofvertexnames(each_vertex.neighbors.display()))

    def get_all_edges(self):
        edges = array_list()
        for each_vertex in self.vertices.display():
            for each_neighbor in each_vertex.neighbors.display():
                edges.append(str(each_vertex.name) + "_" + str(each_neighbor.name))
        return self._get_all_edges_clearance(edges.display())

    def _get_all_edges_clearance(self, given_list):
        main_list = [None] * len(given_list)
        counter = 0
        for each in given_list:
            if each not in main_list:
                each_parts = each.split("_")
                each_swapped = each_parts[1] + "_" + each_parts[0]
                if each_swapped not in main_list:
                    main_list[counter] = each
                    counter += 1
        return list(filter(None, main_list))

    def is_edge_valid(self, u, v):
        if str(u) + "_" + str(v) in self.get_all_edges() or str(v) + "_" + str(u) in self.get_all_edges():
            return True
        else:
            return False

    def bfs(self, start_value):
        answer_list = [None] * len(self.vertices.display())
        counter = 0
        start = self.get_vertex(start_value)
        queue = Queue()
        queue.enqueue(start)
        start.visited = True
        while queue.isEmpty() is False:
            this_vertex = queue.dequeue()
            answer_list[counter] = this_vertex.name
            counter += 1
            for each_neighbor in this_vertex.neighbors.display():
                if each_neighbor.visited is False:
                    queue.enqueue(each_neighbor)
                    each_neighbor.visited = True

        for each_vertex in self.vertices.display():
            each_vertex.visited = False
        return list(filter(None, answer_list))

    def dfs(self, start_value):
        self.dfs_list = [None] * len(self.vertices.display())
        self._dfs(start_value)
        for each_vertex in self.vertices.display():
            each_vertex.visited = False
        return self.dfs_list

    def _dfs(self, start_value):
        answer_list = [None] * len(self.vertices.display())
        start = self.get_vertex(start_value)
        start.visited = True
        self.dfs_list[self.dfs_list.index(None)] = start.name
        for each_neighbor in start.neighbors.display():
            if each_neighbor.visited is False:
                self._dfs(each_neighbor.name)

    def cycle_dfs_all(self, n, vert, start, count):
        vert.visited = True
        if n == 0:
            vert.visited = False
            if self.is_edge_valid(vert.name, start.name) is True:
                count = count + 1
                return count
            else:
                return count
        for i in range(len(self.vertices.display())):
            i_vertex = self.get_vertex(i)
            if i_vertex.visited is False and self.is_edge_valid(vert.name, i_vertex.name):
                count = self.cycle_dfs_all(n - 1, i_vertex, start, count)
        vert.visited = False
        return count

    def countCycles_all(self, n):
        count = 0
        for i in range(len(self.vertices.display()) - (n - 1)):
            i_vertex = self.get_vertex(i)
            count = self.cycle_dfs_all(n - 1, i_vertex, i_vertex, count)
            i_vertex.visited = True
        for each_vertex in self.vertices.display():
            each_vertex.visited = False
        return int(count / 2)

    def cycle_dfs(self, n, vert, start, count, v_name, v_visited):
        vert.visited = True
        if vert.name == v_name:
            v_visited = True
        if n == 0:
            vert.visited = False
            if self.is_edge_valid(vert.name, start.name) is True:
                if v_visited is True:
                    count = count + 1
                return count
            else:
                return count
        for i in range(len(self.vertices.display())):
            i_vertex = self.get_vertex(i)
            if i_vertex.visited is False and self.is_edge_valid(vert.name, i_vertex.name):
                count = self.cycle_dfs(n - 1, i_vertex, start, count, v_name, v_visited)
        vert.visited = False
        return count

    def countCycles(self, n, u_name, v_name):
        count = 0
        u_vertex = self.get_vertex(u_name)
        count = self.cycle_dfs(n - 1, u_vertex, u_vertex, count, v_name, False)
        u_vertex.visited = True
        for each_vertex in self.vertices.display():
            each_vertex.visited = False
        return int(count / 2)

    def find_degree(self, name):
        counter = 0
        u_vertex = self.get_vertex(name)
        edges_list = self.get_all_edges()
        for each_edge in edges_list:
            each_edge_part = each_edge.split("_")
            if int(each_edge_part[1]) == name:
                counter += 1
            if int(each_edge_part[0]) == name:
                counter += 1
        return counter

    def calculate_edge_score(self, u_name, v_name):
        if self.is_edge_valid(u_name, v_name) is True:
            u_vertex = self.get_vertex(u_name)
            v_vertex = self.get_vertex(v_name)
            zij = self.countCycles(3, u_name, v_name)
            ki = self.find_degree(u_name)
            kj = self.find_degree(v_name)
            down = (min(ki - 1, kj - 1))
            if down != 0:
                cij = (zij + 1) / (min(ki - 1, kj - 1))
            else:
                cij = 1000000
            return cij
        else:
            print("INVALID EDGE !")
            return -1

    def _bridges(self, u, visited, parent, low, disc):
        visited[u] = True
        u_vertex = self.get_vertex(u)
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        for each_neighbor in u_vertex.neighbors.display():
            v = each_neighbor.name
            if visited[v] is False:
                parent[v] = u
                self._bridges(v, visited, parent, low, disc)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    self.bridges_list[self.bridges_list.index(None)] = str(u) + "_" + str(v)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridges(self):
        self.bridges_list = [None] * len(self.vertices.display())
        visited = [False] * (len(self.vertices.display()))
        disc = [float("Inf")] * (len(self.vertices.display()))
        low = [float("Inf")] * (len(self.vertices.display()))
        parent = [-1] * (len(self.vertices.display()))
        for i in range(len(self.vertices.display())):
            if visited[i] is False:
                self._bridges(i, visited, parent, low, disc)
        self.Time = 0
        return list(filter(None, self.bridges_list))

    def _articulation_points(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        u_vertex = self.get_vertex(u)
        for each_neighbor in u_vertex.neighbors.display():
            v = each_neighbor.name
            if visited[v] is False:
                parent[v] = u
                children += 1
                self._articulation_points(v, visited, ap, parent, low, disc)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def articulation_points(self):
        visited = [False] * (len(self.vertices.display()))
        disc = [float("Inf")] * (len(self.vertices.display()))
        low = [float("Inf")] * (len(self.vertices.display()))
        parent = [-1] * (len(self.vertices.display()))
        ap = [False] * (len(self.vertices.display()))
        for i in range(len(self.vertices.display())):
            if visited[i] is False:
                self._articulation_points(i, visited, ap, parent, low, disc)
        points = [None for x in range(len(ap))]
        for index, value in enumerate(ap):
            if value is True:
                points[points.index(None)] = index
        answer = array_list()
        for each in points:
            if each is not None:
                answer.append(each)

        return answer.display()

    def connectivity_bfs(self, start_value):
        start = self.get_vertex(start_value)
        queue = Queue()
        queue.enqueue(start)
        start.visited = True
        while queue.isEmpty() is False:
            this_vertex = queue.dequeue()
            for each_neighbor in this_vertex.neighbors.display():
                if each_neighbor.visited is False:
                    queue.enqueue(each_neighbor)
                    each_neighbor.visited = True

class Graph_Matrix:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = [[0 for x in range(dimension)] for y in range(dimension)]
        # self.visited_matrix = [[0 for x in range(dimension)] for y in range(dimension)]
        self.dfs_list = [None]
        self.visited_list = array_list()
        self.bridges_list = [None]
        self.Time = 0
        self.quick_sort_time_taken = None
        self.insertion_sort_time_taken = None
        self.merge_sort_time_taken = None
        self.speed_complexitivity = None
        self.space_complexitivity = 0
        self.setting_up()

    def setting_up(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.matrix[i][j] = 0
                # self.visited_matrix[i][j] = 0

    def add_edge(self, u_value, v_value):
        self.matrix[u_value][v_value] = 1
        self.matrix[v_value][u_value] = 1

    def del_edge(self, element):
        element_parts = element.split("_")
        u_value = int(element_parts[0])
        v_value = int(element_parts[1])
        self.matrix[u_value][v_value] = 0
        self.matrix[v_value][u_value] = 0

    def print_graph(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.matrix[i][j], end=' ')
            print()

    def get_all_edges(self):
        edges_list = [None] * (self.dimension * self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matrix[i][j] == 1:
                    edges_list[edges_list.index(None)] = str(i) + "_" + str(j)
        return self._get_all_edges_clearance(list(filter(None, edges_list)))

    def _get_all_edges_clearance(self, given_list):
        main_list = [None] * len(given_list)
        counter = 0
        for each in given_list:
            if each not in main_list:
                each_parts = each.split("_")
                each_swapped = each_parts[1] + "_" + each_parts[0]
                if each_swapped not in main_list:
                    main_list[counter] = each
                    counter += 1
        return list(filter(None, main_list))

    def is_edge_valid(self, u, v):
        if str(u) + "_" + str(v) in self.get_all_edges() or str(v) + "_" + str(u) in self.get_all_edges():
            return True
        else:
            return False

    def find_neighbors(self, u):
        neighbors_list = [None] * self.dimension
        for j in range(self.dimension):
            if self.matrix[u][j] == 1:
                neighbors_list[neighbors_list.index(None)] = j

        neighbors_list = list(filter(lambda x: x is not None, neighbors_list))
        return neighbors_list

    def bfs(self, start):
        answer_list = [None] * self.dimension
        visited_list = array_list()
        counter = 0
        queue = Queue()
        queue.enqueue(start)
        visited_list.append(start)
        while queue.isEmpty() is False:
            this_vertex = queue.dequeue()
            answer_list[counter] = this_vertex
            counter += 1
            for each_neighbor in self.find_neighbors(this_vertex):
                if visited_list.is_in_list(each_neighbor) is False:
                    queue.enqueue(each_neighbor)
                    visited_list.append(each_neighbor)
        answer_list = list(filter(lambda x: x is not None, answer_list))
        return answer_list

    def dfs(self, start_value):
        self.dfs_list = [None] * self.dimension
        self.visited_list.clear()
        self._dfs(start_value)
        self.visited_list.clear()
        return self.dfs_list

    def _dfs(self, start):
        self.visited_list.append(start)
        self.dfs_list[self.dfs_list.index(None)] = start
        for each_neighbor in self.find_neighbors(start):
            if self.visited_list.is_in_list(each_neighbor) is False:
                self._dfs(each_neighbor)

    def cycle_dfs_all(self, n, vert, start, count):
        self.visited_list.append(vert)
        if n == 0:
            self.visited_list.delete(vert)
            if self.is_edge_valid(vert, start) is True:
                count = count + 1
                return count
            else:
                return count
        for i_vertex in range(self.dimension):
            if self.visited_list.is_in_list(i_vertex) is False and self.is_edge_valid(vert, i_vertex):
                count = self.cycle_dfs_all(n - 1, i_vertex, start, count)
        self.visited_list.delete(vert)
        return count

    def countCycles_all(self, n):
        self.visited_list.clear()
        count = 0
        for i in range(self.dimension - (n - 1)):
            i_vertex = i
            count = self.cycle_dfs_all(n - 1, i_vertex, i_vertex, count)
            self.visited_list.append(i_vertex)
        for each_vertex in range(self.dimension):
            if self.visited_list.is_in_list(each_vertex):
                self.visited_list.delete(each_vertex)
        self.visited_list.clear()
        return int(count / 2)

    def cycle_dfs(self, n, vert, start, count, v_name, v_visited):
        self.visited_list.append(vert)
        if vert == v_name:
            v_visited = True
        if n == 0:
            self.visited_list.delete(vert)
            if self.is_edge_valid(vert, start) is True:
                if v_visited is True:
                    count = count + 1
                return count
            else:
                return count
        for i_vertex in range(self.dimension):
            if self.visited_list.is_in_list(i_vertex) is False and self.is_edge_valid(vert, i_vertex):
                count = self.cycle_dfs(n - 1, i_vertex, start, count, v_name, v_visited)
        self.visited_list.delete(vert)
        return count

    def countCycles(self, n, u_vertex, v_vertex):
        self.visited_list.clear()
        count = 0
        count = self.cycle_dfs(n - 1, u_vertex, u_vertex, count, v_vertex, False)
        self.visited_list.append(u_vertex)
        self.visited_list.clear()
        return int(count / 2)

    def find_degree(self, vert):
        counter = 0
        for j in range(self.dimension):
            if self.matrix[vert][j] == 1:
                counter += 1
        return counter

    def calculate_edge_score(self, u_vertex, v_vertex):
        if self.is_edge_valid(u_vertex, v_vertex) is True:
            zij = self.countCycles(3, u_vertex, v_vertex)
            ki = self.find_degree(u_vertex)
            kj = self.find_degree(v_vertex)
            down = (min(ki - 1, kj - 1))
            if down != 0:
                cij = (zij + 1) / (min(ki - 1, kj - 1))
            else:
                cij = 1000000
            return cij
        else:
            print("INVALID EDGE !")
            return -1

    def _bridges(self, u_vertex, visited, parent, low, disc):
        u = u_vertex
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        for each_neighbor in self.find_neighbors(u_vertex):
            v = each_neighbor
            if visited[v] is False:
                parent[v] = u
                self._bridges(v, visited, parent, low, disc)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    self.bridges_list[self.bridges_list.index(None)] = str(u) + "_" + str(v)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridges(self):
        self.bridges_list = [None] * self.dimension
        visited = [False] * self.dimension
        disc = [float("Inf")] * self.dimension
        low = [float("Inf")] * self.dimension
        parent = [-1] * self.dimension
        for i in range(self.dimension):
            if visited[i] is False:
                self._bridges(i, visited, parent, low, disc)
        self.Time = 0
        self.bridges_list = list(filter(lambda x: x is not None, self.bridges_list))
        return self.bridges_list

    def _articulation_points(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        u_vertex = u
        for each_neighbor in self.find_neighbors(u_vertex):
            v = each_neighbor
            if visited[v] is False:
                parent[v] = u
                children += 1
                self._articulation_points(v, visited, ap, parent, low, disc)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def articulation_points(self):
        visited = [False] * self.dimension
        disc = [float("Inf")] * self.dimension
        low = [float("Inf")] * self.dimension
        parent = [-1] * self.dimension
        ap = [False] * self.dimension
        for i in range(self.dimension):
            if visited[i] is False:
                self._articulation_points(i, visited, ap, parent, low, disc)
        points = [None for x in range(len(ap))]
        for index, value in enumerate(ap):
            if value is True:
                points[points.index(None)] = index
        answer = array_list()
        for each in points:
            if each is not None:
                answer.append(each)

        return answer.display()

    def connectivity_bfs(self, start):
        self.visited_list.clear()
        queue = Queue()
        queue.enqueue(start)
        self.visited_list.append(start)
        while queue.isEmpty() is False:
            this_vertex = queue.dequeue()
            for each_neighbor in self.find_neighbors(this_vertex):
                if self.visited_list.is_in_list(each_neighbor) is False:
                    queue.enqueue(each_neighbor)
                    self.visited_list.append(each_neighbor)


def cij_value_getter(element):
    element_parts = element.split("/")
    return float(element_parts[0])


def partition_main(cij_scores_for_all_edges, low, high):
    i = (low - 1)
    pivot = cij_value_getter(cij_scores_for_all_edges[high])
    for j in range(low, high):
        if cij_value_getter(cij_scores_for_all_edges[j]) <= pivot:
            i = i + 1
            cij_scores_for_all_edges[i], cij_scores_for_all_edges[j] = cij_scores_for_all_edges[j], cij_scores_for_all_edges[i]
    cij_scores_for_all_edges[i + 1], cij_scores_for_all_edges[high] = cij_scores_for_all_edges[high], cij_scores_for_all_edges[i + 1]
    return (i + 1)

def quickSort_main(cij_scores_for_all_edges, low, high):
    if low < high:
        pi = partition_main(cij_scores_for_all_edges, low, high)
        quickSort_main(cij_scores_for_all_edges, low, pi - 1)
        quickSort_main(cij_scores_for_all_edges, pi + 1, high)


def partition(the_list, low, high):
    i = (low - 1)
    pivot = cij_value_getter(the_list[high])
    for j in range(low, high):
        if cij_value_getter(the_list[j]) <= pivot:
            i = i + 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
            the_list[i + 1], the_list[high] = the_list[high], the_list[i + 1]
    return (i + 1)

def quickSort(the_list, low, high, main_graph):
    if low < high:
        pi = partition(the_list, low, high)
        quickSort(the_list, low, pi - 1, main_graph)
        quickSort(the_list, pi + 1, high, main_graph)

def insertionSort(the_list):
    for i in range(1, len(the_list)):
        key = cij_value_getter(the_list[i])
        key_edges = the_list[i][the_list[i].find("/") + 1:]
        j = i - 1
        while j >= 0 and key < cij_value_getter(the_list[j]):
            the_list[j + 1] = the_list[j]
            j -= 1
            the_list[j + 1] = str(key) + "/" + key_edges

def mergeSort(the_list):
    if len(the_list) > 1:
        mid = len(the_list) // 2
        L = the_list[:mid]
        R = the_list[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if cij_value_getter(L[i]) < cij_value_getter(R[j]):
                the_list[k] = L[i]
                i += 1
            else:
                the_list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            the_list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            the_list[k] = R[j]
            j += 1
            k += 1

def first_step(main_graph):
    # calculating the cijs for each edge in the given graphs based on the given rules
    main_graph.print_graph()
    for each_edge in main_graph.get_all_edges():
        each_edge_parts = each_edge.split("_")
        cij_scores_for_all_edges[cij_scores_for_all_edges.index(None)] = str(main_graph.calculate_edge_score(int(each_edge_parts[0]), int(each_edge_parts[1]))) \
        + "/" + str(each_edge)

def second_step(main_graph):
    # in the second step we sort the given list from first step
    qs_list = tuple(cij_scores_for_all_edges * 40)
    is_list = tuple(cij_scores_for_all_edges * 40)
    ms_list = tuple(cij_scores_for_all_edges * 40)
    quickSort_main(cij_scores_for_all_edges, 0, len(cij_scores_for_all_edges) - 1)
    qs_list = list(qs_list)
    is_list = list(is_list)
    ms_list = list(ms_list)
    qs_start = time.time()
    quickSort(qs_list, 0, len(qs_list) - 1, main_graph)
    qs_finish = time.time()
    is_start = time.time()
    insertionSort(is_list)
    is_finish = time.time()
    ms_start = time.time()
    mergeSort(ms_list)
    ms_finish = time.time()
    main_graph.quick_sort_time_taken = qs_finish - qs_start
    main_graph.insertion_sort_time_taken = is_finish - is_start
    main_graph.merge_sort_time_taken = ms_finish - ms_start
    # x_list = ["QUICK SORT", "INSERTION SORT", "MERGE SORT"]
    # y_list = [qs_finish - qs_start, is_finish - is_start, ms_finish - ms_start]
    # plt.bar(x_list, y_list, align='center')
    # plt.show()

def third_step(main_graph):
    # the theory is that the smallest shall be deletted but the thing is that we have to consider edges with the same
    # value which depends on factors like being connected into an articulation point vertex in te graph or being a
    # bridge edge
    print("Cij :", cij_scores_for_all_edges)
    if len(cij_scores_for_all_edges) == 0:
        return
    min = cij_value_getter(cij_scores_for_all_edges[0])
    # cij_scores_for_all_edges[1] = "1.0/3_4"
    mutual_list = array_list()
    if isinstance(main_graph, Graph):
        main_graph.space_complexitivity += len(main_graph.vertices.display())
    else:
        main_graph.space_complexitivity += main_graph.dimension
    for each in cij_scores_for_all_edges:
        if cij_value_getter(each) == min:
            mutual_list.append(each)

    if len(mutual_list.display()) == 1:
        print("BEFORE :", cij_scores_for_all_edges)
        cij_scores_for_all_edges.remove(mutual_list.display()[0])
        print("AFTER :", cij_scores_for_all_edges)
        main_graph.del_edge(mutual_list.display()[0][mutual_list.display()[0].find("/") + 1:])
        print("DELETED 0")
    else:
        mutual_bridged_list = array_list()
        if isinstance(main_graph, Graph):
            main_graph.space_complexitivity += len(main_graph.vertices.display())
        else:
            main_graph.space_complexitivity += main_graph.dimension
        for each in mutual_list.display():
            if each[each.find("/") + 1:] in main_graph.bridges():
                mutual_bridged_list.append(each)
        if len(mutual_bridged_list.display()) == 0:
            del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_list.display()[0])]
            main_graph.del_edge(mutual_list.display()[0][mutual_list.display()[0].find("/") + 1:])
        elif len(mutual_bridged_list.display()) == 1:
            del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_list.display()[0])]
            main_graph.del_edge(mutual_bridged_list.display()[0][mutual_bridged_list.display()[0].find("/") + 1:])
            print("DELETED 1")
        else:
            mutual_bridged_articulared_list = array_list()
            if isinstance(main_graph, Graph):
                main_graph.space_complexitivity += len(main_graph.vertices.display())
            else:
                main_graph.space_complexitivity += main_graph.dimension
            for each in mutual_bridged_list.display():
                each_parts = each[each.find("/") + 1:].split("_")
                if int(each_parts[0]) in main_graph.articulation_points():
                    mutual_bridged_articulared_list.append(each)
            if len(mutual_bridged_articulared_list.display()) == 0:
                del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_list.display()[0])]
                main_graph.del_edge(mutual_bridged_list.display()[0][mutual_bridged_list.display()[0].find("/") + 1:])
                print("DELETED 2")
            elif len(mutual_bridged_articulared_list.display()) == 1:
                del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_articulared_list.display()[0])]
                main_graph.del_edge(mutual_bridged_articulared_list.display()[0][mutual_bridged_articulared_list.display()[0].find("/") + 1:])
                print("DELETED 3")
            else:
                del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_articulared_list.display()[0])]
                main_graph.del_edge(mutual_bridged_articulared_list.display()[0][mutual_bridged_articulared_list.display()[0].find("/") + 1:])
                print("DELETED 4")
    print("Cij :", cij_scores_for_all_edges)

def fourth_step(main_graph):
    # my fourth step has two types, if necessary it'll go deeper in order to find all the groups inside a graph,
    # if not then only A and B is enough !
    if isinstance(main_graph, Graph):
        groups = [None] * len(main_graph.vertices.display())
        seen = array_list()
        if isinstance(main_graph, Graph):
            main_graph.space_complexitivity += len(main_graph.vertices.display()) * 2
        else:
            main_graph.space_complexitivity += main_graph.dimension * 2
        for each_vertex in main_graph.vertices.display():
            each_vertex.visited = False
        bfs_count = 0
        group_counter = 0
        for each_vertex in main_graph.vertices.display():
            if each_vertex.visited is False:
                main_graph.connectivity_bfs(each_vertex.name)
                for each_inner_vertex in main_graph.vertices.display():
                    if each_inner_vertex.visited is True and seen.is_in_list(each_inner_vertex.name) is False:
                        groups[group_counter] = "#" + str(each_inner_vertex.name) + " : " + str(chr(bfs_count + 65))
                        seen.append(each_inner_vertex.name)
                        group_counter += 1
                bfs_count += 1
        print("BFS COUNTER :", bfs_count)
        if bfs_count > 1:
            for each in groups:
                print(each)
            return True
        else:
            if len(cij_scores_for_all_edges) == 0:
                for each in groups:
                    print(each)
                return True
            return False
    else:
        groups = [None] * main_graph.dimension
        seen = array_list()
        if isinstance(main_graph, Graph):
            main_graph.space_complexitivity += len(main_graph.vertices.display()) * 2
        else:
            main_graph.space_complexitivity += main_graph.dimension * 2
        main_graph.visited_list.clear()
        bfs_count = 0
        group_counter = 0
        for each_vertex in range(main_graph.dimension):
            if main_graph.visited_list.is_in_list(each_vertex) is False:
                main_graph.connectivity_bfs(each_vertex)
                for each_inner_vertex in range(main_graph.dimension):
                    if main_graph.visited_list.is_in_list(each_inner_vertex) is True and seen.is_in_list(each_inner_vertex) is False:
                        groups[group_counter] = "#" + str(each_inner_vertex) + " : " + str(chr(bfs_count + 65))
                        seen.append(each_inner_vertex)
                        group_counter += 1
                bfs_count += 1
        print("BFS COUNTER :", bfs_count)
        if bfs_count > 1:
            for each in groups:
                print(each)
            return True
        else:
            if len(cij_scores_for_all_edges) == 0:
                for each in groups:
                    print(each)
                return True
            return False

def check_if_deletion_is_eligible(main_graph, line, first_edge_deletion):
    if first_edge_deletion is False:
        line_parts = line.split("_")
        u = int(line_parts[0])
        v = int(line_parts[1])
        cycle_counts = 0
        cycle = 3
        if isinstance(main_graph, Graph):
            while cycle <= len(main_graph.vertices.display()):
                cycle_counts += main_graph.countCycles(cycle, u, v)
                print(cycle_counts, "came for", line)
                cycle += 1
        elif isinstance(main_graph, Graph_Matrix):
            while cycle <= main_graph.dimension:
                cycle_counts += main_graph.countCycles(cycle, u, v)
                cycle += 1
        if cycle_counts > 0:
            return False
        return True
    else:
        if isinstance(main_graph, Graph):
            if len(main_graph.vertices.display()) <= 3:
                return False
        elif isinstance(main_graph, Graph_Matrix):
            if main_graph.dimension <= 3:
                return False
        return True


def third_step_plus(main_graph, first_time):
    print("Cij :", cij_scores_for_all_edges)
    if len(cij_scores_for_all_edges) > 0:
        min = cij_value_getter(cij_scores_for_all_edges[0])
    else:
        return "DONE"
    # cij_scores_for_all_edges[1] = "1.0/3_4"
    mutual_list = array_list()
    if isinstance(main_graph, Graph):
        main_graph.space_complexitivity += len(main_graph.vertices.display())
    else:
        main_graph.space_complexitivity += main_graph.dimension
    for each in cij_scores_for_all_edges:
        if cij_value_getter(each) == min:
            mutual_list.append(each)

    if len(mutual_list.display()) == 1:
        if check_if_deletion_is_eligible(main_graph, mutual_list.display()[0][mutual_list.display()[0].find("/") + 1:], first_time) is True:
            print("BEFORE :", cij_scores_for_all_edges)
            cij_scores_for_all_edges.remove(mutual_list.display()[0])
            print("AFTER :", cij_scores_for_all_edges)
            main_graph.del_edge(mutual_list.display()[0][mutual_list.display()[0].find("/") + 1:])
            print("DELETED 0")
        else:
            return "DONE"
    else:
        mutual_bridged_list = array_list()
        if isinstance(main_graph, Graph):
            main_graph.space_complexitivity += len(main_graph.vertices.display())
        else:
            main_graph.space_complexitivity += main_graph.dimension
        for each in mutual_list.display():
            if each[each.find("/") + 1:] in main_graph.bridges():
                mutual_bridged_list.append(each)
        if len(mutual_bridged_list.display()) == 0:
            if check_if_deletion_is_eligible(main_graph, mutual_list.display()[0][mutual_list.display()[0].find("/") + 1:], first_time) is True:
                del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_list.display()[0])]
                main_graph.del_edge(mutual_list.display()[0][mutual_list.display()[0].find("/") + 1:])
            else:
                return "DONE"
        elif len(mutual_bridged_list.display()) == 1:
            if check_if_deletion_is_eligible(main_graph, mutual_bridged_list.display()[0][mutual_bridged_list.display()[0].find("/") + 1:], first_time) is True:
                del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_list.display()[0])]
                main_graph.del_edge(mutual_bridged_list.display()[0][mutual_bridged_list.display()[0].find("/") + 1:])
                print("DELETED 1")
            else:
                return "DONE"
        else:
            mutual_bridged_articulared_list = array_list()
            if isinstance(main_graph, Graph):
                main_graph.space_complexitivity += len(main_graph.vertices.display())
            else:
                main_graph.space_complexitivity += main_graph.dimension
            for each in mutual_bridged_list.display():
                each_parts = each[each.find("/") + 1:].split("_")
                if int(each_parts[0]) in main_graph.articulation_points():
                    mutual_bridged_articulared_list.append(each)
            if len(mutual_bridged_articulared_list.display()) == 0:
                if check_if_deletion_is_eligible(main_graph, mutual_bridged_list.display()[0][mutual_bridged_list.display()[0].find("/") + 1:], first_time) is True:
                    del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_list.display()[0])]
                    main_graph.del_edge(mutual_bridged_list.display()[0][mutual_bridged_list.display()[0].find("/") + 1:])
                    print("DELETED 2")
                else:
                    return "DONE"
            elif len(mutual_bridged_articulared_list.display()) == 1:
                if check_if_deletion_is_eligible(main_graph, mutual_bridged_articulared_list.display()[0][mutual_bridged_articulared_list.display()[0].find("/") + 1:], first_time) is True:
                    del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_articulared_list.display()[0])]
                    main_graph.del_edge(mutual_bridged_articulared_list.display()[0][mutual_bridged_articulared_list.display()[0].find("/") + 1:])
                    print("DELETED 3")
                    return "DONE"
            else:
                if check_if_deletion_is_eligible(main_graph, mutual_bridged_articulared_list.display()[0][mutual_bridged_articulared_list.display()[0].find("/") + 1:], first_time) is True:
                    del cij_scores_for_all_edges[cij_scores_for_all_edges.index(mutual_bridged_articulared_list.display()[0])]
                    main_graph.del_edge(mutual_bridged_articulared_list.display()[0][mutual_bridged_articulared_list.display()[0].find("/") + 1:])
                    print("DELETED 4")
                else:
                    return "DONE"
    print("Cij :", cij_scores_for_all_edges)
    return "UNDONE"

def fourth_step_plus(main_graph):
    if isinstance(main_graph, Graph):
        groups = [None] * len(main_graph.vertices.display())
        seen = array_list()
        if isinstance(main_graph, Graph):
            main_graph.space_complexitivity += len(main_graph.vertices.display()) * 2
        else:
            main_graph.space_complexitivity += main_graph.dimension * 2
        for each_vertex in main_graph.vertices.display():
            each_vertex.visited = False
        bfs_count = 0
        group_counter = 0
        for each_vertex in main_graph.vertices.display():
            if each_vertex.visited is False:
                main_graph.connectivity_bfs(each_vertex.name)
                for each_inner_vertex in main_graph.vertices.display():
                    if each_inner_vertex.visited is True and seen.is_in_list(each_inner_vertex.name) is False:
                        groups[group_counter] = "#" + str(each_inner_vertex.name) + " : " + str(chr(bfs_count + 65))
                        seen.append(each_inner_vertex.name)
                        group_counter += 1
                bfs_count += 1
        print("BFS COUNTER :", bfs_count)
        for each in groups:
            print(each)

    else:
        groups = [None] * main_graph.dimension
        seen = array_list()
        if isinstance(main_graph, Graph):
            main_graph.space_complexitivity += len(main_graph.vertices.display()) * 2
        else:
            main_graph.space_complexitivity += main_graph.dimension * 2
        main_graph.visited_list.clear()
        bfs_count = 0
        group_counter = 0
        for each_vertex in range(main_graph.dimension):
            if main_graph.visited_list.is_in_list(each_vertex) is False:
                main_graph.connectivity_bfs(each_vertex)
                for each_inner_vertex in range(main_graph.dimension):
                    if main_graph.visited_list.is_in_list(each_inner_vertex) is True and seen.is_in_list(each_inner_vertex) is False:
                        groups[group_counter] = "#" + str(each_inner_vertex) + " : " + str(chr(bfs_count + 65))
                        seen.append(each_inner_vertex)
                        group_counter += 1
                bfs_count += 1
        print("BFS COUNTER :", bfs_count)
        for each in groups:
            print(each)

def first_phase(main_graph):
    #in the first phase if necessary we send it to the second first phase function, each contains 5 steps but for +
    # it'll be a different recusive function
    first_step(main_graph)
    second_step(main_graph)
    third_step(main_graph)
    if fourth_step(main_graph) is False:
        for i in range(len(cij_scores_for_all_edges)):
            cij_scores_for_all_edges[i] = None
        first_phase(main_graph)

def first_phase_plus(main_graph, first_time):
    first_step(main_graph)
    second_step(main_graph)
    if third_step_plus(main_graph, first_time) == "DONE":
        fourth_step_plus(main_graph)
    else:
        for i in range(len(cij_scores_for_all_edges)):
            cij_scores_for_all_edges[i] = None
        first_phase_plus(main_graph, False)

def start_from_second_phase(chain_graph, matrix_graph, chain_graph_plus, matrix_graph_plus):
    print("=========================== MAIN GRAPH CHAIN ===================================")
    Main.cij_scores_for_all_edges = [None] * len(chain_graph.get_all_edges())
    first_phase(chain_graph)
    print("========================= MAIN GRAPH CHAIN PLUS =================================")
    Main.cij_scores_for_all_edges = [None] * len(chain_graph_plus.get_all_edges())
    first_phase_plus(chain_graph_plus, True)
    print("=========================== MAIN GRAPH MATRIX ===================================")
    Main.cij_scores_for_all_edges = [None] * len(matrix_graph.get_all_edges())
    first_phase(matrix_graph)
    print("======================== MAIN GRAPH MATRIX PLUS ================================")
    Main.cij_scores_for_all_edges = [None] * len(matrix_graph_plus.get_all_edges())
    first_phase_plus(matrix_graph_plus, True)

# main_graph = Graph()
# main_graph.add_vertex(0)
# main_graph.add_vertex(1)
# main_graph.add_vertex(2)
# main_graph.add_vertex(3)
# main_graph.add_vertex(4)
# main_graph.add_vertex(5)
# main_graph.add_edge(3, 2)
# main_graph.add_edge(3, 1)
# main_graph.add_edge(3, 4)
# main_graph.add_edge(3, 5)
# main_graph.add_edge(2, 1)
# main_graph.add_edge(1, 4)
# main_graph.add_edge(4, 5)
# print(main_graph.countCycles(3, 3, 1))
# # print("BRIDGES :", main_graph.bridges())
# # print("ARTICULAR POINTS :", main_graph.articulation_points())
# print(main_graph.countCycles_all(6))

# main_graph = Graph_Matrix(5)
# main_graph.add_edge(2, 1)
# main_graph.add_edge(2, 0)
# main_graph.add_edge(2, 3)
# main_graph.add_edge(2, 4)
# main_graph.add_edge(1, 0)
# main_graph.add_edge(0, 3)
# main_graph.add_edge(3, 4)
# cij_scores_for_all_edges = [None] * 7
# first_phase(main_graph)

# chain_graph = Graph()
# chain_graph.add_vertex(0)
# chain_graph.add_vertex(1)
# chain_graph.add_vertex(2)
# chain_graph.add_vertex(3)
# chain_graph.add_vertex(4)
# chain_graph.add_edge(0, 1)
# chain_graph.add_edge(0, 2)
# chain_graph.add_edge(0, 3)
# chain_graph.add_edge(0, 4)
# chain_graph.print_graph()
# print(chain_graph.articulation_points())
# cij_scores_for_all_edges = [None] * 4
# first_phase(chain_graph)
# print("===============================================")
# matrix_graph = Graph_Matrix(5)
# matrix_graph.add_edge(0, 1)
# matrix_graph.add_edge(0, 2)
# matrix_graph.add_edge(0, 3)
# matrix_graph.add_edge(0, 4)
# matrix_graph.print_graph()
# print(matrix_graph.articulation_points())
# cij_scores_for_all_edges = [None] * 4
# first_phase(matrix_graph)

# print("PRINT GRAPH :")
# main_graph.print_graph()
# print("PRINT ALL EDGES :")
# print(main_graph.get_all_edges())
# print("BFS :")
# print(main_graph.bfs(1))
# print("DFS :")
# print(main_graph.dfs(1))
# print("FIND CYCLE :")
# print(main_graph.countCycles(4, 3, 4))
# print("FIND ALL CYCLES :")
# print(main_graph.countCycles_all(3))
# print("FIND DEGREE :")
# print(main_graph.find_degree(3))
# print("PRINT EDGE SCORE :")
# print(main_graph.calculate_edge_score(1, 2))
if __name__ == '__main__':
    main_line = input()
    main_graph_chain = Graph()
    main_graph_chain_plus = Graph()
    main_line_parts = main_line.split(" ")
    n = int(main_line_parts[0])
    m = int(main_line_parts[1])
    for i in range(n):
        main_graph_chain.add_vertex(i)
        main_graph_chain_plus.add_vertex(i)
    main_graph_matrix = Graph_Matrix(n)
    main_graph_matrix_plus = Graph_Matrix(n)
    for i in range(m):
        line = input()
        line_parts = line.split(" ")
        main_graph_chain.add_edge(int(line_parts[0]), int(line_parts[1]))
        main_graph_chain_plus.add_edge(int(line_parts[0]), int(line_parts[1]))
        main_graph_matrix.add_edge(int(line_parts[0]), int(line_parts[1]))
        main_graph_matrix_plus.add_edge(int(line_parts[0]), int(line_parts[1]))
    cij_scores_for_all_edges = [None] * m
    print("=========================== MAIN GRAPH CHAIN ===================================")
    start = time.time()
    first_phase(main_graph_chain)
    finish = time.time()
    main_graph_chain.speed_complexitivity = finish - start
    cij_scores_for_all_edges = [None] * m
    print("========================= MAIN GRAPH CHAIN PLUS =================================")
    start = time.time()
    first_phase_plus(main_graph_chain_plus, True)
    finish = time.time()
    main_graph_chain_plus.speed_complexitivity = finish - start
    cij_scores_for_all_edges = [None] * m
    print("=========================== MAIN GRAPH MATRIX ===================================")
    start = time.time()
    first_phase(main_graph_matrix)
    finish = time.time()
    main_graph_matrix.speed_complexitivity = finish - start
    cij_scores_for_all_edges = [None] * m
    print("======================== MAIN GRAPH MATRIX PLUS ================================")
    start = time.time()
    first_phase_plus(main_graph_matrix_plus, True)
    finish = time.time()
    main_graph_matrix_plus.speed_complexitivity = finish - start

    fig = plt.figure(figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    time_comparison = fig.add_subplot(233)
    bx1 = fig.add_subplot(234)
    bx2 = fig.add_subplot(235)
    space_comparison = fig.add_subplot(236)
    x_line = ["QUICK", "INSERTION", "MERGE"]
    y_values_ax1 = [main_graph_chain.quick_sort_time_taken, main_graph_chain.insertion_sort_time_taken, main_graph_chain.merge_sort_time_taken]
    y_values_ax2 = [main_graph_matrix.quick_sort_time_taken, main_graph_matrix.insertion_sort_time_taken, main_graph_matrix.merge_sort_time_taken]
    y_values_bx1 = [main_graph_chain_plus.quick_sort_time_taken, main_graph_chain_plus.insertion_sort_time_taken, main_graph_chain_plus.merge_sort_time_taken]
    y_values_bx2 = [main_graph_matrix_plus.quick_sort_time_taken, main_graph_matrix_plus.insertion_sort_time_taken, main_graph_matrix_plus.merge_sort_time_taken]
    time_comparison_list = [main_graph_chain.speed_complexitivity, main_graph_matrix.speed_complexitivity, main_graph_chain_plus.speed_complexitivity, main_graph_matrix_plus.speed_complexitivity]
    space_comparison_list = [main_graph_chain.space_complexitivity, main_graph_matrix.space_complexitivity, main_graph_chain_plus.space_complexitivity, main_graph_matrix_plus.space_complexitivity]
    ax1.set_title("ADJACENCY LIST")
    ax1.bar(x_line, y_values_ax1, align='center', color='c', edgecolor='c')
    ax2.set_title("ADJACENCY MATRIX")
    ax2.bar(x_line, y_values_ax2, align='center', color='r')
    bx1.set_title("ADJACENCY LIST +")
    bx1.bar(x_line, y_values_bx1, align='center', color='g')
    bx2.set_title("ADJACENCY MATRIX +")
    bx2.bar(x_line, y_values_bx2, align='center', color='y')
    time_comparison.set_title("SPEED COMPARISON")
    time_comparison.bar(["LIST", "MATRIX", "LIST +", "MATRIX +"], time_comparison_list, align='center', color='b')
    space_comparison.set_title("SPACE COMPARISON")
    space_comparison.bar(["LIST", "MATRIX", "LIST +", "MATRIX +"], space_comparison_list, align='center', color='m')
    plt.show()