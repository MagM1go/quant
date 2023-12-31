from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from quant.impl.core.client import Client


class BaseModel:
    client: Any | None = None

    @classmethod
    def set_client(cls, client):
        cls.client: Client = client

    @classmethod
    def as_dict(cls, data: dict):
        if data is not None:
            return cls(**data)  # type: ignore
