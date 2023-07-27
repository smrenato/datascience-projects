import typer

# import os

# import sys
from rich.console import Console

# from rich.table import Table
from .config import settings

# from .hydra_conf import dsp_main

main = typer.Typer(
    name="dsp CLI",
)
console = Console()


@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars)
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()


# @main.command()
# def see_configs():
#     console.print(f"Settings {settings.MSG}", style="bold blue")


# @main.command()
# def see_param():
#     os.environ["PARAM_MODE"] = "hparam"
#     console.print(f"Settings {env.PARAM}", style="bold green on blue")
