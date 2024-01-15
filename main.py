from ChessGUI.application import Application


def main() -> None:
    app : Application = Application(800, 800)
    app.run()


if __name__ == "__main__":
    main()
    