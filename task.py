from datetime import datetime

class Task:
    def __init__(self, name, priority=None, deadline=None, start_date=None, duration=None, dependencies=None, tags=None, status='todo', notes=None, resources=None):
        self.name = name
        self.priority = priority
        self.deadline = self.parse_date(deadline)
        self.start_date = self.parse_date(start_date)
        self.duration = duration
        self.dependencies = dependencies if dependencies is not None else []
        self.tags = tags if tags is not None else []
        self.status = status
        self.notes = notes if notes is not None else []
        self.resources = resources if resources is not None else []

    @staticmethod
    def parse_date(date_str):
        if isinstance(date_str, datetime):
            return date_str
        elif isinstance(date_str, str) and date_str:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"Provided string is not a valid date format: {date_str}")
        return None

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def set_status(self, status):
        self.status = status

    def add_note(self, note):
        self.notes.append(note)

    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority,
            "deadline": self.deadline.strftime("%Y-%m-%d") if isinstance(self.deadline, datetime) else self.deadline,
            "start_date": self.start_date.strftime("%Y-%m-%d") if isinstance(self.start_date, datetime) else self.start_date,
            "duration": self.duration,
            "dependencies": self.dependencies,
            "tags": self.tags,
            "status": self.status,
            "notes": self.notes,
            "resources": self.resources
        }
    def __repr__(self):
        return f"Task(name={self.name})"
