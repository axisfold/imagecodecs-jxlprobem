import imagecodecs

fname = "jxl_q10.jxl"
with open(fname, 'rb') as fh:
    jxlbytes = fh.read()
nparr = imagecodecs.jpegxl_decode(jxlbytes)