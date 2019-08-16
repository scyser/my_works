
import os
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from concurrent.futures import ThreadPoolExecutor
import time

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()



    class MyClass:
        def __init__(self):
            self.id = 0
            self.pool = ThreadPoolExecutor(100)
            self.dict_operation = {}

        def get_elements(self, path, flag_recursive=False):
            files_list = []
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    time.sleep(1)
                    files_list.append({"name": filename, "type": "file"})
                for dirname in dirnames:
                    if flag_recursive:
                        new_path = os.path.join(dirpath, dirname)
                        files_list.append({"name": dirname, "type": "folder", "subelements": self.get_elements(new_path, True)})
                        time.sleep(1)
                    else:
                        files_list.append({"name": dirname, "type": "folder"})
                        time.sleep(1)
                break
            return files_list

        def start_get_elements(self, path, flag_recursive=False):
            self.id += 1
            start = self.pool.submit(self.get_elements, path, flag_recursive)
            self.dict_operation[self.id] = start
            return self.id

        def get_result(self, id):
            try:
                if self.dict_operation[id].done():
                    return_list = self.dict_operation[id].result()
                    del self.dict_operation[id]
                    return return_list
                else:
                    return "executing..."
            except KeyError:
                return "Process has done or doesn't exist"


    server.register_instance(MyClass())

    server.serve_forever()