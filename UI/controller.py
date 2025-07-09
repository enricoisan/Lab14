import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.selectedStore = None
        self.numero_giorni_max = None
        self.selectedNodo = None

    def fillDdStore(self):
        stores = self._model.getStores()
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(key = store.store_id,
                                                                  text = store.store_id,
                                                                  data = store,
                                                                  on_click=self.readStore))
        return

    def readStore(self, e):
        self.selectedStore = e.control.data
        print(f"Selected store: {self.selectedStore}")
        return

    def handleCreaGrafo(self, e):
        # Recupero input
        self.numero_giorni_max = self._view._txtIntK.value

        # Validazione degli input
        if self.numero_giorni_max == "" and self.selectedStore is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare uno store e un numero massimo di giorni"))
            self._view.update_page()
            return

        if self.numero_giorni_max == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire numero massimo di giorni"))
            self._view.update_page()
            return

        if self.selectedStore is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare uno store"))
            self._view.update_page()
            return

        try:
            int(self.numero_giorni_max)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore intero"))
            self._view.update_page()
            return

        # Costruzione grafo
        self._model.buildGraph(self.selectedStore.store_id, int(self.numero_giorni_max))
        self.nodi = self._model.getAllNodes()
        self.fillddNode(self.nodi)

        # Chiama metodi del model
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Graph created!"))
        self._view.txt_result.controls.append(ft.Text("Num of nodes: " + str(self._model.getNumNodes())))
        self._view.txt_result.controls.append(ft.Text("Num of edges: " + str(self._model.getNumEdges())))
        self._view.update_page()

    def handleCerca(self, e):
        nodo = self.selectedNodo
        if nodo is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un nodo di partenza"))
            self._view.update_page()

        nodes = self._model.getCammino(nodo)
        self._view.txt_result.controls.append(ft.Text(f"Nodo di partenza : {nodo}"))
        for n in nodes:
            self._view.txt_result.controls.append(ft.Text(n))
        self._view.update_page()

    def handleRicorsione(self, e):
        pass

    def fillddNode(self, nodi):
        for nodo in nodi:
            self._view._ddNode.options.append(ft.dropdown.Option(key=nodo.order_id,
                                                          text=nodo.order_id,
                                                          data=nodo,
                                                          on_click=self.readNodo))
        return

    def readNodo(self, e):
        self.selectedNodo = e.control.data
        print(f"Selected order: {self.selectedNodo}")
        return






