import PySimpleGUI as Sg

from Agent import Agent
from Node import Node
from Track import Track


def initial_gui():
    Sg.theme("LightBlue")
    layout = [[Sg.Text("Number of Nodes"),
               Sg.Slider(range=(2, 10), default_value=5,
                         orientation="horizontal", font=('Helvetica', 12))],
              [Sg.Text("Number of Tracks"),
               Sg.Slider(range=(1, 10), default_value=5,
                         orientation="horizontal", font=('Helvetica', 12))],
              [Sg.Text("Number of Agents"),
               Sg.Slider(range=(1, 10), default_value=5,
                         orientation="horizontal", font=('Helvetica', 12))],
              [Sg.Button('Ok'), Sg.Button('Cancel')]]

    window = Sg.Window('Best Pedestrian Dynamics Model Simulator Ever', layout)

    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED or event == 'Cancel':
            break
        window.close()
        return values


def node_gui(number_of_nodes):
    Sg.theme("LightBlue")
    layout = []
    for i in range(number_of_nodes):
        node_options_list = [
            [Sg.Text("Max Capacity"), Sg.Slider(range=(1, 10), default_value=5,
                                                orientation="horizontal",
                                                font=('Helvetica', 12))],
            [Sg.Text("Is this the final node")],
            [Sg.Radio('No', "Node" + str(i), default=True),
             Sg.Radio('Yes', "Node" + str(i))],
            [Sg.Text("Node Name:"), Sg.InputText('')],
            [Sg.Text("Node Position"),
             Sg.Spin([i for i in range(1, 11)],
                     initial_value=1),
             Sg.Text('X position'),
             Sg.Spin([i for i in range(1, 11)],
                     initial_value=1),
             Sg.Text('Y Position')]]
        layout.append([Sg.Frame("Node " + str(i) + " Attributes:",
                                node_options_list, font='Any 12',
                                title_color='blue')])

    layout.append([Sg.Button('Ok'), Sg.Button('Cancel')])

    window = Sg.Window('Best Pedestrian Dynamics Model Simulator Ever',
                       layout)

    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED or event == 'Cancel':
            break
        window.close()
        return values


def track_gui(number_of_nodes, number_of_tracks):
    Sg.theme("LightBlue")
    layout = []
    for i in range(number_of_tracks):
        track_options_list = [
            [Sg.Text("Distance"), Sg.Slider(range=(1, 10), default_value=5,
                                            orientation="horizontal",
                                            font=('Helvetica', 12))],
            [Sg.Text("Max Capacity"), Sg.Slider(range=(1, 10), default_value=5,
                                                orientation="horizontal",
                                                font=('Helvetica', 12))],
            [Sg.Text("Connects node:"),
             Sg.Spin(
                 [i for i in range(0, number_of_nodes)],
                 initial_value=0),
             Sg.Text('to node:'),
             Sg.Spin(
                 [i for i in range(0, number_of_nodes)],
                 initial_value=0),
             Sg.Text('')],
            [Sg.Text("Weight"), Sg.Slider(range=(1, 10), default_value=5,
                                          orientation="horizontal",
                                          font=('Helvetica', 12))],
            [Sg.Text("Track Name:"), Sg.InputText('')]]
        layout.append([Sg.Frame("Track " + str(i) + " Attributes:",
                                track_options_list, font='Any 12',
                                title_color='blue')])

    layout.append([Sg.Button('Ok'), Sg.Button('Cancel')])

    window = Sg.Window('Best Pedestrian Dynamics Model Simulator Ever',
                       layout)

    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED or event == 'Cancel':
            break
        window.close()
        return values


def agent_gui(number_of_nodes, number_of_agents):
    Sg.theme("LightBlue")
    layout = []
    for i in range(number_of_agents):
        agent_options_list = [
            [Sg.Text("speed"), Sg.Slider(range=(1, 10), default_value=5,
                                         orientation="horizontal",
                                         font=('Helvetica', 12))],
            [Sg.Text("Initial Node"),
             Sg.Slider(range=(0, number_of_nodes - 1), default_value=0,
                       orientation="horizontal",
                       font=('Helvetica', 12))]]
        layout.append([Sg.Frame("Agent " + str(i) + " Attributes:",
                                agent_options_list, font='Any 12',
                                title_color='blue')])

    layout.append([Sg.Button('Ok'), Sg.Button('Cancel')])

    window = Sg.Window('Best Pedestrian Dynamics Model Simulator Ever',
                       layout)

    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED or event == 'Cancel':
            break
        window.close()
        return values


def guis():
    values = initial_gui()
    number_of_nodes = int(values[0])
    number_of_tracks = int(values[1])
    number_of_agents = int(values[2])

    nodes = node_gui(number_of_nodes)
    tracks = track_gui(number_of_nodes, number_of_tracks)
    agents = agent_gui(number_of_nodes, number_of_agents)

    node_dict = dict()
    for i in range(number_of_nodes):
        node = Node(max_capacity=int(nodes[6 * i]), is_end=nodes[6 * i + 2],
                    name=nodes[6 * i + 3],
                    pos=[nodes[6 * i + 4], nodes[6 * i + 5]])
        node_dict["Node" + str(i)] = node

    tracks_list = []
    number_of_track_attributes = 6
    for i in range(number_of_tracks):
        track = Track(distance=int(tracks[number_of_track_attributes * i]),
                      max_capacity=int(
                          tracks[number_of_track_attributes * i + 1]),
                      node1=node_dict["Node" + str(int(
                          tracks[number_of_track_attributes * i + 2]))],
                      node2=node_dict["Node" + str(int(
                          tracks[number_of_track_attributes * i + 3]))],
                      weight=int(tracks[number_of_track_attributes * i + 4]),
                      name=tracks[number_of_track_attributes * i + 5])
        tracks_list.append(track)

    agent_list = []
    for i in range(number_of_agents):
        agent = Agent(speed=int(agents[2 * i]),
                      initial_node=node_dict[
                          "Node" + str(int(agents[2 * i + 1]))])
        agent_list.append(agent)
    return agent_list, tracks_list
