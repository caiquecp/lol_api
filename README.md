# LoL API

LoL API is a Python application made to serve League of Legends data.

## Installation

We use Poetry to manage this project dependencies.

```
poetry install
```

## Configuration

We are using a `.env` file to setup the configuration.

| env | description | required |
|---|---|---|
| champions_json_path | Path to champions JSON file | yes |

## Usage

There are a few commands available at this moment.

Format code:

```
make format
```

Type checking with typing and mypy:

```
make check-typing
```

Run and build data (as JSON):

```
make run
```

## Contributing

I'm not accepting pull requests since it's a project made to learn/study some things and maybe build something else.

## License

Copyright © 2021 Caique Cunha Pereira
