import unittest
import graph_search

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []


class TestGraphSearch(unittest.TestCase):
    def test_width_search(self):
        self.assertEqual(graph_search.width_search(graph, "you", "bob"), True)
        self.assertEqual(graph_search.width_search(
            graph, "you", "stan"), False)
