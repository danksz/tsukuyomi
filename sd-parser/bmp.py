# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Bmp(KaitaiStruct):

    class Compressions(Enum):
        rgb = 0
        rle8 = 1
        rle4 = 2
        bitfields = 3
        jpeg = 4
        png = 5
        cmyk = 11
        cmyk_rle8 = 12
        cmyk_rle4 = 13
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_hdr = self._root.FileHeader(self._io, self, self._root)
        self.len_dib_header = self._io.read_s4le()
        _on = self.len_dib_header
        if _on == 104:
            self._raw_dib_header = self._io.read_bytes((self.len_dib_header - 4))
            _io__raw_dib_header = KaitaiStream(BytesIO(self._raw_dib_header))
            self.dib_header = self._root.BitmapCoreHeader(_io__raw_dib_header, self, self._root)
        elif _on == 12:
            self._raw_dib_header = self._io.read_bytes((self.len_dib_header - 4))
            _io__raw_dib_header = KaitaiStream(BytesIO(self._raw_dib_header))
            self.dib_header = self._root.BitmapCoreHeader(_io__raw_dib_header, self, self._root)
        elif _on == 40:
            self._raw_dib_header = self._io.read_bytes((self.len_dib_header - 4))
            _io__raw_dib_header = KaitaiStream(BytesIO(self._raw_dib_header))
            self.dib_header = self._root.BitmapInfoHeader(_io__raw_dib_header, self, self._root)
        elif _on == 124:
            self._raw_dib_header = self._io.read_bytes((self.len_dib_header - 4))
            _io__raw_dib_header = KaitaiStream(BytesIO(self._raw_dib_header))
            self.dib_header = self._root.BitmapCoreHeader(_io__raw_dib_header, self, self._root)
        else:
            self.dib_header = self._io.read_bytes((self.len_dib_header - 4))

    class FileHeader(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/dd183374.aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.ensure_fixed_contents(b"\x42\x4D")
            self.len_file = self._io.read_u4le()
            self.reserved1 = self._io.read_u2le()
            self.reserved2 = self._io.read_u2le()
            self.ofs_bitmap = self._io.read_s4le()


    class BitmapCoreHeader(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/dd183372.aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.image_width = self._io.read_u2le()
            self.image_height = self._io.read_u2le()
            self.num_planes = self._io.read_u2le()
            self.bits_per_pixel = self._io.read_u2le()


    class BitmapInfoHeader(KaitaiStruct):
        """
        .. seealso::
           Source - https://msdn.microsoft.com/en-us/library/dd183376.aspx
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.image_width = self._io.read_u4le()
            self.image_height = self._io.read_u4le()
            self.num_planes = self._io.read_u2le()
            self.bits_per_pixel = self._io.read_u2le()
            self.compression = KaitaiStream.resolve_enum(self._root.Compressions, self._io.read_u4le())
            self.len_image = self._io.read_u4le()
            self.x_px_per_m = self._io.read_u4le()
            self.y_px_per_m = self._io.read_u4le()
            self.num_colors_used = self._io.read_u4le()
            self.num_colors_important = self._io.read_u4le()


    @property
    def image(self):
        if hasattr(self, '_m_image'):
            return self._m_image if hasattr(self, '_m_image') else None

        _pos = self._io.pos()
        self._io.seek(self.file_hdr.ofs_bitmap)
        self._m_image = self._io.read_bytes_full()
        self._io.seek(_pos)
        return self._m_image if hasattr(self, '_m_image') else None


