# Unit Test plugin for Thonny

This plugin adds a command in Thonny to run [unit tests](https://docs.python.org/3/library/unittest.html) in the currently opened directory.

## Usage
Install the plugin. You can then issue the command to run unit tests, either by pressing the keyboard shortcut F6, or by selecting the command from the toolbar or the run menu. The test results are then displayed in their own frame.

## Development
This project used [Poetry](https://python-poetry.org/). Install Poetry, then you can use `poetry install` to install the dependencies. Next use `poetry build` to make new `.whl` files.

For rapid development, consider linking the `thonnycontrib/` directory to the `site-packages` directory. You find this directory in the 'Manage plug-ins' window in Thonny.

```sh
ln -s ~/Code/thonny-unittest/thonnycontrib ~/.local/lib/python3.10//site-packages/
```

## Acknowledgements
The 'tick' icon is part of the ["Silk" icon set by Mark James](https://github.com/markjames/famfamfam-silk-icons), licensed under the [Creative Commons Attribution 2.5 License](https://creativecommons.org/licenses/by/2.5/). 