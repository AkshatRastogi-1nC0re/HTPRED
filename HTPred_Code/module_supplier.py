import module_description
import Module


class supplier:
    __folder_path = None
    __predefined_modules = None

    def __init__(self, folder_path):
        self.__folder_path = folder_path
        self.__predefined_modules = dict()

    def add_from_path(self,path):
        fileobj = open(path,'r')
        file_body = fileobj.readlines()
        fileobj.close()

        # Splitting for comments by new line
        module_lines = str()
        for f in file_body:
            f = f.strip()
            if f == 'endmodule':
                f += ';'
            if f[:2] != '//' and len(f) != 0:
                module_lines += f

        module_instance = str()
        do_copy = False
        for line in module_lines.split(';'):
            if len(line) > 7 and line[:7] == 'module ':
                do_copy = True
            if do_copy:
                module_instance += line+'\n'
            if line == 'endmodule':
                do_copy = False
                module_desc = module_description.module_description(self,module_instance)
                self.__predefined_modules[module_desc.get_name()] = module_desc
                module_instance = str()

    def get_module(self,module_name):
        if module_name not in self.__predefined_modules:
            self.add_from_path(self.__folder_path+module_name+'.txt')

        return self.__predefined_modules[module_name]

    def get_modules(self):
        return self.__predefined_modules
