import dataclasses

import pyston  # type:ignore
from pyston import exceptions

client = pyston.PystonClient()


@dataclasses.dataclass
class Output:
    content: str
    success: bool


class ExecutionError(exceptions.ExecutionError):  # type: ignore
    ...


async def run(lang: str, code: str) -> Output:
    try:
        output = await client.execute(lang, [pyston.File(code)])
    except exceptions.ExecutionError as e:
        raise ExecutionError from e

    return Output(content=str(output), success=output.success)
