`music21printing` extension
=================

Here is an IPython extension that extends IPython display
system to render music21[1] stream objects as music notation.

It is still at alpha/proof of concept stage.

The extension relies on Lilypond[2] to render the stream objects.

Just have the `musicprinting.py` accessible through your `PYTHONPATH` and
execute the IPython magic command `%load_ext musicprinting`.


[1] http://web.mit.edu/music21/

[2] http://lilypond.org/
