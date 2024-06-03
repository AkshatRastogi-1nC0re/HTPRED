import Module
import module_supplier
import module_feature_extractor
import BenchToFeatureExtractor

# HTPredBenchCreator.Creator v1.35


class Creator:
    __dir = None
    __file_path = None
    __main_module = None
    __supplier = None

    __last_built_module = None

    def __init__(self, file_path, cell_dir, main_module=None):
        self.__dir = cell_dir
        self.__file_path = file_path
        self.__main_module = main_module

        self.__supplier = module_supplier.supplier(cell_dir)
        print("Importing modules...")
        self.__supplier.add_from_path(file_path)

    def build(self, ignore_file=[]) -> None:
        if len(self.__supplier.get_modules()) == 1:
            self.__main_module = list(self.__supplier.get_modules().keys())[0]

        ignore_set = dict()
        for i in ignore_file:
            file = open(i)
            for j in file.readlines():
                j = j.strip()
                if len(j) != 0:
                    kv = j.split(' ')
                    if len(kv) == 1:
                        kv.append('X')
                    ignore_set[kv[0].strip()] = kv[1].strip()
            file.close()

        m = Module.Module(self.__supplier,ignore_set)
        print("Compiling..."+self.__main_module)
        m.parse(self.__supplier.get_modules()[self.__main_module])

        self.__last_built_module = m

    def convert(self):
        if self.__last_built_module is None:
            self.build()

        return self.__last_built_module.get_bench_file()

    def get_compiled_module(self) -> Module:
        return self.__last_built_module


class FeatureExtractor(Creator):
    _feature_extractor = None
    _ignore_list = None

    _module = None

    def __init__(self,file_path,cell_dir,main_module=None):
        Creator.__init__(self,file_path,cell_dir,main_module)

    def getfeatures(self,export_file,ignore_files:list = []):
        self.build(ignore_files)
        self._module = self.get_compiled_module()

        print("COMPILAION DONE\nFEATURE EXTRACTION STARTED")

        self._feature_extractor = module_feature_extractor.feature_extractor(self._module)

        feature_functions = {
        "in_nearest_pin" : self._feature_extractor.in_nearest_pin,
        "out_nearest_pin" : self._feature_extractor.out_nearest_pin,
        "out_nearest_mux" : self._feature_extractor.out_nearest_mux,
        "out_nearest_flipflop" : self._feature_extractor.out_nearest_flipflop,
        "in_nearest_mux" : self._feature_extractor.in_nearest_mux,
        "in_nearest_flipflop" : self._feature_extractor.in_nearest_flipflop,
        "loop_out" : self._feature_extractor.loop_out,
        "loop_in" : self._feature_extractor.loop_in,
        "ff_in" : self._feature_extractor.ff_in,
        "ff_out" : self._feature_extractor.ff_out,
        "mux_out" : self._feature_extractor.mux_out,
        "mux_in" : self._feature_extractor.mux_in,
        "lgfi" : self._feature_extractor.lgfi }

        open(export_file,'w').close()
        threads = []

        for i in feature_functions:
            self.__export(feature_functions,i)
            print("DONE: "+ i)
            # athd = threading.Thread(target=self.__export,args=(feature_functions,i))
            # athd.start()
            # threads.append(athd)

        # for i in threads:
        #     i.join()

        t = open(export_file, 'a')
        for v in feature_functions:
            output = feature_functions[v]
            first = True
            for i in output:
                if first:
                    first = False
                    continue

                for j in range(len(i)):
                    t.write(str(i[j]))
                    if j != len(i) - 1:
                        t.write(",")
                t.write('\n')

        t.close()

    def __export(self,f,fn):
        f[fn] = f[fn]()


class BenchToFeature:
    process = None

    def __init__(self,inputfile):
        self.process = BenchToFeatureExtractor.BenchToFeature(inputfile)
        self.process.calculatefeatures()

    def getfeatures(self):
        for feature in self.process.final_data.keys():
            for wire in self.process.final_data[feature].keys():
                if not isinstance(self.process.final_data[feature][wire],list):
                    self.process.final_data[feature][wire] = [self.process.final_data[feature][wire]]
        return self.process.final_data

    def export(self,file_name):
        self.process.export_to_file(file_name)
