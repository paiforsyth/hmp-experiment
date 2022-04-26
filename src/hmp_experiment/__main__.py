"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hmp Experiment."""


if __name__ == "__main__":
    main(prog_name="hmp-experiment")  # pragma: no cover
