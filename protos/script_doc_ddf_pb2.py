# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: script_doc_ddf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='script_doc_ddf.proto',
  package='dmScriptDoc',
  syntax='proto2',
  serialized_options=_b('\n\032com.dynamo.scriptdoc.protoB\tScriptDoc'),
  serialized_pb=_b('\n\x14script_doc_ddf.proto\x12\x0b\x64mScriptDoc\"5\n\tParameter\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03\x64oc\x18\x02 \x02(\t\x12\r\n\x05types\x18\x03 \x03(\t\"1\n\x06Member\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03\x64oc\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\"7\n\x0bReturnValue\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03\x64oc\x18\x02 \x02(\t\x12\r\n\x05types\x18\x03 \x03(\t\"\xcc\x02\n\x07\x45lement\x12\x1f\n\x04type\x18\x01 \x02(\x0e\x32\x11.dmScriptDoc.Type\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x62rief\x18\x03 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x02(\t\x12.\n\x0creturnvalues\x18\x05 \x03(\x0b\x32\x18.dmScriptDoc.ReturnValue\x12*\n\nparameters\x18\x06 \x03(\x0b\x32\x16.dmScriptDoc.Parameter\x12\x12\n\x08\x65xamples\x18\x07 \x01(\t:\x00\x12\x12\n\x08replaces\x18\x08 \x01(\t:\x00\x12\x0f\n\x05\x65rror\x18\t \x01(\t:\x00\x12$\n\x07tparams\x18\n \x03(\x0b\x32\x13.dmScriptDoc.Member\x12$\n\x07members\x18\x0b \x03(\x0b\x32\x13.dmScriptDoc.Member\x12\r\n\x05notes\x18\x0c \x03(\t\"v\n\x04Info\x12\x11\n\tnamespace\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x62rief\x18\x03 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x02(\t\x12\x0c\n\x04path\x18\x05 \x02(\t\x12\x0c\n\x04\x66ile\x18\x06 \x02(\t\x12\r\n\x05notes\x18\x07 \x03(\t\"S\n\x08\x44ocument\x12&\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x14.dmScriptDoc.Element\x12\x1f\n\x04info\x18\x02 \x01(\x0b\x32\x11.dmScriptDoc.Info*\x92\x01\n\x04Type\x12\x0c\n\x08\x46UNCTION\x10\x00\x12\x0c\n\x08VARIABLE\x10\x01\x12\x0b\n\x07MESSAGE\x10\x02\x12\r\n\tNAMESPACE\x10\x03\x12\x0c\n\x08PROPERTY\x10\x04\x12\x0b\n\x07PACKAGE\x10\x05\x12\n\n\x06STRUCT\x10\x06\x12\t\n\x05MACRO\x10\x07\x12\x08\n\x04\x45NUM\x10\x08\x12\x0b\n\x07TYPEDEF\x10\t\x12\t\n\x05\x43LASS\x10\nB\'\n\x1a\x63om.dynamo.scriptdoc.protoB\tScriptDoc')
)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='dmScriptDoc.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FUNCTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARIABLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAMESPACE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKAGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRUCT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MACRO', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPEDEF', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASS', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=741,
  serialized_end=887,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
FUNCTION = 0
VARIABLE = 1
MESSAGE = 2
NAMESPACE = 3
PROPERTY = 4
PACKAGE = 5
STRUCT = 6
MACRO = 7
ENUM = 8
TYPEDEF = 9
CLASS = 10



_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='dmScriptDoc.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dmScriptDoc.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doc', full_name='dmScriptDoc.Parameter.doc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='dmScriptDoc.Parameter.types', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=37,
  serialized_end=90,
)


_MEMBER = _descriptor.Descriptor(
  name='Member',
  full_name='dmScriptDoc.Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dmScriptDoc.Member.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doc', full_name='dmScriptDoc.Member.doc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='dmScriptDoc.Member.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=92,
  serialized_end=141,
)


_RETURNVALUE = _descriptor.Descriptor(
  name='ReturnValue',
  full_name='dmScriptDoc.ReturnValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dmScriptDoc.ReturnValue.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doc', full_name='dmScriptDoc.ReturnValue.doc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='dmScriptDoc.ReturnValue.types', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=143,
  serialized_end=198,
)


_ELEMENT = _descriptor.Descriptor(
  name='Element',
  full_name='dmScriptDoc.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dmScriptDoc.Element.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dmScriptDoc.Element.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brief', full_name='dmScriptDoc.Element.brief', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='dmScriptDoc.Element.description', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returnvalues', full_name='dmScriptDoc.Element.returnvalues', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='dmScriptDoc.Element.parameters', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examples', full_name='dmScriptDoc.Element.examples', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replaces', full_name='dmScriptDoc.Element.replaces', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dmScriptDoc.Element.error', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tparams', full_name='dmScriptDoc.Element.tparams', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='members', full_name='dmScriptDoc.Element.members', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='dmScriptDoc.Element.notes', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=201,
  serialized_end=533,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='dmScriptDoc.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='dmScriptDoc.Info.namespace', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dmScriptDoc.Info.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brief', full_name='dmScriptDoc.Info.brief', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='dmScriptDoc.Info.description', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='dmScriptDoc.Info.path', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='dmScriptDoc.Info.file', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='dmScriptDoc.Info.notes', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=535,
  serialized_end=653,
)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='dmScriptDoc.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='dmScriptDoc.Document.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='dmScriptDoc.Document.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=655,
  serialized_end=738,
)

_ELEMENT.fields_by_name['type'].enum_type = _TYPE
_ELEMENT.fields_by_name['returnvalues'].message_type = _RETURNVALUE
_ELEMENT.fields_by_name['parameters'].message_type = _PARAMETER
_ELEMENT.fields_by_name['tparams'].message_type = _MEMBER
_ELEMENT.fields_by_name['members'].message_type = _MEMBER
_DOCUMENT.fields_by_name['elements'].message_type = _ELEMENT
_DOCUMENT.fields_by_name['info'].message_type = _INFO
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Member'] = _MEMBER
DESCRIPTOR.message_types_by_name['ReturnValue'] = _RETURNVALUE
DESCRIPTOR.message_types_by_name['Element'] = _ELEMENT
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'script_doc_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmScriptDoc.Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

Member = _reflection.GeneratedProtocolMessageType('Member', (_message.Message,), dict(
  DESCRIPTOR = _MEMBER,
  __module__ = 'script_doc_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmScriptDoc.Member)
  ))
_sym_db.RegisterMessage(Member)

ReturnValue = _reflection.GeneratedProtocolMessageType('ReturnValue', (_message.Message,), dict(
  DESCRIPTOR = _RETURNVALUE,
  __module__ = 'script_doc_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmScriptDoc.ReturnValue)
  ))
_sym_db.RegisterMessage(ReturnValue)

Element = _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), dict(
  DESCRIPTOR = _ELEMENT,
  __module__ = 'script_doc_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmScriptDoc.Element)
  ))
_sym_db.RegisterMessage(Element)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
  DESCRIPTOR = _INFO,
  __module__ = 'script_doc_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmScriptDoc.Info)
  ))
_sym_db.RegisterMessage(Info)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENT,
  __module__ = 'script_doc_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmScriptDoc.Document)
  ))
_sym_db.RegisterMessage(Document)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
