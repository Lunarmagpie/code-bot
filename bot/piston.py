import dataclasses

import pyston  # type:ignore
from pyston import exceptions  # type:ignore

client = pyston.PystonClient()


@dataclasses.dataclass
class Output:
    content: str
    success: bool


class ExecutionError(exceptions.ExecutionError):
    ...


async def run(lang: str, code: str) -> Output:
    try:
        output = await client.execute(lang, [pyston.File(code)])
    except exceptions.ExecutionError as e:
        raise ExecutionError from e

    return Output(content=str(output), success=output.success)
