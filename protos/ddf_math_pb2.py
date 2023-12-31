# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ddf_math.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ddf_extensions_pb2 as ddf__extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ddf_math.proto',
  package='dmMath',
  syntax='proto2',
  serialized_options=_b('\n\020com.dynamo.protoB\007DdfMath\222\265\030)dmsdk/dlib/vmath.h dmsdk/dlib/transform.h'),
  serialized_pb=_b('\n\x0e\x64\x64\x66_math.proto\x12\x06\x64mMath\x1a\x14\x64\x64\x66_extensions.proto\"U\n\x06Point3\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x02:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x02:\x01\x30\x12\x0c\n\x01\x64\x18\x04 \x01(\x02:\x01\x30:\x13\x82\xb5\x18\x0f\x64mVMath::Point3\"W\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x02:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x02:\x01\x30\x12\x0c\n\x01\x64\x18\x04 \x01(\x02:\x01\x30:\x14\x82\xb5\x18\x10\x64mVMath::Vector3\"W\n\x07Vector4\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x02:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x02:\x01\x30\x12\x0c\n\x01w\x18\x04 \x01(\x02:\x01\x30:\x14\x82\xb5\x18\x10\x64mVMath::Vector4\"Q\n\x04Quat\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x02:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x02:\x01\x30\x12\x0c\n\x01w\x18\x04 \x01(\x02:\x01\x31:\x11\x82\xb5\x18\rdmVMath::Quat\"\x8d\x01\n\tTransform\x12\x1e\n\x08rotation\x18\x01 \x01(\x0b\x32\x0c.dmMath.Quat\x12$\n\x0btranslation\x18\x02 \x01(\x0b\x32\x0f.dmMath.Vector3\x12\x1e\n\x05scale\x18\x03 \x01(\x0b\x32\x0f.dmMath.Vector3:\x1a\x82\xb5\x18\x16\x64mTransform::Transform\"\x9f\x02\n\x07Matrix4\x12\x0e\n\x03m00\x18\x01 \x01(\x02:\x01\x31\x12\x0e\n\x03m01\x18\x02 \x01(\x02:\x01\x30\x12\x0e\n\x03m02\x18\x03 \x01(\x02:\x01\x30\x12\x0e\n\x03m03\x18\x04 \x01(\x02:\x01\x30\x12\x0e\n\x03m10\x18\x05 \x01(\x02:\x01\x30\x12\x0e\n\x03m11\x18\x06 \x01(\x02:\x01\x31\x12\x0e\n\x03m12\x18\x07 \x01(\x02:\x01\x30\x12\x0e\n\x03m13\x18\x08 \x01(\x02:\x01\x30\x12\x0e\n\x03m20\x18\t \x01(\x02:\x01\x30\x12\x0e\n\x03m21\x18\n \x01(\x02:\x01\x30\x12\x0e\n\x03m22\x18\x0b \x01(\x02:\x01\x31\x12\x0e\n\x03m23\x18\x0c \x01(\x02:\x01\x30\x12\x0e\n\x03m30\x18\r \x01(\x02:\x01\x30\x12\x0e\n\x03m31\x18\x0e \x01(\x02:\x01\x30\x12\x0e\n\x03m32\x18\x0f \x01(\x02:\x01\x30\x12\x0e\n\x03m33\x18\x10 \x01(\x02:\x01\x31:\x14\x82\xb5\x18\x10\x64mVMath::Matrix4BH\n\x10\x63om.dynamo.protoB\x07\x44\x64\x66Math\x92\xb5\x18)dmsdk/dlib/vmath.h dmsdk/dlib/transform.h')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,])




_POINT3 = _descriptor.Descriptor(
  name='Point3',
  full_name='dmMath.Point3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dmMath.Point3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dmMath.Point3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='dmMath.Point3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='dmMath.Point3.d', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\202\265\030\017dmVMath::Point3'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=133,
)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='dmMath.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dmMath.Vector3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dmMath.Vector3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='dmMath.Vector3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='dmMath.Vector3.d', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\202\265\030\020dmVMath::Vector3'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=222,
)


_VECTOR4 = _descriptor.Descriptor(
  name='Vector4',
  full_name='dmMath.Vector4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dmMath.Vector4.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dmMath.Vector4.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='dmMath.Vector4.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='dmMath.Vector4.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\202\265\030\020dmVMath::Vector4'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=311,
)


_QUAT = _descriptor.Descriptor(
  name='Quat',
  full_name='dmMath.Quat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='dmMath.Quat.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='dmMath.Quat.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='dmMath.Quat.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='dmMath.Quat.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\202\265\030\rdmVMath::Quat'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=394,
)


_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='dmMath.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation', full_name='dmMath.Transform.rotation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translation', full_name='dmMath.Transform.translation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='dmMath.Transform.scale', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('\202\265\030\026dmTransform::Transform'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=538,
)


_MATRIX4 = _descriptor.Descriptor(
  name='Matrix4',
  full_name='dmMath.Matrix4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m00', full_name='dmMath.Matrix4.m00', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m01', full_name='dmMath.Matrix4.m01', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m02', full_name='dmMath.Matrix4.m02', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m03', full_name='dmMath.Matrix4.m03', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m10', full_name='dmMath.Matrix4.m10', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m11', full_name='dmMath.Matrix4.m11', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m12', full_name='dmMath.Matrix4.m12', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m13', full_name='dmMath.Matrix4.m13', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m20', full_name='dmMath.Matrix4.m20', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m21', full_name='dmMath.Matrix4.m21', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m22', full_name='dmMath.Matrix4.m22', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m23', full_name='dmMath.Matrix4.m23', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m30', full_name='dmMath.Matrix4.m30', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m31', full_name='dmMath.Matrix4.m31', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m32', full_name='dmMath.Matrix4.m32', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m33', full_name='dmMath.Matrix4.m33', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\202\265\030\020dmVMath::Matrix4'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=828,
)

_TRANSFORM.fields_by_name['rotation'].message_type = _QUAT
_TRANSFORM.fields_by_name['translation'].message_type = _VECTOR3
_TRANSFORM.fields_by_name['scale'].message_type = _VECTOR3
DESCRIPTOR.message_types_by_name['Point3'] = _POINT3
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Vector4'] = _VECTOR4
DESCRIPTOR.message_types_by_name['Quat'] = _QUAT
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['Matrix4'] = _MATRIX4
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point3 = _reflection.GeneratedProtocolMessageType('Point3', (_message.Message,), dict(
  DESCRIPTOR = _POINT3,
  __module__ = 'ddf_math_pb2'
  # @@protoc_insertion_point(class_scope:dmMath.Point3)
  ))
_sym_db.RegisterMessage(Point3)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'ddf_math_pb2'
  # @@protoc_insertion_point(class_scope:dmMath.Vector3)
  ))
_sym_db.RegisterMessage(Vector3)

Vector4 = _reflection.GeneratedProtocolMessageType('Vector4', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR4,
  __module__ = 'ddf_math_pb2'
  # @@protoc_insertion_point(class_scope:dmMath.Vector4)
  ))
_sym_db.RegisterMessage(Vector4)

Quat = _reflection.GeneratedProtocolMessageType('Quat', (_message.Message,), dict(
  DESCRIPTOR = _QUAT,
  __module__ = 'ddf_math_pb2'
  # @@protoc_insertion_point(class_scope:dmMath.Quat)
  ))
_sym_db.RegisterMessage(Quat)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORM,
  __module__ = 'ddf_math_pb2'
  # @@protoc_insertion_point(class_scope:dmMath.Transform)
  ))
_sym_db.RegisterMessage(Transform)

Matrix4 = _reflection.GeneratedProtocolMessageType('Matrix4', (_message.Message,), dict(
  DESCRIPTOR = _MATRIX4,
  __module__ = 'ddf_math_pb2'
  # @@protoc_insertion_point(class_scope:dmMath.Matrix4)
  ))
_sym_db.RegisterMessage(Matrix4)


DESCRIPTOR._options = None
_POINT3._options = None
_VECTOR3._options = None
_VECTOR4._options = None
_QUAT._options = None
_TRANSFORM._options = None
_MATRIX4._options = None
# @@protoc_insertion_point(module_scope)
