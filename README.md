# PLY Lexer and Parser

## Usage

This is a guide for this project.

### Makefile

For conviniece this project comes with a Makefile. To run execute de shell command
```bash
$ make test
```
and it will lex and parse the default test file, which is `prof-test.txt` and compare its output with the expected.

The compilation of **python** commands for running this the files directly can be found in the Makefile.

There are rules for runing the lexer and parser individually and for testing the output against expected outputs.

### Parser
To run the parser:

```bash
$ make parse
```

Default input file can be modified by changing `IN` variable.

```bash
$ make parse IN=./file/path/file.txt
```

### Output
Default outputs will be in `out/`. Can be modified by changing the `OUT` in the Makefile execution.

```bash
make test OUT=./relative-or-full/path/file.txt
```