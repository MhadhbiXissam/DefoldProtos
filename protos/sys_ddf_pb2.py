# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sys_ddf.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sys_ddf.proto',
  package='dmSystemDDF',
  syntax='proto2',
  serialized_options=_b('\n\027com.dynamo.system.protoB\006System'),
  serialized_pb=_b('\n\rsys_ddf.proto\x12\x0b\x64mSystemDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\"\x14\n\x04\x45xit\x12\x0c\n\x04\x63ode\x18\x01 \x02(\x05\"\x0f\n\rToggleProfile\"\x14\n\x12TogglePhysicsDebug\"J\n\x0bStartRecord\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x17\n\x0c\x66rame_period\x18\x02 \x01(\x05:\x01\x32\x12\x0f\n\x03\x66ps\x18\x03 \x01(\x05:\x02\x33\x30\"\x0c\n\nStopRecord\"\\\n\x06Reboot\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\t\x12\x0c\n\x04\x61rg2\x18\x02 \x01(\t\x12\x0c\n\x04\x61rg3\x18\x03 \x01(\t\x12\x0c\n\x04\x61rg4\x18\x04 \x01(\t\x12\x0c\n\x04\x61rg5\x18\x05 \x01(\t\x12\x0c\n\x04\x61rg6\x18\x06 \x01(\t\"$\n\x08SetVsync\x12\x18\n\rswap_interval\x18\x01 \x02(\x05:\x01\x31\"\'\n\x12SetUpdateFrequency\x12\x11\n\tfrequency\x18\x01 \x02(\x05\x42!\n\x17\x63om.dynamo.system.protoB\x06System')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,])




_EXIT = _descriptor.Descriptor(
  name='Exit',
  full_name='dmSystemDDF.Exit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dmSystemDDF.Exit.code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=68,
  serialized_end=88,
)


_TOGGLEPROFILE = _descriptor.Descriptor(
  name='ToggleProfile',
  full_name='dmSystemDDF.ToggleProfile',
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
  serialized_start=90,
  serialized_end=105,
)


_TOGGLEPHYSICSDEBUG = _descriptor.Descriptor(
  name='TogglePhysicsDebug',
  full_name='dmSystemDDF.TogglePhysicsDebug',
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
  serialized_start=107,
  serialized_end=127,
)


_STARTRECORD = _descriptor.Descriptor(
  name='StartRecord',
  full_name='dmSystemDDF.StartRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='dmSystemDDF.StartRecord.file_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_period', full_name='dmSystemDDF.StartRecord.frame_period', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fps', full_name='dmSystemDDF.StartRecord.fps', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=30,
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
  serialized_start=129,
  serialized_end=203,
)


_STOPRECORD = _descriptor.Descriptor(
  name='StopRecord',
  full_name='dmSystemDDF.StopRecord',
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
  serialized_start=205,
  serialized_end=217,
)


_REBOOT = _descriptor.Descriptor(
  name='Reboot',
  full_name='dmSystemDDF.Reboot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg1', full_name='dmSystemDDF.Reboot.arg1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg2', full_name='dmSystemDDF.Reboot.arg2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg3', full_name='dmSystemDDF.Reboot.arg3', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg4', full_name='dmSystemDDF.Reboot.arg4', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg5', full_name='dmSystemDDF.Reboot.arg5', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg6', full_name='dmSystemDDF.Reboot.arg6', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=219,
  serialized_end=311,
)


_SETVSYNC = _descriptor.Descriptor(
  name='SetVsync',
  full_name='dmSystemDDF.SetVsync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swap_interval', full_name='dmSystemDDF.SetVsync.swap_interval', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=1,
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
  serialized_start=313,
  serialized_end=349,
)


_SETUPDATEFREQUENCY = _descriptor.Descriptor(
  name='SetUpdateFrequency',
  full_name='dmSystemDDF.SetUpdateFrequency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency', full_name='dmSystemDDF.SetUpdateFrequency.frequency', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=351,
  serialized_end=390,
)

DESCRIPTOR.message_types_by_name['Exit'] = _EXIT
DESCRIPTOR.message_types_by_name['ToggleProfile'] = _TOGGLEPROFILE
DESCRIPTOR.message_types_by_name['TogglePhysicsDebug'] = _TOGGLEPHYSICSDEBUG
DESCRIPTOR.message_types_by_name['StartRecord'] = _STARTRECORD
DESCRIPTOR.message_types_by_name['StopRecord'] = _STOPRECORD
DESCRIPTOR.message_types_by_name['Reboot'] = _REBOOT
DESCRIPTOR.message_types_by_name['SetVsync'] = _SETVSYNC
DESCRIPTOR.message_types_by_name['SetUpdateFrequency'] = _SETUPDATEFREQUENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Exit = _reflection.GeneratedProtocolMessageType('Exit', (_message.Message,), dict(
  DESCRIPTOR = _EXIT,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.Exit)
  ))
_sym_db.RegisterMessage(Exit)

ToggleProfile = _reflection.GeneratedProtocolMessageType('ToggleProfile', (_message.Message,), dict(
  DESCRIPTOR = _TOGGLEPROFILE,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.ToggleProfile)
  ))
_sym_db.RegisterMessage(ToggleProfile)

TogglePhysicsDebug = _reflection.GeneratedProtocolMessageType('TogglePhysicsDebug', (_message.Message,), dict(
  DESCRIPTOR = _TOGGLEPHYSICSDEBUG,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.TogglePhysicsDebug)
  ))
_sym_db.RegisterMessage(TogglePhysicsDebug)

StartRecord = _reflection.GeneratedProtocolMessageType('StartRecord', (_message.Message,), dict(
  DESCRIPTOR = _STARTRECORD,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.StartRecord)
  ))
_sym_db.RegisterMessage(StartRecord)

StopRecord = _reflection.GeneratedProtocolMessageType('StopRecord', (_message.Message,), dict(
  DESCRIPTOR = _STOPRECORD,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.StopRecord)
  ))
_sym_db.RegisterMessage(StopRecord)

Reboot = _reflection.GeneratedProtocolMessageType('Reboot', (_message.Message,), dict(
  DESCRIPTOR = _REBOOT,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.Reboot)
  ))
_sym_db.RegisterMessage(Reboot)

SetVsync = _reflection.GeneratedProtocolMessageType('SetVsync', (_message.Message,), dict(
  DESCRIPTOR = _SETVSYNC,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.SetVsync)
  ))
_sym_db.RegisterMessage(SetVsync)

SetUpdateFrequency = _reflection.GeneratedProtocolMessageType('SetUpdateFrequency', (_message.Message,), dict(
  DESCRIPTOR = _SETUPDATEFREQUENCY,
  __module__ = 'sys_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmSystemDDF.SetUpdateFrequency)
  ))
_sym_db.RegisterMessage(SetUpdateFrequency)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
