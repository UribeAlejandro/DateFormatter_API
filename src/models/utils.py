from threading import Lock


class SingletonCounter(type):
    """This is a thread-safe implementation of Singleton, ensures only one
    instance of the class is created."""

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Counter(metaclass=SingletonCounter):
    """A simple counter class that can be used to keep track of the number of
    times an event occurs."""

    def __init__(self) -> None:
        self.__count = 0

    def increment(self) -> None:
        """Increment the counter by 1."""
        self.__count += 1

    def get_count(self) -> int:
        """Get the current count.

        Returns
        -------
        int
            The current count.
        """
        return self.__count

    def reset(self) -> None:
        """Reset the counter to 0."""
        self.__count = 0
