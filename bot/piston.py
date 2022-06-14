import dataclasses
import pyston  # type:ignore


client = pyston.PystonClient()


@dataclasses.dataclass
class Output:
    content: str
    success: bool


async def run(lang: str, code: str) -> Output:
    output = await client.execute(lang, [pyston.File(code)])

    return Output(content=str(output), success=output.success)
