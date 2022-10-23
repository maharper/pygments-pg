# pygments-pg

A [Pygments](https://pygments.org) lexer for syntax highlighting of pg language code.
[WeBWorK](https://webwork.maa.org/wiki/) problems are written in the pg language.
PG is an extension to PERL and the lexer is based on the PERL Pygments lexer.

## Status

**This is a work in progress - status - barely begun**.
Currently all the lexer does is enable Pygments to recoginize code blocks tagged with `pg` or `PG`.
This lexer returns the perl lexer, so Pygments highlights pg code as though it was perl code.

## Roadmap

* Build the pg lexer by adding the features of pg code, extending the perl lexer.

## Usage

Install pygments-pg into the (python) environment where you are using Pygments.
Pygments should find the lexer automatically and use it to hightlight code tagged `pg`.
