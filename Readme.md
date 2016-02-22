# Macnote.vim

Simplified and friendly note management plugin.

## Basic features

* Write note with markdown and yaml as frontmatter.
* All extended markdown syntax included, visit [sample page](https://chemzqm.me/sample).
* Preview in Chrome with range and auto reload support.
* Create, delete and search note with command.
* Unite source for easier note management.
* Support both neovim/vim job-control for async parsing.

## Install

Take [vundle](https://github.com/VundleVim/Vundle.vim) as example:

    Plugin 'chemzqm/macnote.vim'

`misaka` and `pygments` is used for high preformance markdown parse and syntax
highlight, you can install them via:

    pip install pygments misaka

If your vim doesn't support, you can install
[vimproc.vim](https://github.com/Shougo/vimproc.vim)

    Plugin 'Shougo/vimproc.vim'

to do async job.

## Usage

* Create or edit note:

        :Note {path}

  _{path} could include folder, use `<tab>` for auto complete_

* Delete note;

        :NoteDelete {path}

* Search note:

        :[bang]NoteSearch {path}

* Preview current note:

        :Preview

* Auto reload preview on file save and cursor hold:

        :PreviewAuto

  _Chrome tab would be close on buffer delete_

* Open unite source for note:

        :Unite note

  _There is `open` `delete` `add` action for unite note source_

  [unite.vim](https://github.com/Shougo/unite.vim) has support for sort by file
  modify time, you can make your lastest changed note comes first by:

        call unite#custom#source(
          \  'note', 'sorters', ['sorter_ftime', 'sorter_reverse']
          \)

## Configurations

All configurations are optional.

* `g:macnote_note_directory` could be used to set root directory of notes,
  defaults: `~/Documents/notes`
* `g:note_cwindow_open` could be set to `1` if you want open quickfix list after
  search.
* `g:note_unite_quickfix` if you have unite quickfix source, set it to `1` to
  open unite quickfix source after search.
* `g:unite_note_ag_opts` is used for set options for ag, which is ued for file
  search in unite note, default value is `--nocolor --nogroup -g ''`

Use `:h macnote` inside vim to get more info.

## License

MIT
