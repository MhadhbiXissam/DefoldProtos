# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: render_ddf.proto

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
  name='render_ddf.proto',
  package='dmRenderDDF',
  syntax='proto2',
  serialized_options=_b('\n\027com.dynamo.render.protoB\006Render'),
  serialized_pb=_b('\n\x10render_ddf.proto\x12\x0b\x64mRenderDDF\x1a\x14\x64\x64\x66_extensions.proto\x1a\x0e\x64\x64\x66_math.proto\"\xa3\x01\n\x13RenderPrototypeDesc\x12\x14\n\x06script\x18\x01 \x02(\tB\x04\xa0\xbb\x18\x01\x12@\n\tmaterials\x18\x02 \x03(\x0b\x32-.dmRenderDDF.RenderPrototypeDesc.MaterialDesc\x1a\x34\n\x0cMaterialDesc\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x16\n\x08material\x18\x02 \x02(\tB\x04\xa0\xbb\x18\x01\":\n\x08\x44rawText\x12 \n\x08position\x18\x01 \x02(\x0b\x32\x0e.dmMath.Point3\x12\x0c\n\x04text\x18\x02 \x02(\t\"_\n\rDrawDebugText\x12 \n\x08position\x18\x01 \x02(\x0b\x32\x0e.dmMath.Point3\x12\x0c\n\x04text\x18\x02 \x02(\t\x12\x1e\n\x05\x63olor\x18\x03 \x02(\x0b\x32\x0f.dmMath.Vector4\"r\n\x08\x44rawLine\x12#\n\x0bstart_point\x18\x01 \x02(\x0b\x32\x0e.dmMath.Point3\x12!\n\tend_point\x18\x02 \x02(\x0b\x32\x0e.dmMath.Point3\x12\x1e\n\x05\x63olor\x18\x03 \x02(\x0b\x32\x0f.dmMath.Vector4\".\n\rWindowResized\x12\r\n\x05width\x18\x01 \x02(\r\x12\x0e\n\x06height\x18\x02 \x02(\r\"\'\n\x06Resize\x12\r\n\x05width\x18\x01 \x02(\r\x12\x0e\n\x06height\x18\x02 \x02(\r\",\n\nClearColor\x12\x1e\n\x05\x63olor\x18\x01 \x02(\x0b\x32\x0f.dmMath.Vector4\"O\n\x17\x44isplayProfileQualifier\x12\r\n\x05width\x18\x01 \x02(\r\x12\x0e\n\x06height\x18\x02 \x02(\r\x12\x15\n\rdevice_models\x18\x03 \x03(\t\"X\n\x0e\x44isplayProfile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x38\n\nqualifiers\x18\x02 \x03(\x0b\x32$.dmRenderDDF.DisplayProfileQualifier\"@\n\x0f\x44isplayProfiles\x12-\n\x08profiles\x18\x01 \x03(\x0b\x32\x1b.dmRenderDDF.DisplayProfileB!\n\x17\x63om.dynamo.render.protoB\x06Render')
  ,
  dependencies=[ddf__extensions__pb2.DESCRIPTOR,ddf__math__pb2.DESCRIPTOR,])




_RENDERPROTOTYPEDESC_MATERIALDESC = _descriptor.Descriptor(
  name='MaterialDesc',
  full_name='dmRenderDDF.RenderPrototypeDesc.MaterialDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dmRenderDDF.RenderPrototypeDesc.MaterialDesc.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material', full_name='dmRenderDDF.RenderPrototypeDesc.MaterialDesc.material', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=183,
  serialized_end=235,
)

_RENDERPROTOTYPEDESC = _descriptor.Descriptor(
  name='RenderPrototypeDesc',
  full_name='dmRenderDDF.RenderPrototypeDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='dmRenderDDF.RenderPrototypeDesc.script', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\240\273\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='materials', full_name='dmRenderDDF.RenderPrototypeDesc.materials', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RENDERPROTOTYPEDESC_MATERIALDESC, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=235,
)


_DRAWTEXT = _descriptor.Descriptor(
  name='DrawText',
  full_name='dmRenderDDF.DrawText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='dmRenderDDF.DrawText.position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='dmRenderDDF.DrawText.text', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=237,
  serialized_end=295,
)


_DRAWDEBUGTEXT = _descriptor.Descriptor(
  name='DrawDebugText',
  full_name='dmRenderDDF.DrawDebugText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='dmRenderDDF.DrawDebugText.position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='dmRenderDDF.DrawDebugText.text', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='dmRenderDDF.DrawDebugText.color', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=297,
  serialized_end=392,
)


_DRAWLINE = _descriptor.Descriptor(
  name='DrawLine',
  full_name='dmRenderDDF.DrawLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_point', full_name='dmRenderDDF.DrawLine.start_point', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_point', full_name='dmRenderDDF.DrawLine.end_point', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='dmRenderDDF.DrawLine.color', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=394,
  serialized_end=508,
)


_WINDOWRESIZED = _descriptor.Descriptor(
  name='WindowResized',
  full_name='dmRenderDDF.WindowResized',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='dmRenderDDF.WindowResized.width', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='dmRenderDDF.WindowResized.height', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=510,
  serialized_end=556,
)


_RESIZE = _descriptor.Descriptor(
  name='Resize',
  full_name='dmRenderDDF.Resize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='dmRenderDDF.Resize.width', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='dmRenderDDF.Resize.height', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=558,
  serialized_end=597,
)


_CLEARCOLOR = _descriptor.Descriptor(
  name='ClearColor',
  full_name='dmRenderDDF.ClearColor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='dmRenderDDF.ClearColor.color', index=0,
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
  serialized_start=599,
  serialized_end=643,
)


_DISPLAYPROFILEQUALIFIER = _descriptor.Descriptor(
  name='DisplayProfileQualifier',
  full_name='dmRenderDDF.DisplayProfileQualifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='dmRenderDDF.DisplayProfileQualifier.width', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='dmRenderDDF.DisplayProfileQualifier.height', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_models', full_name='dmRenderDDF.DisplayProfileQualifier.device_models', index=2,
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
  serialized_start=645,
  serialized_end=724,
)


_DISPLAYPROFILE = _descriptor.Descriptor(
  name='DisplayProfile',
  full_name='dmRenderDDF.DisplayProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dmRenderDDF.DisplayProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qualifiers', full_name='dmRenderDDF.DisplayProfile.qualifiers', index=1,
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
  serialized_start=726,
  serialized_end=814,
)


_DISPLAYPROFILES = _descriptor.Descriptor(
  name='DisplayProfiles',
  full_name='dmRenderDDF.DisplayProfiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profiles', full_name='dmRenderDDF.DisplayProfiles.profiles', index=0,
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
  serialized_start=816,
  serialized_end=880,
)

_RENDERPROTOTYPEDESC_MATERIALDESC.containing_type = _RENDERPROTOTYPEDESC
_RENDERPROTOTYPEDESC.fields_by_name['materials'].message_type = _RENDERPROTOTYPEDESC_MATERIALDESC
_DRAWTEXT.fields_by_name['position'].message_type = ddf__math__pb2._POINT3
_DRAWDEBUGTEXT.fields_by_name['position'].message_type = ddf__math__pb2._POINT3
_DRAWDEBUGTEXT.fields_by_name['color'].message_type = ddf__math__pb2._VECTOR4
_DRAWLINE.fields_by_name['start_point'].message_type = ddf__math__pb2._POINT3
_DRAWLINE.fields_by_name['end_point'].message_type = ddf__math__pb2._POINT3
_DRAWLINE.fields_by_name['color'].message_type = ddf__math__pb2._VECTOR4
_CLEARCOLOR.fields_by_name['color'].message_type = ddf__math__pb2._VECTOR4
_DISPLAYPROFILE.fields_by_name['qualifiers'].message_type = _DISPLAYPROFILEQUALIFIER
_DISPLAYPROFILES.fields_by_name['profiles'].message_type = _DISPLAYPROFILE
DESCRIPTOR.message_types_by_name['RenderPrototypeDesc'] = _RENDERPROTOTYPEDESC
DESCRIPTOR.message_types_by_name['DrawText'] = _DRAWTEXT
DESCRIPTOR.message_types_by_name['DrawDebugText'] = _DRAWDEBUGTEXT
DESCRIPTOR.message_types_by_name['DrawLine'] = _DRAWLINE
DESCRIPTOR.message_types_by_name['WindowResized'] = _WINDOWRESIZED
DESCRIPTOR.message_types_by_name['Resize'] = _RESIZE
DESCRIPTOR.message_types_by_name['ClearColor'] = _CLEARCOLOR
DESCRIPTOR.message_types_by_name['DisplayProfileQualifier'] = _DISPLAYPROFILEQUALIFIER
DESCRIPTOR.message_types_by_name['DisplayProfile'] = _DISPLAYPROFILE
DESCRIPTOR.message_types_by_name['DisplayProfiles'] = _DISPLAYPROFILES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RenderPrototypeDesc = _reflection.GeneratedProtocolMessageType('RenderPrototypeDesc', (_message.Message,), dict(

  MaterialDesc = _reflection.GeneratedProtocolMessageType('MaterialDesc', (_message.Message,), dict(
    DESCRIPTOR = _RENDERPROTOTYPEDESC_MATERIALDESC,
    __module__ = 'render_ddf_pb2'
    # @@protoc_insertion_point(class_scope:dmRenderDDF.RenderPrototypeDesc.MaterialDesc)
    ))
  ,
  DESCRIPTOR = _RENDERPROTOTYPEDESC,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.RenderPrototypeDesc)
  ))
_sym_db.RegisterMessage(RenderPrototypeDesc)
_sym_db.RegisterMessage(RenderPrototypeDesc.MaterialDesc)

DrawText = _reflection.GeneratedProtocolMessageType('DrawText', (_message.Message,), dict(
  DESCRIPTOR = _DRAWTEXT,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.DrawText)
  ))
_sym_db.RegisterMessage(DrawText)

DrawDebugText = _reflection.GeneratedProtocolMessageType('DrawDebugText', (_message.Message,), dict(
  DESCRIPTOR = _DRAWDEBUGTEXT,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.DrawDebugText)
  ))
_sym_db.RegisterMessage(DrawDebugText)

DrawLine = _reflection.GeneratedProtocolMessageType('DrawLine', (_message.Message,), dict(
  DESCRIPTOR = _DRAWLINE,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.DrawLine)
  ))
_sym_db.RegisterMessage(DrawLine)

WindowResized = _reflection.GeneratedProtocolMessageType('WindowResized', (_message.Message,), dict(
  DESCRIPTOR = _WINDOWRESIZED,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.WindowResized)
  ))
_sym_db.RegisterMessage(WindowResized)

Resize = _reflection.GeneratedProtocolMessageType('Resize', (_message.Message,), dict(
  DESCRIPTOR = _RESIZE,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.Resize)
  ))
_sym_db.RegisterMessage(Resize)

ClearColor = _reflection.GeneratedProtocolMessageType('ClearColor', (_message.Message,), dict(
  DESCRIPTOR = _CLEARCOLOR,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.ClearColor)
  ))
_sym_db.RegisterMessage(ClearColor)

DisplayProfileQualifier = _reflection.GeneratedProtocolMessageType('DisplayProfileQualifier', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYPROFILEQUALIFIER,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.DisplayProfileQualifier)
  ))
_sym_db.RegisterMessage(DisplayProfileQualifier)

DisplayProfile = _reflection.GeneratedProtocolMessageType('DisplayProfile', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYPROFILE,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.DisplayProfile)
  ))
_sym_db.RegisterMessage(DisplayProfile)

DisplayProfiles = _reflection.GeneratedProtocolMessageType('DisplayProfiles', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYPROFILES,
  __module__ = 'render_ddf_pb2'
  # @@protoc_insertion_point(class_scope:dmRenderDDF.DisplayProfiles)
  ))
_sym_db.RegisterMessage(DisplayProfiles)


DESCRIPTOR._options = None
_RENDERPROTOTYPEDESC_MATERIALDESC.fields_by_name['material']._options = None
_RENDERPROTOTYPEDESC.fields_by_name['script']._options = None
# @@protoc_insertion_point(module_scope)
