# ============================================================================
# FILE: note.py
# AUTHOR: Qiming Zhao <chemzqm@gmail.com>
# License: MIT license
# ============================================================================
# pylint: disable=E0401,C0411
import os
import time
from .base import Base

def timeago(now, seconds):
    diff = now - seconds
    if diff <= 0:
        return 'just now'
    if diff < 60:
        return str(int(diff)) + ' seconds ago'
    if diff/60 < 60:
        return str(int(diff/60)) + ' minutes ago'
    if diff/3.6e+3 < 24:
        return str(int(diff/3.6e+3)) + ' hours ago'
    if diff/8.64e+4 < 24:
        return str(int(diff/8.64e+4)) + ' days ago'
    if diff/6.048e+5 < 4.34812:
        return str(int(diff/6.048e+5)) + ' weeks ago'
    if diff/2.63e+6 < 12:
        return str(int(diff/2.63e+6)) + ' months ago'
    return str(int(diff/3.156e+7)) + 'years ago'

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'note'
        self.kind = 'file'

    def on_init(self, context):
        root = self.vim.vars.get('macnote_note_directory')
        if not root:
            root = os.path.expanduser('~/Documents/notes')
        context['__root'] = root

    def highlight(self):
        self.vim.command('highlight default link deniteNoteName Title')
        self.vim.command('highlight default link deniteNoteTime Statement')

    def define_syntax(self):
        self.vim.command(r'syntax match deniteNote /^.*$/ ' +
                         r'containedin=' + self.syntax_name)
        self.vim.command(r'syntax match deniteNoteName /^\s\?\S\+/ ' +
                         r'contained containedin=deniteNote')
        self.vim.command(r'syntax match deniteNoteTime /(.\{-})/ ' +
                         r'contained containedin=deniteNote')

    def gather_candidates(self, context):
        root = context['__root']
        candidates = []

        items = os.scandir(root)
        now = time.time()
        for item in items:
            if item.is_file():
                mtime = item.stat().st_mtime
                candidates.append({
                    'word': '%s (%s)' % (item.name, timeago(now, mtime)),
                    'action__path': item.path,
                    'source_mtime': mtime
                    })

        candidates = sorted(candidates, key=lambda item: item['source_mtime'],
                            reverse=True)
        return candidates
