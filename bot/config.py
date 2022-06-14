import dataclasses

import dotenv


@dataclasses.dataclass
class Config:
    token: str


CONFIG = Config(
    **{
        key.lower() if key else None: value
        for key, value in dotenv.dotenv_values(".env").items()
    }  # type: ignore
)
