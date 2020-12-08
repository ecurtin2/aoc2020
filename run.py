import importlib
from pathlib import Path
from typing import List, Optional, get_type_hints

import cattr
import click

modules = [
    str(p.name).replace("d", "").replace(".py", "")
    for p in Path(__file__).parent.rglob("d*.py")
]


cattr.register_structure_hook(List[int], lambda s, _: [int(l) for l in s.splitlines()])
cattr.register_structure_hook(List[str], lambda s, _: s.splitlines())


@click.command()
@click.argument("day", type=click.Choice(modules + ["all"]), required=True)
@click.option("--part", "-p", type=click.Choice(["1", "2"]), required=False)
def cli(day: int, part: Optional[int]):

    if day == "all":
        modules_to_run = [f"d{m}" for m in modules if m != "all"]
    else:
        modules_to_run = [f"d{day}"]

    for mod in modules_to_run:
        print(f"Day {mod[1:]}: ")
        module = importlib.import_module(mod)

        input_path = Path(f"inputs/{mod}p{part}.txt")
        if (not input_path.is_file()) and (part != "1"):
            # fallback since sometimes same input reused.
            input_path = Path(f"inputs/{mod}p1.txt")

        try:
            raw_str = input_path.read_text()
        except FileNotFoundError:
            print(
                f"No data file found for day {mod} part {part}. Expected {input_path}"
            )
            continue

        if part is not None:
            if part == "1":
                funcs = ["part1"]
            elif part == "2":
                funcs = ["part2"]
            else:
                raise ValueError(f"bad part name: {part}")
        else:
            funcs = ["part1", "part2"]

        for func_name in funcs:
            print(func_name, end=": ")
            func = getattr(module, func_name)
            typ = list(get_type_hints(func).values())[0]
            inp = cattr.structure(raw_str, typ)
            print(func(inp))
        print()


if __name__ == "__main__":
    cli()
