"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Gridworks Type Registry."""


if __name__ == "__main__":
    main(prog_name="gridworks-type-registry")  # pragma: no cover
