# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh_ddf.proto

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
  name='mesh_ddf.proto',
  package='dmMeshDDF',
  syntax='proto2',
  serialized_options=_b('\n\030com.dynamo.gamesys.protoB\tMeshProto'),
  serialized_pb=_b('\n\x0emesh_ddf.proto\x12\tdmMeshDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\"\xde\x02\n\x08MeshDesc\x12\x16\n\x08material\x18\x01 \x02(\tB\x04\xa0\xbb\x18\x01\x12\x16\n\x08vertices\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\x12\x16\n\x08textures\x18\x03 \x03(\tB\x04\xa0\xbb\x18\x01\x12N\n\x0eprimitive_type\x18\x04 \x01(\x0e\x32!.dmMeshDDF.MeshDesc.PrimitiveType:\x13PRIMITIVE_TRIANGLES\x12\x17\n\x0fposition_stream\x18\x05 \x01(\t\x12\x15\n\rnormal_stream\x18\x06 \x01(\t\"\x89\x01\n\rPrimitiveType\x12\x1e\n\x0fPRIMITIVE_LINES\x10\x01\x1a\t\xc2\xc1\x18\x05Lines\x12&\n\x13PRIMITIVE_TRIANGLES\x10\x04\x1a\r\xc2\xc1\x18\tTriangles\x12\x30\n\x18PRIMITIVE_TRIANGLE_STRIP\x10\x05\x1a\x12\xc2\xc1\x18\x0eTriangle StripB%\n\x18\x63om.dynamo.gamesys.protoB\tMeshProto')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,])



_MESHDESC_PRIMITIVETYPE = _descriptor.EnumDescriptor(
  name='PrimitiveType',
  full_name='dmMeshDDF.MeshDesc.PrimitiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIMITIVE_LINES', index=0, number=1,
      serialized_options=_b('\302\301\030\005Lines'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIMITIVE_TRIANGLES', index=1, number=4,
      serialized_options=_b('\302\301\030\tTriangles'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIMITIVE_TRIANGLE_STRIP', index=2, number=5,
      serialized_options=_b('\302\301\030\016Triangle Strip'),
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=281,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_MESHDESC_PRIMITIVETYPE)


_MESHDESC = _descriptor.Descriptor(
  name='MeshDesc',
  full_name='dmMeshDDF.MeshDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='material', full_name='dmMeshDDF.MeshDesc.material', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='dmMeshDDF.MeshDesc.vertices', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='textures', full_name='dmMeshDDF.MeshDesc.textures', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primitive_type', full_name='dmMeshDDF.MeshDesc.primitive_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_stream', full_name='dmMeshDDF.MeshDesc.position_stream', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normal_stream', full_name='dmMeshDDF.MeshDesc.normal_stream', index=5,
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
    _MESHDESC_PRIMITIVETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=418,
)

_MESHDESC.fields_by_name['primitive_type'].enum_type = _MESHDESC_PRIMITIVETYPE
_MESHDESC_PRIMITIVETYPE.containing_type = _MESHDESC
DESCRIPTOR.message_types_by_name['MeshDesc'] = _MESHDESC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeshDesc = _reflection.GeneratedProtocolMessageType('MeshDesc', (_message.Message,), dict(
  DESCRIPTOR = _MESHDESC,
  __module__ = 'mesh_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmMeshDDF.MeshDesc)
  ))
_sym_db.RegisterMessage(MeshDesc)


DESCRIPTOR._options = None
_MESHDESC_PRIMITIVETYPE.values_by_name["PRIMITIVE_LINES"]._options = None
_MESHDESC_PRIMITIVETYPE.values_by_name["PRIMITIVE_TRIANGLES"]._options = None
_MESHDESC_PRIMITIVETYPE.values_by_name["PRIMITIVE_TRIANGLE_STRIP"]._options = None
_MESHDESC.fields_by_name['material']._options = None
_MESHDESC.fields_by_name['vertices']._options = None
_MESHDESC.fields_by_name['textures']._options = None
# @@protoc_insertion_point(module_scope)
