from black import out
import crescent
import hikari
from bot import utils
from bot import piston

plugin = crescent.Plugin("eval")


class EvalError(Exception):
    ...


@plugin.include
@crescent.message_command(name="Run")
async def run(ctx: crescent.Context, message: hikari.Message):
    if not message.content:
        return

    code: str = ""

    in_code_block = False

    for sec in utils.split(message.content, "```"):
        if sec == "```":
            in_code_block = not in_code_block
        elif in_code_block:
            code += sec

    lang = code.splitlines().pop(0).strip()

    if f"```{lang}" not in message.content:
        raise EvalError("A language is not specified.")

    code_lines = code.splitlines()
    code_lines.pop(0)
    code = "\n".join(code_lines)

    output = await piston.run(lang, code)

    if output.success:
        hint = "The code ran successfully."
    else:
        hint = "The code had an error!"

    await ctx.respond(f"{hint}\n```\n{output.content}```")
