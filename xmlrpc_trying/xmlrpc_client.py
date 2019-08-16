import xmlrpc.client
import time
s = xmlrpc.client.ServerProxy('http://localhost:8000')
#print(s.get_elements("E:/Test", True))
id = s.start_get_elements("D:/Test", True)
print(id)
time.sleep(1)
print(s.get_result(id))
time.sleep(10)
print(s.get_result(id))