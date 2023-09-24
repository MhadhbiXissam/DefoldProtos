# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rig_ddf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ddf_extensions_pb2 as ddf__extensions__pb2
import ddf_math_pb2 as ddf__math__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rig_ddf.proto',
  package='dmRigDDF',
  syntax='proto2',
  serialized_options=_b('\n\024com.dynamo.rig.protoB\003Rig'),
  serialized_pb=_b('\n\rrig_ddf.proto\x12\x08\x64mRigDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\"\xcd\x01\n\x04\x42one\x12\x0e\n\x06parent\x18\x01 \x02(\r\x12\n\n\x02id\x18\x02 \x02(\x04\x12\x0c\n\x04name\x18\x03 \x02(\t\x12&\n\x05local\x18\x04 \x02(\x0b\x32\x11.dmMath.TransformB\x04\xa0\xb5\x18\x01\x12&\n\x05world\x18\x05 \x02(\x0b\x32\x11.dmMath.TransformB\x04\xa0\xb5\x18\x01\x12\x32\n\x11inverse_bind_pose\x18\x06 \x02(\x0b\x32\x11.dmMath.TransformB\x04\xa0\xb5\x18\x01\x12\x11\n\x06length\x18\x07 \x01(\x02:\x01\x30:\x04\x98\xb5\x18\x01\"g\n\x02IK\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0e\n\x06parent\x18\x02 \x02(\r\x12\r\n\x05\x63hild\x18\x03 \x02(\r\x12\x0e\n\x06target\x18\x04 \x02(\r\x12\x16\n\x08positive\x18\x05 \x01(\x08:\x04true\x12\x0e\n\x03mix\x18\x06 \x01(\x02:\x01\x31\"D\n\x08Skeleton\x12\x1d\n\x05\x62ones\x18\x01 \x03(\x0b\x32\x0e.dmRigDDF.Bone\x12\x19\n\x03iks\x18\x02 \x03(\x0b\x32\x0c.dmRigDDF.IK\"V\n\x0e\x41nimationTrack\x12\x0f\n\x07\x62one_id\x18\x01 \x02(\x04\x12\x11\n\tpositions\x18\x02 \x03(\x02\x12\x11\n\trotations\x18\x03 \x03(\x02\x12\r\n\x05scale\x18\x04 \x03(\x02\"N\n\x08\x45ventKey\x12\t\n\x01t\x18\x01 \x02(\x02\x12\x12\n\x07integer\x18\x02 \x01(\x05:\x01\x30\x12\x10\n\x05\x66loat\x18\x03 \x01(\x02:\x01\x30\x12\x11\n\x06string\x18\x04 \x01(\x04:\x01\x30\"@\n\nEventTrack\x12\x10\n\x08\x65vent_id\x18\x01 \x02(\x04\x12 \n\x04keys\x18\x02 \x03(\x0b\x32\x12.dmRigDDF.EventKey\"\x97\x01\n\x0cRigAnimation\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x10\n\x08\x64uration\x18\x02 \x02(\x02\x12\x13\n\x0bsample_rate\x18\x03 \x02(\x02\x12(\n\x06tracks\x18\x04 \x03(\x0b\x32\x18.dmRigDDF.AnimationTrack\x12*\n\x0c\x65vent_tracks\x18\x05 \x03(\x0b\x32\x14.dmRigDDF.EventTrack\":\n\x0c\x41nimationSet\x12*\n\nanimations\x18\x01 \x03(\x0b\x32\x16.dmRigDDF.RigAnimation\"0\n\x15\x41nimationInstanceDesc\x12\x17\n\tanimation\x18\x01 \x02(\tB\x04\xa0\xbb\x18\x01\"Y\n\x10\x41nimationSetDesc\x12\x33\n\nanimations\x18\x01 \x03(\x0b\x32\x1f.dmRigDDF.AnimationInstanceDesc\x12\x10\n\x08skeleton\x18\x02 \x01(\t\"\x81\x03\n\x04Mesh\x12!\n\x08\x61\x61\x62\x62_min\x18\x01 \x02(\x0b\x32\x0f.dmMath.Vector3\x12!\n\x08\x61\x61\x62\x62_max\x18\x02 \x02(\x0b\x32\x0f.dmMath.Vector3\x12\x11\n\tpositions\x18\x03 \x03(\x02\x12\x0f\n\x07normals\x18\x04 \x03(\x02\x12\x10\n\x08tangents\x18\x05 \x03(\x02\x12\x0e\n\x06\x63olors\x18\x06 \x03(\x02\x12\x11\n\ttexcoord0\x18\x07 \x03(\x02\x12 \n\x18num_texcoord0_components\x18\x08 \x01(\r\x12\x11\n\ttexcoord1\x18\t \x03(\x02\x12 \n\x18num_texcoord1_components\x18\n \x01(\r\x12\x0f\n\x07indices\x18\x0b \x01(\x0c\x12\x33\n\x0eindices_format\x18\x0c \x01(\x0e\x32\x1b.dmRigDDF.IndexBufferFormat\x12\x0f\n\x07weights\x18\r \x03(\x02\x12\x14\n\x0c\x62one_indices\x18\x0e \x03(\r\x12\x16\n\x0ematerial_index\x18\x0f \x01(\r\"a\n\x05Model\x12&\n\x05local\x18\x01 \x02(\x0b\x32\x11.dmMath.TransformB\x04\xa0\xb5\x18\x01\x12\n\n\x02id\x18\x02 \x02(\x04\x12\x1e\n\x06meshes\x18\x03 \x03(\x0b\x32\x0e.dmRigDDF.Mesh:\x04\x98\xb5\x18\x01\"h\n\x07MeshSet\x12\x1f\n\x06models\x18\x01 \x03(\x0b\x32\x0f.dmRigDDF.Model\x12\x11\n\tmaterials\x18\x02 \x03(\t\x12\x11\n\tbone_list\x18\x03 \x03(\x04\x12\x16\n\x0emax_bone_count\x18\x04 \x01(\r\"r\n\x08RigScene\x12\x16\n\x08skeleton\x18\x01 \x01(\tB\x04\xa0\xbb\x18\x01\x12\x1b\n\ranimation_set\x18\x02 \x01(\tB\x04\xa0\xbb\x18\x01\x12\x16\n\x08mesh_set\x18\x03 \x02(\tB\x04\xa0\xbb\x18\x01\x12\x19\n\x0btexture_set\x18\x04 \x01(\tB\x04\xa0\xbb\x18\x01*I\n\x11IndexBufferFormat\x12\x19\n\x15INDEXBUFFER_FORMAT_16\x10\x00\x12\x19\n\x15INDEXBUFFER_FORMAT_32\x10\x01\x42\x1b\n\x14\x63om.dynamo.rig.protoB\x03Rig')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,])

_INDEXBUFFERFORMAT = _descriptor.EnumDescriptor(
  name='IndexBufferFormat',
  full_name='dmRigDDF.IndexBufferFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INDEXBUFFER_FORMAT_16', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXBUFFER_FORMAT_32', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1746,
  serialized_end=1819,
)
_sym_db.RegisterEnumDescriptor(_INDEXBUFFERFORMAT)

IndexBufferFormat = enum_type_wrapper.EnumTypeWrapper(_INDEXBUFFERFORMAT)
INDEXBUFFER_FORMAT_16 = 0
INDEXBUFFER_FORMAT_32 = 1



_BONE = _descriptor.Descriptor(
  name='Bone',
  full_name='dmRigDDF.Bone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='dmRigDDF.Bone.parent', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='dmRigDDF.Bone.id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dmRigDDF.Bone.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local', full_name='dmRigDDF.Bone.local', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='world', full_name='dmRigDDF.Bone.world', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inverse_bind_pose', full_name='dmRigDDF.Bone.inverse_bind_pose', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='dmRigDDF.Bone.length', index=6,
      number=7, type=2, cpp_type=6, label=1,
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
  serialized_options=_b('\230\265\030\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=271,
)


_IK = _descriptor.Descriptor(
  name='IK',
  full_name='dmRigDDF.IK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dmRigDDF.IK.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='dmRigDDF.IK.parent', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='dmRigDDF.IK.child', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='dmRigDDF.IK.target', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positive', full_name='dmRigDDF.IK.positive', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mix', full_name='dmRigDDF.IK.mix', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=376,
)


_SKELETON = _descriptor.Descriptor(
  name='Skeleton',
  full_name='dmRigDDF.Skeleton',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bones', full_name='dmRigDDF.Skeleton.bones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iks', full_name='dmRigDDF.Skeleton.iks', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=378,
  serialized_end=446,
)


_ANIMATIONTRACK = _descriptor.Descriptor(
  name='AnimationTrack',
  full_name='dmRigDDF.AnimationTrack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bone_id', full_name='dmRigDDF.AnimationTrack.bone_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions', full_name='dmRigDDF.AnimationTrack.positions', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotations', full_name='dmRigDDF.AnimationTrack.rotations', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='dmRigDDF.AnimationTrack.scale', index=3,
      number=4, type=2, cpp_type=6, label=3,
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
  serialized_start=448,
  serialized_end=534,
)


_EVENTKEY = _descriptor.Descriptor(
  name='EventKey',
  full_name='dmRigDDF.EventKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='t', full_name='dmRigDDF.EventKey.t', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integer', full_name='dmRigDDF.EventKey.integer', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float', full_name='dmRigDDF.EventKey.float', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='dmRigDDF.EventKey.string', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=536,
  serialized_end=614,
)


_EVENTTRACK = _descriptor.Descriptor(
  name='EventTrack',
  full_name='dmRigDDF.EventTrack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='dmRigDDF.EventTrack.event_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='dmRigDDF.EventTrack.keys', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=616,
  serialized_end=680,
)


_RIGANIMATION = _descriptor.Descriptor(
  name='RigAnimation',
  full_name='dmRigDDF.RigAnimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dmRigDDF.RigAnimation.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='dmRigDDF.RigAnimation.duration', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='dmRigDDF.RigAnimation.sample_rate', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracks', full_name='dmRigDDF.RigAnimation.tracks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_tracks', full_name='dmRigDDF.RigAnimation.event_tracks', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=683,
  serialized_end=834,
)


_ANIMATIONSET = _descriptor.Descriptor(
  name='AnimationSet',
  full_name='dmRigDDF.AnimationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='animations', full_name='dmRigDDF.AnimationSet.animations', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=836,
  serialized_end=894,
)


_ANIMATIONINSTANCEDESC = _descriptor.Descriptor(
  name='AnimationInstanceDesc',
  full_name='dmRigDDF.AnimationInstanceDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='animation', full_name='dmRigDDF.AnimationInstanceDesc.animation', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
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
  serialized_start=896,
  serialized_end=944,
)


_ANIMATIONSETDESC = _descriptor.Descriptor(
  name='AnimationSetDesc',
  full_name='dmRigDDF.AnimationSetDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='animations', full_name='dmRigDDF.AnimationSetDesc.animations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skeleton', full_name='dmRigDDF.AnimationSetDesc.skeleton', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=946,
  serialized_end=1035,
)


_MESH = _descriptor.Descriptor(
  name='Mesh',
  full_name='dmRigDDF.Mesh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aabb_min', full_name='dmRigDDF.Mesh.aabb_min', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aabb_max', full_name='dmRigDDF.Mesh.aabb_max', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions', full_name='dmRigDDF.Mesh.positions', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normals', full_name='dmRigDDF.Mesh.normals', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tangents', full_name='dmRigDDF.Mesh.tangents', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colors', full_name='dmRigDDF.Mesh.colors', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='texcoord0', full_name='dmRigDDF.Mesh.texcoord0', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_texcoord0_components', full_name='dmRigDDF.Mesh.num_texcoord0_components', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='texcoord1', full_name='dmRigDDF.Mesh.texcoord1', index=8,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_texcoord1_components', full_name='dmRigDDF.Mesh.num_texcoord1_components', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indices', full_name='dmRigDDF.Mesh.indices', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indices_format', full_name='dmRigDDF.Mesh.indices_format', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='dmRigDDF.Mesh.weights', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bone_indices', full_name='dmRigDDF.Mesh.bone_indices', index=13,
      number=14, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material_index', full_name='dmRigDDF.Mesh.material_index', index=14,
      number=15, type=13, cpp_type=3, label=1,
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
  serialized_start=1038,
  serialized_end=1423,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='dmRigDDF.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local', full_name='dmRigDDF.Model.local', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='dmRigDDF.Model.id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meshes', full_name='dmRigDDF.Model.meshes', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_options=_b('\230\265\030\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1425,
  serialized_end=1522,
)


_MESHSET = _descriptor.Descriptor(
  name='MeshSet',
  full_name='dmRigDDF.MeshSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='dmRigDDF.MeshSet.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='materials', full_name='dmRigDDF.MeshSet.materials', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bone_list', full_name='dmRigDDF.MeshSet.bone_list', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bone_count', full_name='dmRigDDF.MeshSet.max_bone_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=1524,
  serialized_end=1628,
)


_RIGSCENE = _descriptor.Descriptor(
  name='RigScene',
  full_name='dmRigDDF.RigScene',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skeleton', full_name='dmRigDDF.RigScene.skeleton', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='animation_set', full_name='dmRigDDF.RigScene.animation_set', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mesh_set', full_name='dmRigDDF.RigScene.mesh_set', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='texture_set', full_name='dmRigDDF.RigScene.texture_set', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
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
  serialized_start=1630,
  serialized_end=1744,
)

_BONE.fields_by_name['local'].message_type = ddf__math__pb2._TRANSFORM
_BONE.fields_by_name['world'].message_type = ddf__math__pb2._TRANSFORM
_BONE.fields_by_name['inverse_bind_pose'].message_type = ddf__math__pb2._TRANSFORM
_SKELETON.fields_by_name['bones'].message_type = _BONE
_SKELETON.fields_by_name['iks'].message_type = _IK
_EVENTTRACK.fields_by_name['keys'].message_type = _EVENTKEY
_RIGANIMATION.fields_by_name['tracks'].message_type = _ANIMATIONTRACK
_RIGANIMATION.fields_by_name['event_tracks'].message_type = _EVENTTRACK
_ANIMATIONSET.fields_by_name['animations'].message_type = _RIGANIMATION
_ANIMATIONSETDESC.fields_by_name['animations'].message_type = _ANIMATIONINSTANCEDESC
_MESH.fields_by_name['aabb_min'].message_type = ddf__math__pb2._VECTOR3
_MESH.fields_by_name['aabb_max'].message_type = ddf__math__pb2._VECTOR3
_MESH.fields_by_name['indices_format'].enum_type = _INDEXBUFFERFORMAT
_MODEL.fields_by_name['local'].message_type = ddf__math__pb2._TRANSFORM
_MODEL.fields_by_name['meshes'].message_type = _MESH
_MESHSET.fields_by_name['models'].message_type = _MODEL
DESCRIPTOR.message_types_by_name['Bone'] = _BONE
DESCRIPTOR.message_types_by_name['IK'] = _IK
DESCRIPTOR.message_types_by_name['Skeleton'] = _SKELETON
DESCRIPTOR.message_types_by_name['AnimationTrack'] = _ANIMATIONTRACK
DESCRIPTOR.message_types_by_name['EventKey'] = _EVENTKEY
DESCRIPTOR.message_types_by_name['EventTrack'] = _EVENTTRACK
DESCRIPTOR.message_types_by_name['RigAnimation'] = _RIGANIMATION
DESCRIPTOR.message_types_by_name['AnimationSet'] = _ANIMATIONSET
DESCRIPTOR.message_types_by_name['AnimationInstanceDesc'] = _ANIMATIONINSTANCEDESC
DESCRIPTOR.message_types_by_name['AnimationSetDesc'] = _ANIMATIONSETDESC
DESCRIPTOR.message_types_by_name['Mesh'] = _MESH
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['MeshSet'] = _MESHSET
DESCRIPTOR.message_types_by_name['RigScene'] = _RIGSCENE
DESCRIPTOR.enum_types_by_name['IndexBufferFormat'] = _INDEXBUFFERFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bone = _reflection.GeneratedProtocolMessageType('Bone', (_message.Message,), dict(
  DESCRIPTOR = _BONE,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.Bone)
  ))
_sym_db.RegisterMessage(Bone)

IK = _reflection.GeneratedProtocolMessageType('IK', (_message.Message,), dict(
  DESCRIPTOR = _IK,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.IK)
  ))
_sym_db.RegisterMessage(IK)

Skeleton = _reflection.GeneratedProtocolMessageType('Skeleton', (_message.Message,), dict(
  DESCRIPTOR = _SKELETON,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.Skeleton)
  ))
_sym_db.RegisterMessage(Skeleton)

AnimationTrack = _reflection.GeneratedProtocolMessageType('AnimationTrack', (_message.Message,), dict(
  DESCRIPTOR = _ANIMATIONTRACK,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.AnimationTrack)
  ))
_sym_db.RegisterMessage(AnimationTrack)

EventKey = _reflection.GeneratedProtocolMessageType('EventKey', (_message.Message,), dict(
  DESCRIPTOR = _EVENTKEY,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.EventKey)
  ))
_sym_db.RegisterMessage(EventKey)

EventTrack = _reflection.GeneratedProtocolMessageType('EventTrack', (_message.Message,), dict(
  DESCRIPTOR = _EVENTTRACK,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.EventTrack)
  ))
_sym_db.RegisterMessage(EventTrack)

RigAnimation = _reflection.GeneratedProtocolMessageType('RigAnimation', (_message.Message,), dict(
  DESCRIPTOR = _RIGANIMATION,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.RigAnimation)
  ))
_sym_db.RegisterMessage(RigAnimation)

AnimationSet = _reflection.GeneratedProtocolMessageType('AnimationSet', (_message.Message,), dict(
  DESCRIPTOR = _ANIMATIONSET,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.AnimationSet)
  ))
_sym_db.RegisterMessage(AnimationSet)

AnimationInstanceDesc = _reflection.GeneratedProtocolMessageType('AnimationInstanceDesc', (_message.Message,), dict(
  DESCRIPTOR = _ANIMATIONINSTANCEDESC,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.AnimationInstanceDesc)
  ))
_sym_db.RegisterMessage(AnimationInstanceDesc)

AnimationSetDesc = _reflection.GeneratedProtocolMessageType('AnimationSetDesc', (_message.Message,), dict(
  DESCRIPTOR = _ANIMATIONSETDESC,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.AnimationSetDesc)
  ))
_sym_db.RegisterMessage(AnimationSetDesc)

Mesh = _reflection.GeneratedProtocolMessageType('Mesh', (_message.Message,), dict(
  DESCRIPTOR = _MESH,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.Mesh)
  ))
_sym_db.RegisterMessage(Mesh)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), dict(
  DESCRIPTOR = _MODEL,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.Model)
  ))
_sym_db.RegisterMessage(Model)

MeshSet = _reflection.GeneratedProtocolMessageType('MeshSet', (_message.Message,), dict(
  DESCRIPTOR = _MESHSET,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.MeshSet)
  ))
_sym_db.RegisterMessage(MeshSet)

RigScene = _reflection.GeneratedProtocolMessageType('RigScene', (_message.Message,), dict(
  DESCRIPTOR = _RIGSCENE,
  __module__ = 'rig_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRigDDF.RigScene)
  ))
_sym_db.RegisterMessage(RigScene)


DESCRIPTOR._options = None
_BONE.fields_by_name['local']._options = None
_BONE.fields_by_name['world']._options = None
_BONE.fields_by_name['inverse_bind_pose']._options = None
_BONE._options = None
_ANIMATIONINSTANCEDESC.fields_by_name['animation']._options = None
_MODEL.fields_by_name['local']._options = None
_MODEL._options = None
_RIGSCENE.fields_by_name['skeleton']._options = None
_RIGSCENE.fields_by_name['animation_set']._options = None
_RIGSCENE.fields_by_name['mesh_set']._options = None
_RIGSCENE.fields_by_name['texture_set']._options = None
# @@protoc_insertion_point(module_scope)