import Main
import statistics
import math

limit = 3


class ApplicationClass:

    applications_list = Main.array_list()

    def __init__(self, app_name, programmer_name):
        self.app_name = app_name
        self.programmer_name = programmer_name
        self.downloaded_times = 0
        self.strategy_rate = None
        self.sports_rate = None
        self.simulation_rate = None

    def add_strategy_rate(self, rate):
        if self.strategy_rate is None:
            self.strategy_rate = rate
        else:
            the_list = [self.strategy_rate, rate]
            self.strategy_rate = statistics.mean(the_list)

    def add_sports_rate(self, rate):
        if self.sports_rate is None:
            self.sports_rate = rate
        else:
            the_list = [self.sports_rate, rate]
            self.sports_rate = statistics.mean(the_list)

    def add_simulation_rate(self, rate):
        if self.simulation_rate is None:
            self.simulation_rate = rate
        else:
            the_list = [self.simulation_rate, rate]
            self.simulation_rate = statistics.mean(the_list)


def app_adder(given_app_name):
    for each_app in ApplicationClass.applications_list.display():
        if each_app.app_name == given_app_name:
            return False
    return True

def none_checker(value):
    if value is None:
        return 0
    else:
        return value

def eds_calculator(first, second):
    if first.strategy_rate is None:
        first.strategy_rate = 0
    return math.sqrt(math.pow(none_checker(second.strategy_rate) - none_checker(first.strategy_rate), 2) + \
    math.pow(none_checker(second.sports_rate) - none_checker(first.sports_rate), 2) + \
    math.pow(none_checker(second.simulation_rate) - none_checker(first.simulation_rate), 2))

def check_edge_inside(given_list, edge):
    edges_parts = edge.split("_")
    reversed_edge = edges_parts[1] + "_" + edges_parts[0]
    for each in given_list:
        if each == edge or each == reversed_edge:
            return True
    return False

def make_all_edges():
    edges_list = Main.array_list()
    for each_app_1 in ApplicationClass.applications_list.display():
        for each_app_2 in ApplicationClass.applications_list.display():
            if each_app_1.app_name != each_app_2.app_name:
                if eds_calculator(each_app_1, each_app_2) <= limit:
                    app_1_id = ApplicationClass.applications_list.display().index(each_app_1)
                    app_2_id = ApplicationClass.applications_list.display().index(each_app_2)
                    new_edge = str(app_1_id) + "_" + str(app_2_id)
                    if check_edge_inside(edges_list.display(), new_edge) is False:
                        edges_list.append(new_edge)
    return edges_list.display()

def pass_first_to_second():
    main_graph_chain = Main.Graph()
    main_graph_chain_plus = Main.Graph()
    for i in range(len(ApplicationClass.applications_list)):
        main_graph_chain.add_vertex(i)
        main_graph_chain_plus.add_vertex(i)
    main_graph_matrix = Main.Graph_Matrix(len(ApplicationClass.applications_list))
    main_graph_matrix_plus = Main.Graph_Matrix(len(ApplicationClass.applications_list))
    edges = make_all_edges()
    for each_edge in edges:
        edges_parts = each_edge.split("_")
        u = int(edges_parts[0])
        v = int(edges_parts[1])
        main_graph_chain.add_edge(u, v)
        main_graph_chain_plus.add_edge(u, v)
        main_graph_matrix.add_edge(u, v)
        main_graph_matrix_plus.add_edge(u, v)
    Main.start_from_second_phase(main_graph_chain, main_graph_matrix, main_graph_chain_plus, main_graph_matrix_plus)

def get_recommendations(given_app):
    answers = Main.array_list()
    for each_app in ApplicationClass.applications_list.display():
        if each_app.app_name != given_app.app_name:
            if eds_calculator(given_app, each_app) <= limit:
                answers.append(each_app.app_name)
    return answers.display()

