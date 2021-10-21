from flask_smorest import Api, Page

api = Api()


class SQLCursorPage(Page):
    @property
    def item_count(self):
        return self.collection.count()
