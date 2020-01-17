from twilio.rest import Client

class AdminQueue:
    def __init__(self):
        self._account_sid = 'AC1b1dcc8d75c7cd3ece8ffb9a73346ae1'
        self._auth_token = '31ba3f8179d7605a9d47b57a05d6a5f7'
        self.client = Client(self._account_sid, self._auth_token)
        self._name = ""
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'
    def enqueue(self, item):
        #Aqui deben añadir a la cola #
        self._queue.append(item)
        message = self.client.messages.create(
                              body='Welcome, '+ str(item['name'])+ ', you will be attended soon bitch!' + str(self.size()) + ', before you, sorry, bitch!',
                              from_='+18126104825',
                              to=str(item['phone'])
                          )
        return message.sid
    def dequeue(self):
        #aqui deben procesar la cola #
        if self.size() > 0:
            if self.mode == 'FIFO':
                item = self._queue.pop()
                return item
            elif self._mode == 'LIFO':
                item = self._queue.pop(-1)
                return item
        else:
            msg = {
                "msg": "Fila sin elementos"
            }
            return msgr

    def get_queue(self):
        #RETORNAR todos en la fila
        return self._queue
    def size(self):
        return len(self._queue)
         