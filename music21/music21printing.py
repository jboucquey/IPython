# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# An IPython extension to display musical notation in notebooks
# ==================
# 
# This notebook is meant to be saved as `.py` in order to be used as an extension

# <codecell>

import music21
import tempfile, os

def add_preamble(fin, fout):
    """ This is a rough way to ensure that the .ly code will be rendered
        without any additional margins.
        TODO: check and validate this way of working
    """
    if isinstance(fin, str):
        fin = open(fin)
    if isinstance(fout, str):
        fout = open(fout, 'w')
    fout.write('\include "lilypond-book-preamble.ly"\n')
    for l in fin:
        fout.write(l)
    fin.close()
    fout.close()

def make_stream_png(stream_obj):
    """ Takes a music21 stream object and returns the path of a temporary file 
        containing the snippet representation of the stream
    """
    h1, ly_file = tempfile.mkstemp('.ly')
    h2, ly_post_file = tempfile.mkstemp('-post.ly')
    h3, ly_png = tempfile.mkstemp()
    
    # Generate the lilypond file and add the preamble
    stream_obj.write('lily', ly_file)
    add_preamble(ly_file, ly_post_file)
    
    # Generate the corresponding image
    # TODO: Should trap all possible errors here!
    # TODO: Should take lilypond config out of music21 environment
    os.system('lilypond --png -o ' + ly_png + ' ' + ly_post_file)
    
    # Delete the two working .ly files
    os.remove(ly_file)
    os.remove(ly_post_file)
    
    # Return the path to the generated image
    return (ly_png + '.png')

def render_stream(obj):
    img_path = make_stream_png(obj)
    img_data = open(img_path).read()
    os.remove(img_path)
    return img_data

def load_ipython_extension(ip):
    png_formatter = ip.display_formatter.formatters['image/png']
    png_formatter.for_type_by_name('music21.stream', 'Stream', render_stream)

# <markdowncell>

# To install this, download it as `.py` script and make it accessible to your `PYTHONPATH`.
# It can then be loaded by:
#     
# `%load_ext music21printing`

