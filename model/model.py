import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._edges = None
        self._nodes = None
        self._grafo = nx.DiGraph()
        self._idMap = {}

    def buildGraph(self, store_id, giorni):

        # Inizializziamo il grafo
        self._grafo.clear()

        # Aggiungiamo i nodi
        self._nodes = DAO.getNodes(store_id)
        self._grafo.add_nodes_from(self._nodes)

        # Riempiamo il dizionario (se necessario)
        self.fillIdMap()

        # Aggiungiamo gli archi
        for node1 in self._nodes:
            for node2 in self._nodes:
                if node1 != node2:
                    w = DAO.getWeight(node1, node2, giorni)
                    if w:
                        self._grafo.add_edge(node1, node2, weight = w[0])
        return

    def getStores(self):
        return DAO.getStores()

    def getNodes(self, storeId):
        return DAO.getNodes(storeId)

    def nodiRaggiungibiliBFS(self, start_node):
        bfs_nodes = list(nx.bfs_tree(self._grafo, start_node).nodes())
        return bfs_nodes

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getAllEdges(self):
        return self._grafo.edges

    def getAllNodes(self):
        return self._nodes

    def fillIdMap(self):
        for nodo in self._nodes:
            self._idMap[nodo.store_id] = nodo

    def getCammino(self, source):
        lp = []

        # for source in self._graph.nodes:
        tree = nx.dfs_tree(self._grafo, source)
        nodi = list(tree.nodes())

        for node in nodi:
            tmp = [node]

            while tmp[0] != source:
                pred = nx.predecessor(tree, source, tmp[0])
                tmp.insert(0, pred[0])

            if len(tmp) > len(lp):
                lp = copy.deepcopy(tmp)

        return lp