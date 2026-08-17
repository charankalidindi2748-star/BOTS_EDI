from .envelope import recorddefs, structure, nextmessage

syntax = {
    'version': '00403',        # only for sending
    'contenttype': 'application/X12',
    'charset': 'us-ascii',
    'field_sep': '*',
    'sfield_sep': '>',
    'record_sep': '~',         # <-- this line is essential
    'skip_char': '\r\n'
}