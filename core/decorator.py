from utils.logger_utils import now_ts, write_log

class LoggingDecorator:
    """Adds logging functionality to resource operations."""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    @property
    def name(self):
        return self._wrapped.name

    @property
    def config(self):
        return self._wrapped.config

    @property
    def deleted(self):
        return self._wrapped.deleted

    @deleted.setter
    def deleted(self, value):
        self._wrapped.deleted = value

    def _log(self, action: str, msg: str):
        line = f"[{now_ts()}] {self._wrapped.__class__.__name__} '{self._wrapped.name}' {action} - {msg}"
        print(line)
        write_log(self._wrapped.name, line)

    def start(self):
        msg = self._wrapped.start()
        self._log("started", msg)
        return msg

    def stop(self):
        msg = self._wrapped.stop()
        self._log("stopped", msg)
        return msg

    def delete(self):
        msg = self._wrapped.delete()
        self._log("deleted", msg)
        return msg

    def to_dict(self):
        return self._wrapped.to_dict()

    def validate_config(self):
        return self._wrapped.validate_config()

    def get_details(self):
        return self._wrapped.get_details()

    def set_state(self, state):
        self._wrapped.set_state(state)
