import alembic.config


def handler(event, context):
    alembic_args = [
        "--raiseerr",
        "upgrade", "head",
    ]
    alembic.config.main(argv=alembic_args)


if __name__ == "__main__":
    handler({}, [])
