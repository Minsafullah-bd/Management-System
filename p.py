class ManagementSystem:
    def __init__(self, name="Management System"):
        self.name = name
        self.records = []

    def display_name(self):
        return self.name

    def add_record(self, record):
        self.records.append(record)
        return self.records

    def list_records(self):
        return self.records

    def remove_record(self, record):
        if record in self.records:
            self.records.remove(record)
            return True
        return False

    def find_record(self, record):
        return record in self.records

    def count_records(self):
        return len(self.records)

    def clear_records(self):
        self.records.clear()
        return self.records

    def update_record(self, old_record, new_record):
        if old_record in self.records:



    #hello
    #hello
            index = self.records.index(old_record)
            self.records[index] = new_record
            return True
        return False
