from todo_item import Item

class view_model:
    def __init__(self, items: list[Item]):
        self._items: list[Item] = items

    @property
    def items(self) -> list[Item]:
        return self._items
    
    @property
    def to_do(self) -> list[Item]:
        return [item for item in self._items if item.status == "To Do"]

    @property
    def in_progress(self):
        return [item for item in self._items if item.status == "In Progress"]

    @property
    def complete(self):
        return [item for item in self._items if item.status == "Done"]

    @property
    def should_show_all_done_items(self):
        return len(self.filter_list_by_status('Complete')) <= 5