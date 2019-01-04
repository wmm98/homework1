import socket
import threading
from Queue import Queue
def scan(port):
  s = socket.socket()
  s.settimeout(0.1)
  if s.connect_ex(('localhost', port)) == 0:
    print port, 'open'
  s.close()

def worker():
  while not q.empty():
    port = q.get()
    try:
      scan(port)
    finally:
      q.task_done()

if __name__ == '__main__':
  q = Queue()
  map(q.put,range(1,65535))
  threads = [threading.Thread(target=worker) for i in xrange(100)]
  map(lambda x:x.start(),threads)
  q.join()
