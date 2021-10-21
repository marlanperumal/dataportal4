class NotFoundError(Exception):
    status_code = 404

    def __init__(self, message: str):
        super().__init__()
        self.message = message

    def to_dict(self) -> dict:
        return {
            "code": self.status_code,
            "status": "Not Found",
            "message": self.message,
            "errors": {},
        }
