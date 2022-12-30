# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.

class Solution:
    def allPathsSourceTarget(self, graph):
        path_record = dict()
        target = len(graph) - 1

        return self.traverse(0, graph, path_record, target)

    def traverse(self, index, graph, path_record, target):
        if index == target:
            path_record[index] = [[index]]
            return [[index]]

        index_paths = []
        for edge in graph[index]:
            edge_paths = None

            if edge in path_record:
                edge_paths = path_record.get(edge)
            else:
                edge_paths = self.traverse(edge, graph, path_record, target)

            for edge_path in edge_paths:
                index_paths.append([index, *edge_path])

        path_record[index] = index_paths

        return index_paths
