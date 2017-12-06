import graphviz as gv
import functools


class StateMachine(object):
    """Class for building a state machine."""

    def __init__(self, output_format):
        self.graph = functools.partial(gv.Digraph, format=output_format)()

    def add(self, nodes, edges):
        self._add_nodes(nodes)
        self._add_edges(edges)

    def _add_nodes(self, nodes):
        for n in nodes:
            self.graph.node(n)

    def _add_edges(self, edges):
        for e, v in edges.items():
            self.graph.edge(e[0], e[1], label=v)

    def render(self, file_path):
        """Renders the graph and exports it to a specified file.

        :param file_path: Path of the rendered graph
        """

        self.graph.render(file_path, view=True)
