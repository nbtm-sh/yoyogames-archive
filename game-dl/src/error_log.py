class ErrorLog:
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')

    def missing_file(self, location):
        write = f"[Error] Failed to download {location}\n"
        self.output_file.write(write)