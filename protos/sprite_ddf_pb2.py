# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sprite_ddf.proto

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
import graphics_ddf_pb2 as graphics__ddf__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sprite_ddf.proto',
  package='dmGameSystemDDF',
  syntax='proto2',
  serialized_options=_b('\n\030com.dynamo.gamesys.protoB\006Sprite'),
  serialized_pb=_b('\n\x10sprite_ddf.proto\x12\x0f\x64mGameSystemDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\x1a\x12graphics_ddf.proto\"\xc4\x05\n\nSpriteDesc\x12\x16\n\x08tile_set\x18\x01 \x02(\tB\x04\xa0\xbb\x18\x01\x12\x19\n\x11\x64\x65\x66\x61ult_animation\x18\x02 \x02(\t\x12;\n\x08material\x18\x03 \x01(\t:#/builtins/materials/sprite.materialB\x04\xa0\xbb\x18\x01\x12K\n\nblend_mode\x18\x04 \x01(\x0e\x32%.dmGameSystemDDF.SpriteDesc.BlendMode:\x10\x42LEND_MODE_ALPHA\x12\x1f\n\x06slice9\x18\x05 \x01(\x0b\x32\x0f.dmMath.Vector4\x12\x1d\n\x04size\x18\x06 \x01(\x0b\x32\x0f.dmMath.Vector4\x12G\n\tsize_mode\x18\x07 \x01(\x0e\x32$.dmGameSystemDDF.SpriteDesc.SizeMode:\x0eSIZE_MODE_AUTO\x12\x11\n\x06offset\x18\x08 \x01(\x02:\x01\x30\x12\x18\n\rplayback_rate\x18\t \x01(\x02:\x01\x31\x12/\n\nattributes\x18\n \x03(\x0b\x32\x1b.dmGraphics.VertexAttribute\"\xc5\x01\n\tBlendMode\x12\x1f\n\x10\x42LEND_MODE_ALPHA\x10\x00\x1a\t\xc2\xc1\x18\x05\x41lpha\x12\x1b\n\x0e\x42LEND_MODE_ADD\x10\x01\x1a\x07\xc2\xc1\x18\x03\x41\x64\x64\x12\x34\n\x14\x42LEND_MODE_ADD_ALPHA\x10\x02\x1a\x1a\xc2\xc1\x18\x16\x41\x64\x64 Alpha (Deprecated)\x12!\n\x0f\x42LEND_MODE_MULT\x10\x03\x1a\x0c\xc2\xc1\x18\x08Multiply\x12!\n\x11\x42LEND_MODE_SCREEN\x10\x04\x1a\n\xc2\xc1\x18\x06Screen\"J\n\x08SizeMode\x12 \n\x10SIZE_MODE_MANUAL\x10\x00\x1a\n\xc2\xc1\x18\x06Manual\x12\x1c\n\x0eSIZE_MODE_AUTO\x10\x01\x1a\x08\xc2\xc1\x18\x04\x41uto\"H\n\rPlayAnimation\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x11\n\x06offset\x18\x02 \x01(\x02:\x01\x30\x12\x18\n\rplayback_rate\x18\x03 \x01(\x02:\x01\x31\"1\n\rAnimationDone\x12\x14\n\x0c\x63urrent_tile\x18\x01 \x02(\r\x12\n\n\x02id\x18\x02 \x02(\x04\"!\n\x11SetFlipHorizontal\x12\x0c\n\x04\x66lip\x18\x01 \x02(\r\"\x1f\n\x0fSetFlipVertical\x12\x0c\n\x04\x66lip\x18\x01 \x02(\rB\"\n\x18\x63om.dynamo.gamesys.protoB\x06Sprite')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,graphics__ddf__pb2.DESCRIPTOR,])



_SPRITEDESC_BLENDMODE = _descriptor.EnumDescriptor(
  name='BlendMode',
  full_name='dmGameSystemDDF.SpriteDesc.BlendMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLEND_MODE_ALPHA', index=0, number=0,
      serialized_options=_b('\302\301\030\005Alpha'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLEND_MODE_ADD', index=1, number=1,
      serialized_options=_b('\302\301\030\003Add'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLEND_MODE_ADD_ALPHA', index=2, number=2,
      serialized_options=_b('\302\301\030\026Add Alpha (Deprecated)'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLEND_MODE_MULT', index=3, number=3,
      serialized_options=_b('\302\301\030\010Multiply'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLEND_MODE_SCREEN', index=4, number=4,
      serialized_options=_b('\302\301\030\006Screen'),
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=531,
  serialized_end=728,
)
_sym_db.RegisterEnumDescriptor(_SPRITEDESC_BLENDMODE)

_SPRITEDESC_SIZEMODE = _descriptor.EnumDescriptor(
  name='SizeMode',
  full_name='dmGameSystemDDF.SpriteDesc.SizeMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIZE_MODE_MANUAL', index=0, number=0,
      serialized_options=_b('\302\301\030\006Manual'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIZE_MODE_AUTO', index=1, number=1,
      serialized_options=_b('\302\301\030\004Auto'),
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=730,
  serialized_end=804,
)
_sym_db.RegisterEnumDescriptor(_SPRITEDESC_SIZEMODE)


_SPRITEDESC = _descriptor.Descriptor(
  name='SpriteDesc',
  full_name='dmGameSystemDDF.SpriteDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tile_set', full_name='dmGameSystemDDF.SpriteDesc.tile_set', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_animation', full_name='dmGameSystemDDF.SpriteDesc.default_animation', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material', full_name='dmGameSystemDDF.SpriteDesc.material', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/builtins/materials/sprite.material").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blend_mode', full_name='dmGameSystemDDF.SpriteDesc.blend_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slice9', full_name='dmGameSystemDDF.SpriteDesc.slice9', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='dmGameSystemDDF.SpriteDesc.size', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size_mode', full_name='dmGameSystemDDF.SpriteDesc.size_mode', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='dmGameSystemDDF.SpriteDesc.offset', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playback_rate', full_name='dmGameSystemDDF.SpriteDesc.playback_rate', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='dmGameSystemDDF.SpriteDesc.attributes', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SPRITEDESC_BLENDMODE,
    _SPRITEDESC_SIZEMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=804,
)


_PLAYANIMATION = _descriptor.Descriptor(
  name='PlayAnimation',
  full_name='dmGameSystemDDF.PlayAnimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dmGameSystemDDF.PlayAnimation.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='dmGameSystemDDF.PlayAnimation.offset', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playback_rate', full_name='dmGameSystemDDF.PlayAnimation.playback_rate', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=806,
  serialized_end=878,
)


_ANIMATIONDONE = _descriptor.Descriptor(
  name='AnimationDone',
  full_name='dmGameSystemDDF.AnimationDone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_tile', full_name='dmGameSystemDDF.AnimationDone.current_tile', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='dmGameSystemDDF.AnimationDone.id', index=1,
      number=2, type=4, cpp_type=4, label=2,
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
  serialized_start=880,
  serialized_end=929,
)


_SETFLIPHORIZONTAL = _descriptor.Descriptor(
  name='SetFlipHorizontal',
  full_name='dmGameSystemDDF.SetFlipHorizontal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flip', full_name='dmGameSystemDDF.SetFlipHorizontal.flip', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=931,
  serialized_end=964,
)


_SETFLIPVERTICAL = _descriptor.Descriptor(
  name='SetFlipVertical',
  full_name='dmGameSystemDDF.SetFlipVertical',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flip', full_name='dmGameSystemDDF.SetFlipVertical.flip', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=966,
  serialized_end=997,
)

_SPRITEDESC.fields_by_name['blend_mode'].enum_type = _SPRITEDESC_BLENDMODE
_SPRITEDESC.fields_by_name['slice9'].message_type = ddf__math__pb2._VECTOR4
_SPRITEDESC.fields_by_name['size'].message_type = ddf__math__pb2._VECTOR4
_SPRITEDESC.fields_by_name['size_mode'].enum_type = _SPRITEDESC_SIZEMODE
_SPRITEDESC.fields_by_name['attributes'].message_type = graphics__ddf__pb2._VERTEXATTRIBUTE
_SPRITEDESC_BLENDMODE.containing_type = _SPRITEDESC
_SPRITEDESC_SIZEMODE.containing_type = _SPRITEDESC
DESCRIPTOR.message_types_by_name['SpriteDesc'] = _SPRITEDESC
DESCRIPTOR.message_types_by_name['PlayAnimation'] = _PLAYANIMATION
DESCRIPTOR.message_types_by_name['AnimationDone'] = _ANIMATIONDONE
DESCRIPTOR.message_types_by_name['SetFlipHorizontal'] = _SETFLIPHORIZONTAL
DESCRIPTOR.message_types_by_name['SetFlipVertical'] = _SETFLIPVERTICAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpriteDesc = _reflection.GeneratedProtocolMessageType('SpriteDesc', (_message.Message,), dict(
  DESCRIPTOR = _SPRITEDESC,
  __module__ = 'sprite_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.SpriteDesc)
  ))
_sym_db.RegisterMessage(SpriteDesc)

PlayAnimation = _reflection.GeneratedProtocolMessageType('PlayAnimation', (_message.Message,), dict(
  DESCRIPTOR = _PLAYANIMATION,
  __module__ = 'sprite_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.PlayAnimation)
  ))
_sym_db.RegisterMessage(PlayAnimation)

AnimationDone = _reflection.GeneratedProtocolMessageType('AnimationDone', (_message.Message,), dict(
  DESCRIPTOR = _ANIMATIONDONE,
  __module__ = 'sprite_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.AnimationDone)
  ))
_sym_db.RegisterMessage(AnimationDone)

SetFlipHorizontal = _reflection.GeneratedProtocolMessageType('SetFlipHorizontal', (_message.Message,), dict(
  DESCRIPTOR = _SETFLIPHORIZONTAL,
  __module__ = 'sprite_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.SetFlipHorizontal)
  ))
_sym_db.RegisterMessage(SetFlipHorizontal)

SetFlipVertical = _reflection.GeneratedProtocolMessageType('SetFlipVertical', (_message.Message,), dict(
  DESCRIPTOR = _SETFLIPVERTICAL,
  __module__ = 'sprite_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmGameSystemDDF.SetFlipVertical)
  ))
_sym_db.RegisterMessage(SetFlipVertical)


DESCRIPTOR._options = None
_SPRITEDESC_BLENDMODE.values_by_name["BLEND_MODE_ALPHA"]._options = None
_SPRITEDESC_BLENDMODE.values_by_name["BLEND_MODE_ADD"]._options = None
_SPRITEDESC_BLENDMODE.values_by_name["BLEND_MODE_ADD_ALPHA"]._options = None
_SPRITEDESC_BLENDMODE.values_by_name["BLEND_MODE_MULT"]._options = None
_SPRITEDESC_BLENDMODE.values_by_name["BLEND_MODE_SCREEN"]._options = None
_SPRITEDESC_SIZEMODE.values_by_name["SIZE_MODE_MANUAL"]._options = None
_SPRITEDESC_SIZEMODE.values_by_name["SIZE_MODE_AUTO"]._options = None
_SPRITEDESC.fields_by_name['tile_set']._options = None
_SPRITEDESC.fields_by_name['material']._options = None
# @@protoc_insertion_point(module_scope)
