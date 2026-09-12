class ManagementSystem:
    def __init__(self, name="Management System"):
        self.name = name

    def display_name(self):
        return self.name

    def add_record(self, record):
        if not hasattr(self, "records"):
            self.records = []
        self.records.append(record)
        return self.records

    def list_records(self):
        return getattr(self, "records", [])
