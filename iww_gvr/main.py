"""The iww_gvr command line interface module."""


from iww_gvr.menu import Menu

# TODO dvp: if needed, then add here passing command line arguments, configuring, logging and so on.


def main():
    """Run iww_gvr in interactive mode."""
    Menu()


if __name__ == "__main__":
    main()
