# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nfile.proto\x12\x04\x66ile\"\x83\x01\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\x0c\x12\x17\n\nupdated_at\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12\x17\n\ncreated_at\x18\x04 \x01(\x02H\x01\x88\x01\x01\x42\r\n\x0b_updated_atB\r\n\x0b_created_at\"\'\n\x12\x43reateFileResponse\x12\x11\n\tfile_uuid\x18\x01 \x01(\t\"#\n\x0eGetFileRequest\x12\x11\n\tfile_uuid\x18\x01 \x01(\t\"#\n\x0fGetFileResponse\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t2\x81\x01\n\x04\x46ile\x12\x41\n\nCreateFile\x12\x17.file.CreateFileRequest\x1a\x18.file.CreateFileResponse(\x01\x12\x36\n\x07GetFile\x12\x14.file.GetFileRequest\x1a\x15.file.GetFileResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEFILEREQUEST']._serialized_start=21
  _globals['_CREATEFILEREQUEST']._serialized_end=152
  _globals['_CREATEFILERESPONSE']._serialized_start=154
  _globals['_CREATEFILERESPONSE']._serialized_end=193
  _globals['_GETFILEREQUEST']._serialized_start=195
  _globals['_GETFILEREQUEST']._serialized_end=230
  _globals['_GETFILERESPONSE']._serialized_start=232
  _globals['_GETFILERESPONSE']._serialized_end=267
  _globals['_FILE']._serialized_start=270
  _globals['_FILE']._serialized_end=399
# @@protoc_insertion_point(module_scope)
