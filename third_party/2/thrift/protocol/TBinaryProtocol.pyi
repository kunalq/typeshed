# Stubs for thrift.protocol.TBinaryProtocol (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from .TProtocol import *

class TBinaryProtocol(TProtocolBase):
    VERSION_MASK = ...  # type: Any
    VERSION_1 = ...  # type: Any
    TYPE_MASK = ...  # type: Any
    strictRead = ...  # type: Any
    strictWrite = ...  # type: Any
    def __init__(self, trans, strictRead=..., strictWrite=...) -> None: ...
    def writeMessageBegin(self, name, type, seqid): ...
    def writeMessageEnd(self): ...
    def writeStructBegin(self, name): ...
    def writeStructEnd(self): ...
    def writeFieldBegin(self, name, type, id): ...
    def writeFieldEnd(self): ...
    def writeFieldStop(self): ...
    def writeMapBegin(self, ktype, vtype, size): ...
    def writeMapEnd(self): ...
    def writeListBegin(self, etype, size): ...
    def writeListEnd(self): ...
    def writeSetBegin(self, etype, size): ...
    def writeSetEnd(self): ...
    def writeBool(self, bool): ...
    def writeByte(self, byte): ...
    def writeI16(self, i16): ...
    def writeI32(self, i32): ...
    def writeI64(self, i64): ...
    def writeDouble(self, dub): ...
    def writeString(self, str): ...
    def readMessageBegin(self): ...
    def readMessageEnd(self): ...
    def readStructBegin(self): ...
    def readStructEnd(self): ...
    def readFieldBegin(self): ...
    def readFieldEnd(self): ...
    def readMapBegin(self): ...
    def readMapEnd(self): ...
    def readListBegin(self): ...
    def readListEnd(self): ...
    def readSetBegin(self): ...
    def readSetEnd(self): ...
    def readBool(self): ...
    def readByte(self): ...
    def readI16(self): ...
    def readI32(self): ...
    def readI64(self): ...
    def readDouble(self): ...
    def readString(self): ...

class TBinaryProtocolFactory:
    strictRead = ...  # type: Any
    strictWrite = ...  # type: Any
    def __init__(self, strictRead=..., strictWrite=...) -> None: ...
    def getProtocol(self, trans): ...

class TBinaryProtocolAccelerated(TBinaryProtocol): ...

class TBinaryProtocolAcceleratedFactory:
    def getProtocol(self, trans): ...
