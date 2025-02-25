from dataclasses import dataclass

from settings.settings import Settings


@dataclass
class Topic:
    _profile_ini: str
    _address: str
    _alias: str | None = None
    _qos: int = 1
    _color: str | None = None
    _no_local: bool = False
    _retain_as_published: bool = False
    _retain_handling: str | None = None

    def __post_init__(self):
        self._settings = Settings(self._profile_ini)

    def create(self) -> None:
        """Creating topic."""
        self._settings.set_with_save('topics', self._address, self._address)

        for attr_name in dir(self):
            attr = getattr(type(self), attr_name, None)
            if isinstance(attr, property):
                self._settings.set_with_save(
                    self._address, attr_name, str(getattr(self, attr_name))
                )

    def get_name(self):
        return self._alias or self._address

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value
        self._settings.set_with_save(self._address, 'address', value)

    @property
    def alias(self) -> str:
        return self._alias

    @alias.setter
    def alias(self, value: str) -> None:
        self._alias = value
        self._settings.set_with_save(self._address, 'alias', value)

    @property
    def qos(self) -> int:
        return self._qos

    @qos.setter
    def qos(self, value: int) -> None:
        self._qos = value
        self._settings.set_with_save(self._address, 'qos', value)

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value
        self._settings.set_with_save(self._address, 'color', value)

    @property
    def no_local(self) -> bool:
        return self._no_local

    @no_local.setter
    def no_local(self, value: bool) -> None:
        self._no_local = value
        self._settings.set_with_save(self._address, 'no_local', value)

    @property
    def retain_as_published(self) -> bool:
        return self._retain_as_published

    @retain_as_published.setter
    def retain_as_published(self, value: bool) -> None:
        self._retain_as_published = value
        self._settings.set_with_save(self._address, 'retain_as_published', value)

    @property
    def retain_handling(self) -> str:
        return self._retain_handling

    @retain_handling.setter
    def retain_handling(self, value: str) -> None:
        self._retain_handling = value
        self._settings.set_with_save(self._address, 'retain_handling', value)

    def set_fields_from_dict(self, data: dict) -> None:
        for key, value in data.items():
            key = key.removeprefix('_')
            if hasattr(self, key):
                setattr(self, key, value)
