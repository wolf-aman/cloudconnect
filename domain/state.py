from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, resource):
        self._resource = resource

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def start(self) -> str: pass
    @abstractmethod
    def stop(self) -> str: pass
    @abstractmethod
    def delete(self) -> str: pass


class CreatedState(State):
    @property
    def name(self): return "created"

    def start(self):
        self._resource.set_state(StartedState(self._resource))
        return f"{self._resource.name} started."

    def stop(self): raise RuntimeError("Cannot stop: not started.")
    def delete(self):
        self._resource.deleted = True
        self._resource.set_state(DeletedState(self._resource))
        return f"{self._resource.name} deleted."


class StartedState(State):
    @property
    def name(self): return "started"

    def start(self): raise RuntimeError("Already started.")
    def stop(self):
        self._resource.set_state(StoppedState(self._resource))
        return f"{self._resource.name} stopped."
    def delete(self): raise RuntimeError("Stop first before deleting.")


class StoppedState(State):
    @property
    def name(self): return "stopped"

    def start(self):
        self._resource.set_state(StartedState(self._resource))
        return f"{self._resource.name} started again."
    def stop(self): raise RuntimeError("Already stopped.")
    def delete(self):
        self._resource.deleted = True
        self._resource.set_state(DeletedState(self._resource))
        return f"{self._resource.name} deleted."


class DeletedState(State):
    @property
    def name(self): return "deleted"

    def start(self): raise RuntimeError("Cannot start deleted resource.")
    def stop(self): raise RuntimeError("Cannot stop deleted resource.")
    def delete(self): raise RuntimeError("Already deleted.")