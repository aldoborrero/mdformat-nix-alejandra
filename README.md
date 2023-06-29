# mdformat-nix-alejandra

> Mdformat plugin to format Nix code blocks with alejandra

## Description

mdformat-nix-alejandra is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format Nix code blocks with [alejandra](https://github.com/kamadorueda/alejandra).
The plugin invokes alejandra in a subprocess so having it installed is a requirement.

## Getting started

To make the most of this repository, you should have the following installed:

- [Nix](https://nixos.org/)
- [Direnv](https://direnv.net/)

After cloning this repository and entering inside, run `direnv allow` when prompted, and you will be met with following prompt.

```terminal
🔨 Welcome to mdformat-nix-alejandra

[Tools]

  check  - Checks the source tree
  fmt    - Format the source tree

[general commands]

  menu   - prints this menu

[python]

  pytest - Invoke pytest directly
```

It will also load required dependencies like `python`, `poetry`, `pytest` and `alejandra` to quickly develop.

## Installing (Python)

1. [Install alejandra](https://github.com/kamadorueda/alejandra#prebuilt-binaries)
1. Install mdformat-nix-alejandra
   ```bash
   pip install mdformat-nix-alejandra
   ```

## Usage

```bash
mdformat YOUR_MARKDOWN_FILE.md
```

## License

This project is licensed under the MIT license. See the [LICENSE](./LICENSE) file for more details.

## Support

If you encounter any issues or have any questions, please open an issue on the GitHub repository.

## Acknowledgements

This code is practically based on [mdformat-rustfmt](https://github.com/hukkin/mdformat-rustfmt) plugin written by [hukkin](https://github.com/hukkin), so kudos to him.
