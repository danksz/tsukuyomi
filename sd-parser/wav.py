# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Wav(KaitaiStruct):
    """The WAVE file format is a subset of Microsoft's RIFF specification for the
    storage of multimedia files. A RIFF file starts out with a file header
    followed by a sequence of data chunks. A WAVE file is often just a RIFF
    file with a single "WAVE" chunk which consists of two sub-chunks --
    a "fmt " chunk specifying the data format and a "data" chunk containing
    the actual sample data.
    
    This Kaitai implementation was written by John Byrd of Gigantic Software
    (jbyrd@giganticsoftware.com), and it is likely to contain bugs.
    
    .. seealso::
       Source - https://www.loc.gov/preservation/digital/formats/fdd/fdd000001.shtml
    """

    class WFormatTagType(Enum):
        unknown = 0
        pcm = 1
        adpcm = 2
        ieee_float = 3
        alaw = 6
        mulaw = 7
        dvi_adpcm = 17
        dolby_ac3_spdif = 146
        extensible = 65534
        development = 65535

    class ChunkType(Enum):
        fmt = 544501094
        bext = 1650817140
        cue = 1668637984
        data = 1684108385
        minf = 1835626086
        regn = 1919248238
        umid = 1970104676
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.riff_id = self._io.ensure_fixed_contents(b"\x52\x49\x46\x46")
        self.file_size = self._io.read_u4le()
        self.wave_id = self._io.ensure_fixed_contents(b"\x57\x41\x56\x45")
        self._raw_chunks = self._io.read_bytes((self.file_size - 5))
        _io__raw_chunks = KaitaiStream(BytesIO(self._raw_chunks))
        self.chunks = self._root.ChunksType(_io__raw_chunks, self, self._root)

    class SampleType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sample = self._io.read_u2le()


    class FormatChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.w_format_tag = KaitaiStream.resolve_enum(self._root.WFormatTagType, self._io.read_u2le())
            self.n_channels = self._io.read_u2le()
            self.n_samples_per_sec = self._io.read_u4le()
            self.n_avg_bytes_per_sec = self._io.read_u4le()
            self.n_block_align = self._io.read_u2le()
            self.w_bits_per_sample = self._io.read_u2le()
            if not (self.is_basic_pcm):
                self.cb_size = self._io.read_u2le()

            if self.is_cb_size_meaningful:
                self.w_valid_bits_per_sample = self._io.read_u2le()

            if self.is_extensible:
                self.channel_mask_and_subformat = self._root.ChannelMaskAndSubformatType(self._io, self, self._root)


        @property
        def is_extensible(self):
            if hasattr(self, '_m_is_extensible'):
                return self._m_is_extensible if hasattr(self, '_m_is_extensible') else None

            self._m_is_extensible = self.w_format_tag == self._root.WFormatTagType.extensible
            return self._m_is_extensible if hasattr(self, '_m_is_extensible') else None

        @property
        def is_basic_pcm(self):
            if hasattr(self, '_m_is_basic_pcm'):
                return self._m_is_basic_pcm if hasattr(self, '_m_is_basic_pcm') else None

            self._m_is_basic_pcm = self.w_format_tag == self._root.WFormatTagType.pcm
            return self._m_is_basic_pcm if hasattr(self, '_m_is_basic_pcm') else None

        @property
        def is_basic_float(self):
            if hasattr(self, '_m_is_basic_float'):
                return self._m_is_basic_float if hasattr(self, '_m_is_basic_float') else None

            self._m_is_basic_float = self.w_format_tag == self._root.WFormatTagType.ieee_float
            return self._m_is_basic_float if hasattr(self, '_m_is_basic_float') else None

        @property
        def is_cb_size_meaningful(self):
            if hasattr(self, '_m_is_cb_size_meaningful'):
                return self._m_is_cb_size_meaningful if hasattr(self, '_m_is_cb_size_meaningful') else None

            self._m_is_cb_size_meaningful =  ((not (self.is_basic_pcm)) and (self.cb_size != 0)) 
            return self._m_is_cb_size_meaningful if hasattr(self, '_m_is_cb_size_meaningful') else None


    class GuidType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data1 = self._io.read_u4le()
            self.data2 = self._io.read_u2le()
            self.data3 = self._io.read_u2le()
            self.data4 = self._io.read_u4be()
            self.data4a = self._io.read_u4be()


    class CuePointType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw_name = self._io.read_u4le()
            self.dw_position = self._io.read_u4le()
            self.fcc_chunk = self._io.read_u4le()
            self.dw_chunk_start = self._io.read_u4le()
            self.dw_block_start = self._io.read_u4le()
            self.dw_sample_offset = self._io.read_u4le()


    class DataChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes_full()


    class SamplesType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.samples = self._io.read_u4le()


    class ChannelMaskAndSubformatType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw_channel_mask = self._root.ChannelMaskType(self._io, self, self._root)
            self.subformat = self._root.GuidType(self._io, self, self._root)


    class ChunksType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk = []
            i = 0
            while not self._io.is_eof():
                self.chunk.append(self._root.ChunkType(self._io, self, self._root))
                i += 1



    class CueChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw_cue_points = self._io.read_u4le()
            if self.dw_cue_points != 0:
                self.cue_points = [None] * (self.dw_cue_points)
                for i in range(self.dw_cue_points):
                    self.cue_points[i] = self._root.CuePointType(self._io, self, self._root)




    class ChannelMaskType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.front_right_of_center = self._io.read_bits_int(1) != 0
            self.front_left_of_center = self._io.read_bits_int(1) != 0
            self.back_right = self._io.read_bits_int(1) != 0
            self.back_left = self._io.read_bits_int(1) != 0
            self.low_frequency = self._io.read_bits_int(1) != 0
            self.front_center = self._io.read_bits_int(1) != 0
            self.front_right = self._io.read_bits_int(1) != 0
            self.front_left = self._io.read_bits_int(1) != 0
            self.top_center = self._io.read_bits_int(1) != 0
            self.side_right = self._io.read_bits_int(1) != 0
            self.side_left = self._io.read_bits_int(1) != 0
            self.back_center = self._io.read_bits_int(1) != 0
            self.top_back_left = self._io.read_bits_int(1) != 0
            self.top_front_right = self._io.read_bits_int(1) != 0
            self.top_front_center = self._io.read_bits_int(1) != 0
            self.top_front_left = self._io.read_bits_int(1) != 0
            self.unused1 = self._io.read_bits_int(6)
            self.top_back_right = self._io.read_bits_int(1) != 0
            self.top_back_center = self._io.read_bits_int(1) != 0
            self.unused2 = self._io.read_bits_int(8)


    class ChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk_id = self._io.read_u4be()
            self.len = self._io.read_u4le()
            _on = self.chunk_id
            if _on == 1684108385:
                self._raw_data = self._io.read_bytes(self.len)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = self._root.DataChunkType(_io__raw_data, self, self._root)
            elif _on == 1668637984:
                self._raw_data = self._io.read_bytes(self.len)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = self._root.CueChunkType(_io__raw_data, self, self._root)
            elif _on == 1650817140:
                self._raw_data = self._io.read_bytes(self.len)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = self._root.BextChunkType(_io__raw_data, self, self._root)
            elif _on == 1718449184:
                self._raw_data = self._io.read_bytes(self.len)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = self._root.FormatChunkType(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(self.len)


    class BextChunkType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.description = (self._io.read_bytes(256)).decode(u"ASCII")
            self.originator = (self._io.read_bytes(32)).decode(u"ASCII")
            self.originator_reference = (self._io.read_bytes(32)).decode(u"ASCII")
            self.origination_date = (self._io.read_bytes(10)).decode(u"ASCII")
            self.origination_time = (self._io.read_bytes(8)).decode(u"ASCII")
            self.time_reference_low = self._io.read_u4le()
            self.time_reference_high = self._io.read_u4le()
            self.version = self._io.read_u2le()
            self.umid = self._io.read_bytes(64)
            self.loudness_value = self._io.read_u2le()
            self.loudness_range = self._io.read_u2le()
            self.max_true_peak_level = self._io.read_u2le()
            self.max_momentary_loudness = self._io.read_u2le()
            self.max_short_term_loudness = self._io.read_u2le()


    @property
    def format_chunk(self):
        if hasattr(self, '_m_format_chunk'):
            return self._m_format_chunk if hasattr(self, '_m_format_chunk') else None

        self._m_format_chunk = self.chunks.chunk[0].data
        return self._m_format_chunk if hasattr(self, '_m_format_chunk') else None


