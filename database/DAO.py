from database.DB_connect import DBConnect
from model.Order import Order
from model.Store import Store


class DAO():
    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM stores"
        cursor.execute(query,)
        for row in cursor:
            result.append(Store(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(storeId):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * 
                    FROM orders 
                    WHERE store_id = %s"""
        cursor.execute(query, (storeId, ) )
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result

        # Metodo che ricava il peso dell'arco tra due nodi (nodo1 e nodo2)

    def getWeight(nodo1, nodo2, giorni):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT T1.Quantity + T2.Quantity as Weight
                    FROM 
                        (SELECT o.order_id, o.order_date, SUM(ot.quantity) as Quantity
                        FROM orders o, order_items ot
                        WHERE o.order_id = %s
                        AND o.order_id  = ot.order_id) T1, 
                        (SELECT o.order_id, o.order_date, SUM(ot.quantity) as Quantity
                        FROM orders o, order_items ot
                        WHERE o.order_id = %s
                        AND o.order_id  = ot.order_id) T2
                    WHERE DATEDIFF(T2.order_date, T1.order_date) > 0
                    AND DATEDIFF(T2.order_date, T1.order_date) < %s"""
        cursor.execute(query, (nodo1.order_id, nodo2.order_id, giorni,))
        for row in cursor:
            result.append(row["Weight"])
        cursor.close()
        conn.close()
        return result