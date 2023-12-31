# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine_ddf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ddf_extensions_pb2 as ddf__extensions__pb2
import ddf_math_pb2 as ddf__math__pb2
import lua_ddf_pb2 as lua__ddf__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='engine_ddf.proto',
  package='dmEngineDDF',
  syntax='proto2',
  serialized_options=_b('\n\027com.dynamo.engine.protoB\006Engine'),
  serialized_pb=_b('\n\x10\x65ngine_ddf.proto\x12\x0b\x64mEngineDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\x1a\rlua_ddf.proto\"\t\n\x07HideApp\"0\n\tRunScript\x12#\n\x06module\x18\x01 \x02(\x0b\x32\x13.dmLuaDDF.LuaModuleB!\n\x17\x63om.dynamo.engine.protoB\x06\x45ngine')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,lua__ddf__pb2.DESCRIPTOR,])




_HIDEAPP = _descriptor.Descriptor(
  name='HideApp',
  full_name='dmEngineDDF.HideApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=95,
)


_RUNSCRIPT = _descriptor.Descriptor(
  name='RunScript',
  full_name='dmEngineDDF.RunScript',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='dmEngineDDF.RunScript.module', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=145,
)

_RUNSCRIPT.fields_by_name['module'].message_type = lua__ddf__pb2._LUAMODULE
DESCRIPTOR.message_types_by_name['HideApp'] = _HIDEAPP
DESCRIPTOR.message_types_by_name['RunScript'] = _RUNSCRIPT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HideApp = _reflection.GeneratedProtocolMessageType('HideApp', (_message.Message,), dict(
  DESCRIPTOR = _HIDEAPP,
  __module__ = 'engine_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmEngineDDF.HideApp)
  ))
_sym_db.RegisterMessage(HideApp)

RunScript = _reflection.GeneratedProtocolMessageType('RunScript', (_message.Message,), dict(
  DESCRIPTOR = _RUNSCRIPT,
  __module__ = 'engine_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmEngineDDF.RunScript)
  ))
_sym_db.RegisterMessage(RunScript)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
