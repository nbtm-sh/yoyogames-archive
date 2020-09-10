class CFG:
    def __init__(self, fp):
        self.fp = fp
        self.dict = {}

        for line in self.fp.readlines():
            key, value = line.split('=', 1)
            value = value.strip()
            key = key.strip()

            self.dict[key] = value
        
    def __getitem__(self, key):
        return self.dict[key]
    
    def __setitem__(self, key, value):
        self.dict[key] = value
    
    def dumps(self):
        return '\n'.join([key + '=' + value for key, value in zip(self.dict.keys(), self.dict.values())])