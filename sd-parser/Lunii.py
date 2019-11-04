#!/usr/bin/env python

# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO

if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Lunii(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        pass

    class ContentStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nbr_stories = self._io.read_u2be()
            self.stories = [None] * (self.nbr_stories)
            for i in range(self.nbr_stories):
                self.stories[i] = self._root.StoriesLocationStruct(self._io, self, self._root)



    class StoriesLocationStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start_address = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.unknown = self._io.read_u4be()


    @property
    def contents(self):
        if hasattr(self, '_m_contents'):
            return self._m_contents if hasattr(self, '_m_contents') else None

        _pos = self._io.pos()
#       self._io.seek(16384)
        self._io.seek(51200000)
        self._m_contents = self._root.ContentStruct(self._io, self, self._root)
        self._io.seek(_pos)
        return self._m_contents if hasattr(self, '_m_contents') else None


