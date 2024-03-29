import urwid


def show_or_exit(key: str):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))


txt = urwid.Text(u"Hello world!")
fill = urwid.Filler(txt, "top")
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
