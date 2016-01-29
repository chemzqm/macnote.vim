# Macdown.vim

A simplified and flexible markdown solution for vim user on Mac.

Using applescript instead of a server to enhance the exprience of live preview.

## Basic features

* Preview in Chrome with range and auto reload support.
* Async markdown parse.
* Build in unite source, find and search your notes become much easier.
* You can publish genereated html with just scp command.

## Install

Take [vundle](https://github.com/VundleVim/Vundle.vim) as example:

    Plugin 'chemzqm/macdown.vim'

[vimproc.vim](https: //github.com/Shougo/vimproc.vim) is needed for processing
  markdown files in async.

    Plugin 'Shougo/vimproc.vim'

## Usage

To preview current markdown file, type:

    :Preview

Preview with range, eg:

    :1,10Preview

Or visual select a range, and use:

    :'<,'>Preview

To toggle auto preview for current file, type:

    :PreviewAuto

The chrome page would be refreshed on CursorHold and BufWrite

## Configuration

You can configure almost anything, see:
[doc/macdown.txt](https://github.com/chemzqm/macdown.vim/blob/master/doc/macdown.txt)


## TODO

* Scrollbind for vim and Chrome
