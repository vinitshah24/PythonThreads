Data types must be specified when using a **multiprocessing.Value** or  **multiprocessing.Array** .

This can be challenging to beginners that are not familiar with c data types, specifically with the string type codes commonly used in C **printf()** statements.

Internally, when we use a string type code, the multiprocessing.sharedctypes module will convert them to Python types from the ctypes module.

Reviewing the code, we can see a [**typecode_to_type** dictionary](https://github.com/python/cpython/blob/3.10/Lib/multiprocessing/sharedctypes.py#L25) that maps type codes to ctype types.

For example:

|  | **typecode_to_type**=**{** **'c'**:**ctypes**.**c_char**, **'u'**:**ctypes**.**c_wchar**, **'b'**:**ctypes**.**c_byte**, **'B'**:**ctypes**.**c_ubyte**, **'h'**:**ctypes**.**c_short**, **'H'**:**ctypes**.**c_ushort**, **'i'**:**ctypes**.**c_int**, **'I'**:**ctypes**.**c_uint**, **'l'**:**ctypes**.**c_long**, **'L'**:**ctypes**.**c_ulong**, **'q'**:**ctypes**.**c_longlong**,**'Q'**:**ctypes**.**c_ulonglong**, **'f'**:**ctypes**.**c_float**, **'d'**:**ctypes**.**c**_double **}** |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
