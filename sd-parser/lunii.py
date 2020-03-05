# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

import wav
import bmp
class Lunii(KaitaiStruct):

    class Lbool(Enum):
        enabled = 1
        disabled = 65535
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = self._io.read_bytes(self.fileoffset)
        self.contents = self._root.ContentStruct(self._io, self, self._root)

    class StoryStruct(KaitaiStruct):
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
        def abs_start_address(self):
            if hasattr(self, '_m_abs_start_address'):
                return self._m_abs_start_address if hasattr(self, '_m_abs_start_address') else None

            self._m_abs_start_address = (self._root.fileoffset + (self.start_address * 512))
            return self._m_abs_start_address if hasattr(self, '_m_abs_start_address') else None

        @property
        def story_info(self):
            if hasattr(self, '_m_story_info'):
                return self._m_story_info if hasattr(self, '_m_story_info') else None

            _pos = self._io.pos()
            self._io.seek(self.abs_start_address)
            self._m_story_info = self._root.StoryInfoStruct(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_story_info if hasattr(self, '_m_story_info') else None


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
                self.stories[i] = self._root.StoryStruct(self._io, self, self._root)



    class StoryInfoStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nbr_nodes = self._io.read_u2be()
            self.factory_disabled = self._io.read_u1()
            self.version = self._io.read_u2be()
            self.padding = self._io.read_bytes((512 - 5))
            self.nodes = [None] * (self.nbr_nodes)
            for i in range(self.nbr_nodes):
                self.nodes[i] = self._root.NodeStruct(self._io, self, self._root)



    class NodeStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uuid = self._io.read_bytes(16)
            self.image_start_sector = self._io.read_u4be()
            self.image_size = self._io.read_u4be()
            self.audio_start_sector = self._io.read_u4be()
            self.audio_size = self._io.read_u4be()
            self._raw_navigation = self._io.read_bytes((512 - 32))
            _io__raw_navigation = KaitaiStream(BytesIO(self._raw_navigation))
            self.navigation = self._root.NavigationStruct(_io__raw_navigation, self, self._root)

        @property
        def image(self):
            if hasattr(self, '_m_image'):
                return self._m_image if hasattr(self, '_m_image') else None

            if self.image_size != 4294967295:
                _pos = self._io.pos()
                self._io.seek(self.image_start_address)
                self._raw__m_image = self._io.read_bytes((self.image_size * 512))
                _io__raw__m_image = KaitaiStream(BytesIO(self._raw__m_image))
                self._m_image = bmp.Bmp(_io__raw__m_image)
                self._io.seek(_pos)

            return self._m_image if hasattr(self, '_m_image') else None

        @property
        def audio(self):
            if hasattr(self, '_m_audio'):
                return self._m_audio if hasattr(self, '_m_audio') else None

            if self.audio_size != 4294967295:
                _pos = self._io.pos()
                self._io.seek(self.audio_start_address)
                self._raw__m_audio = self._io.read_bytes((self.audio_size * 512))
                _io__raw__m_audio = KaitaiStream(BytesIO(self._raw__m_audio))
                self._m_audio = wav.Wav(_io__raw__m_audio)
                self._io.seek(_pos)

            return self._m_audio if hasattr(self, '_m_audio') else None

        @property
        def story_start_address(self):
            if hasattr(self, '_m_story_start_address'):
                return self._m_story_start_address if hasattr(self, '_m_story_start_address') else None

            self._m_story_start_address = self._parent._parent.abs_start_address
            return self._m_story_start_address if hasattr(self, '_m_story_start_address') else None

        @property
        def audio_start_address(self):
            if hasattr(self, '_m_audio_start_address'):
                return self._m_audio_start_address if hasattr(self, '_m_audio_start_address') else None

            self._m_audio_start_address = (self.story_start_address + ((1 + self.audio_start_sector) * 512))
            return self._m_audio_start_address if hasattr(self, '_m_audio_start_address') else None

        @property
        def image_start_address(self):
            if hasattr(self, '_m_image_start_address'):
                return self._m_image_start_address if hasattr(self, '_m_image_start_address') else None

            self._m_image_start_address = (self.story_start_address + ((1 + self.image_start_sector) * 512))
            return self._m_image_start_address if hasattr(self, '_m_image_start_address') else None


    class NavigationStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.action_on_ok = self._io.read_u2be()
            self.option_in_transition = self._io.read_u2be()
            self.chosen_option = self._io.read_u2be()
            self.wheel_enabled = KaitaiStream.resolve_enum(self._root.Lbool, self._io.read_u2be())
            self.ok_enabled = KaitaiStream.resolve_enum(self._root.Lbool, self._io.read_u2be())
            self.home_enabled = KaitaiStream.resolve_enum(self._root.Lbool, self._io.read_u2be())
            self.paused_enabled = KaitaiStream.resolve_enum(self._root.Lbool, self._io.read_u2be())
            self.autojump_at_audio_ends_enabled = KaitaiStream.resolve_enum(self._root.Lbool, self._io.read_u2be())


    @property
    def fileoffset(self):
        if hasattr(self, '_m_fileoffset'):
            return self._m_fileoffset if hasattr(self, '_m_fileoffset') else None

        self._m_fileoffset = 51200000
        return self._m_fileoffset if hasattr(self, '_m_fileoffset') else None


