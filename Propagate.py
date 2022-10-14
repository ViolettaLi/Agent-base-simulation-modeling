"""Works out time for simulation."""
import os

import matplotlib.patches as m_patches
import matplotlib.pyplot as plt
from celluloid import Camera
from matplotlib.animation import PillowWriter

from Agent import Agent
from Node import Node
from Track import Track

directory = os.path.dirname(os.path.realpath(__file__))


def track_time(agent: Agent, track: Track):
    """Calculate the time for an agent to cross the track."""
    time = track.distance / agent.speed
    return time


fig = plt.figure()
camera = Camera(fig)


def check_end_node(tracks):
    end_node_counter = 0
    for track in tracks:
        if track.end_node.end:
            end_node_counter += 1

    if end_node_counter < 1:
        raise Exception("oops, no node has been defined as the end node")
    elif end_node_counter > 1:
        raise Exception("oops, too many nodes have been defined as end nodes")


def plot_frame(tracks, time):
    """Plot the frame."""
    colours = ['r', 'g', 'b', 'orange', 'black']
    i = 0
    patches = []
    # travellers = []
    for track in tracks:
        # x.append(track.start_node.pos[0])
        # x.append(track.end_node.pos[0])
        # y.append(track.start_node.pos[1])
        # y.append(track.end_node.pos[1])
        assert isinstance(track.end_node, Node)
        x = [track.start_node.pos[0], track.end_node.pos[0]]
        y = [track.start_node.pos[1], track.end_node.pos[1]]
        plt.plot(x, y, "-o", linewidth=5 + 5 * track.travellers,
                 color=colours[i])
        patch = m_patches.Patch(color=colours[i], label=track.travellers)

        plt.plot(x[0], y[0], "o", ms=5 + 10 * track.start_node.travellers,
                 color="b")
        plt.plot(x[1], y[1], "o", ms=5 + 10 * track.end_node.travellers,
                 color="b")
        patches.append(patch)
        i += 1
    patches.append(
        m_patches.Patch(color="white", label=("time=" + str(int(time)))))
    plt.legend(handles=patches)

    # legend = plt.legend(handles=tr)
    # ax = plt.gca().add_artist(legend)
    # plt.legend(handles=)

    # t = plt.figure()
    # plt.legend(handles=[t])
    # plots.append(t)
    # travellers.append("time")
    # plt.legend(plots, travellers)


def propagate(agents, tracks, dt=0.01, animate=False):
    """Calculate time for simulation."""
    # initial frame

    check_end_node(tracks)

    t = 0
    count = 0

    leftover = agents

    while len(leftover) > 0:
        # propagate each agent through one time step
        for agent in leftover:
            if agent.exit:
                leftover.remove(agent)
                continue
            elif agent.element == 'Node':
                # choose a track and try and join it
                ideal_track = agent.current_node.ideal_track()
                ideal_track.add_if_can(agent)
                continue
            elif agent.element == 'Track':
                if isinstance(agent.current_track, Track):
                    if agent.timer >= track_time(agent, agent.current_track):
                        # move agent to node
                        agent.element = "Node"
                        agent.current_track.end_node.travellers += 1
                        agent.current_track.travellers -= 1
                        agent.timer = 0
                        agent.current_node = agent.current_track.end_node
                        if agent.current_node.end:
                            agent.exit = True
                        agent.current_track = None
                        continue
                    else:
                        agent.timer += dt
                        continue
                else:
                    raise Exception("Agent current track has been set wrong")
            raise Exception("oops! agent status wasn't found", agent.element)
        if count % 5 == 0:
            plot_frame(tracks, t)
            camera.snap()
        t += dt
        count += 1
        print(leftover)
    if animate:
        anim = camera.animate()
        pillow = PillowWriter(fps=45)
        filename = directory + "\\Animation.gif"
        anim.save(filename, writer=pillow)

    return t
