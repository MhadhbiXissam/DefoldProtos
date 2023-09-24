# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: atlas_ddf.proto

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
import tile_ddf_pb2 as tile__ddf__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='atlas_ddf.proto',
  package='dmGameSystemDDF',
  syntax='proto2',
  serialized_options=_b('\n\030com.dynamo.gamesys.protoB\nAtlasProto'),
  serialized_pb=_b('\n\x0f\x61tlas_ddf.proto\x12\x0f\x64mGameSystemDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\x1a\x0etile_ddf.proto\"v\n\nAtlasImage\x12\x13\n\x05image\x18\x01 \x02(\tB\x04\xa0\xbb\x18\x01\x12S\n\x10sprite_trim_mode\x18\x02 \x01(\x0e\x32#.dmGameSystemDDF.SpriteTrimmingMode:\x14SPRITE_TRIM_MODE_OFF\"\xd4\x01\n\x0e\x41tlasAnimation\x12\n\n\x02id\x18\x01 \x02(\t\x12+\n\x06images\x18\x02 \x03(\x0b\x32\x1b.dmGameSystemDDF.AtlasImage\x12\x42\n\x08playback\x18\x03 \x01(\x0e\x32\x19.dmGameSystemDDF.Playback:\x15PLAYBACK_ONCE_FORWARD\x12\x0f\n\x03\x66ps\x18\x04 \x01(\r:\x02\x33\x30\x12\x1a\n\x0f\x66lip_horizontal\x18\x05 \x01(\r:\x01\x30\x12\x18\n\rflip_vertical\x18\x06 \x01(\r:\x01\x30\"\xe9\x01\n\x05\x41tlas\x12+\n\x06images\x18\x01 \x03(\x0b\x32\x1b.dmGameSystemDDF.AtlasImage\x12\x33\n\nanimations\x18\x02 \x03(\x0b\x32\x1f.dmGameSystemDDF.AtlasAnimation\x12\x11\n\x06margin\x18\x03 \x01(\r:\x01\x30\x12\x1a\n\x0f\x65xtrude_borders\x18\x04 \x01(\r:\x01\x30\x12\x18\n\rinner_padding\x18\x05 \x01(\r:\x01\x30\x12\x19\n\x0emax_page_width\x18\x06 \x01(\r:\x01\x30\x12\x1a\n\x0fmax_page_height\x18\x07 \x01(\r:\x01\x30\x42&\n\x18\x63om.dynamo.gamesys.protoB\nAtlasProto')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,tile__ddf__pb2.DESCRIPTOR,])




_ATLASIMAGE = _descriptor.Descriptor(
  name='AtlasImage',
  full_name='dmGameSystemDDF.AtlasImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='dmGameSystemDDF.AtlasImage.image', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sprite_trim_mode', full_name='dmGameSystemDDF.AtlasImage.sprite_trim_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=90,
  serialized_end=208,
)


_ATLASANIMATION = _descriptor.Descriptor(
  name='AtlasAnimation',
  full_name='dmGameSystemDDF.AtlasAnimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dmGameSystemDDF.AtlasAnimation.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='dmGameSystemDDF.AtlasAnimation.images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playback', full_name='dmGameSystemDDF.AtlasAnimation.playback', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fps', full_name='dmGameSystemDDF.AtlasAnimation.fps', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=30,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flip_horizontal', full_name='dmGameSystemDDF.AtlasAnimation.flip_horizontal', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flip_vertical', full_name='dmGameSystemDDF.AtlasAnimation.flip_vertical', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=211,
  serialized_end=423,
)


_ATLAS = _descriptor.Descriptor(
  name='Atlas',
  full_name='dmGameSystemDDF.Atlas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='images', full_name='dmGameSystemDDF.Atlas.images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='animations', full_name='dmGameSystemDDF.Atlas.animations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='margin', full_name='dmGameSystemDDF.Atlas.margin', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extrude_borders', full_name='dmGameSystemDDF.Atlas.extrude_borders', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inner_padding', full_name='dmGameSystemDDF.Atlas.inner_padding', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_page_width', full_name='dmGameSystemDDF.Atlas.max_page_width', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_page_height', full_name='dmGameSystemDDF.Atlas.max_page_height', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=426,
  serialized_end=659,
)

_ATLASIMAGE.fields_by_name['sprite_trim_mode'].enum_type = tile__ddf__pb2._SPRITETRIMMINGMODE
_ATLASANIMATION.fields_by_name['images'].message_type = _ATLASIMAGE
_ATLASANIMATION.fields_by_name['playback'].enum_type = tile__ddf__pb2._PLAYBACK
_ATLAS.fields_by_name['images'].message_type = _ATLASIMAGE
_ATLAS.fields_by_name['animations'].message_type = _ATLASANIMATION
DESCRIPTOR.message_types_by_name['AtlasImage'] = _ATLASIMAGE
DESCRIPTOR.message_types_by_name['AtlasAnimation'] = _ATLASANIMATION
DESCRIPTOR.message_types_by_name['Atlas'] = _ATLAS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AtlasImage = _reflection.GeneratedProtocolMessageType('AtlasImage', (_message.Message,), dict(
  DESCRIPTOR = _ATLASIMAGE,
  __module__ = 'atlas_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.AtlasImage)
  ))
_sym_db.RegisterMessage(AtlasImage)

AtlasAnimation = _reflection.GeneratedProtocolMessageType('AtlasAnimation', (_message.Message,), dict(
  DESCRIPTOR = _ATLASANIMATION,
  __module__ = 'atlas_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.AtlasAnimation)
  ))
_sym_db.RegisterMessage(AtlasAnimation)

Atlas = _reflection.GeneratedProtocolMessageType('Atlas', (_message.Message,), dict(
  DESCRIPTOR = _ATLAS,
  __module__ = 'atlas_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.Atlas)
  ))
_sym_db.RegisterMessage(Atlas)


DESCRIPTOR._options = None
_ATLASIMAGE.fields_by_name['image']._options = None
# @@protoc_insertion_point(module_scope)