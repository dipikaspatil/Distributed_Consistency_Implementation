# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KeyValueClusterStore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='KeyValueClusterStore.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1aKeyValueClusterStore.proto\"t\n\x0fSetupConnection\x12.\n\x0c\x61ll_clusters\x18\x02 \x03(\x0b\x32\x18.SetupConnection.Cluster\x1a\x31\n\x07\x43luster\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\"&\n\x0e\x43onnectReplica\x12\x14\n\x0creplica_name\x18\x01 \x01(\t\"4\n\rConnectClient\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\"\x91\x02\n\rClientRequest\x12\x14\n\x0crequest_type\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12.\n\x0bget_request\x18\x04 \x01(\x0b\x32\x19.ClientRequest.GetRequest\x12.\n\x0bput_request\x18\x05 \x01(\x0b\x32\x19.ClientRequest.PutRequest\x12\x19\n\x11\x63onsistency_level\x18\x06 \x01(\r\x1a\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x1a(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\"q\n\x13\x43oordinatorResponse\x12\x15\n\rresponse_type\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\r\x12\r\n\x05value\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\"\xc1\x02\n\x0eReplicaRequest\x12\x18\n\x10src_replica_name\x18\x01 \x01(\t\x12\x19\n\x11\x64\x65st_replica_name\x18\x02 \x01(\t\x12\x14\n\x0crequest_type\x18\x03 \x01(\t\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\x12\x12\n\nrequest_id\x18\x05 \x01(\t\x12/\n\x0bget_request\x18\x06 \x01(\x0b\x32\x1a.ReplicaRequest.GetRequest\x12/\n\x0bput_request\x18\x07 \x01(\x0b\x32\x1a.ReplicaRequest.PutRequest\x1a\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x1a;\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"\xc9\x01\n\x0fReplicaResponse\x12\x18\n\x10src_replica_name\x18\x01 \x01(\t\x12\x19\n\x11\x64\x65st_replica_name\x18\x02 \x01(\t\x12\x15\n\rresponse_type\x18\x03 \x01(\t\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\x12\x12\n\nrequest_id\x18\x05 \x01(\t\x12\x0b\n\x03key\x18\x06 \x01(\r\x12\r\n\x05value\x18\x07 \x01(\t\x12\x11\n\ttimestamp\x18\x08 \x01(\t\x12\x0f\n\x07message\x18\t \x01(\t\";\n\nReadRepair\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\">\n\rHintedHandoff\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"\xb2\x03\n\x0fKeyValueMessage\x12,\n\x10setup_connection\x18\x01 \x01(\x0b\x32\x10.SetupConnectionH\x00\x12*\n\x0f\x63onnect_replica\x18\x02 \x01(\x0b\x32\x0f.ConnectReplicaH\x00\x12(\n\x0e\x63onnect_client\x18\x03 \x01(\x0b\x32\x0e.ConnectClientH\x00\x12(\n\x0e\x63lient_request\x18\x04 \x01(\x0b\x32\x0e.ClientRequestH\x00\x12\x34\n\x14\x63oordinator_response\x18\x05 \x01(\x0b\x32\x14.CoordinatorResponseH\x00\x12*\n\x0freplica_request\x18\x06 \x01(\x0b\x32\x0f.ReplicaRequestH\x00\x12,\n\x10replica_response\x18\x07 \x01(\x0b\x32\x10.ReplicaResponseH\x00\x12\"\n\x0bread_repair\x18\x08 \x01(\x0b\x32\x0b.ReadRepairH\x00\x12(\n\x0ehinted_handoff\x18\t \x01(\x0b\x32\x0e.HintedHandoffH\x00\x42\x13\n\x11key_value_messageb\x06proto3')
)




_SETUPCONNECTION_CLUSTER = _descriptor.Descriptor(
  name='Cluster',
  full_name='SetupConnection.Cluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SetupConnection.Cluster.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='SetupConnection.Cluster.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='SetupConnection.Cluster.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=146,
)

_SETUPCONNECTION = _descriptor.Descriptor(
  name='SetupConnection',
  full_name='SetupConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_clusters', full_name='SetupConnection.all_clusters', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SETUPCONNECTION_CLUSTER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=146,
)


_CONNECTREPLICA = _descriptor.Descriptor(
  name='ConnectReplica',
  full_name='ConnectReplica',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replica_name', full_name='ConnectReplica.replica_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=186,
)


_CONNECTCLIENT = _descriptor.Descriptor(
  name='ConnectClient',
  full_name='ConnectClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='ConnectClient.src', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='ConnectClient.transaction_id', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=240,
)


_CLIENTREQUEST_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='ClientRequest.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientRequest.GetRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=474,
)

_CLIENTREQUEST_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='ClientRequest.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientRequest.PutRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientRequest.PutRequest.value', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=516,
)

_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='ClientRequest.request_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='ClientRequest.transaction_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='ClientRequest.request_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_request', full_name='ClientRequest.get_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='put_request', full_name='ClientRequest.put_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consistency_level', full_name='ClientRequest.consistency_level', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTREQUEST_GETREQUEST, _CLIENTREQUEST_PUTREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=516,
)


_COORDINATORRESPONSE = _descriptor.Descriptor(
  name='CoordinatorResponse',
  full_name='CoordinatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_type', full_name='CoordinatorResponse.response_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='CoordinatorResponse.transaction_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='CoordinatorResponse.key', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='CoordinatorResponse.value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='CoordinatorResponse.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=631,
)


_REPLICAREQUEST_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='ReplicaRequest.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaRequest.GetRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=474,
)

_REPLICAREQUEST_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='ReplicaRequest.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaRequest.PutRequest.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReplicaRequest.PutRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaRequest.PutRequest.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=896,
  serialized_end=955,
)

_REPLICAREQUEST = _descriptor.Descriptor(
  name='ReplicaRequest',
  full_name='ReplicaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src_replica_name', full_name='ReplicaRequest.src_replica_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_replica_name', full_name='ReplicaRequest.dest_replica_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='ReplicaRequest.request_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='ReplicaRequest.transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='ReplicaRequest.request_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_request', full_name='ReplicaRequest.get_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='put_request', full_name='ReplicaRequest.put_request', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPLICAREQUEST_GETREQUEST, _REPLICAREQUEST_PUTREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=955,
)


_REPLICARESPONSE = _descriptor.Descriptor(
  name='ReplicaResponse',
  full_name='ReplicaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src_replica_name', full_name='ReplicaResponse.src_replica_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_replica_name', full_name='ReplicaResponse.dest_replica_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_type', full_name='ReplicaResponse.response_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='ReplicaResponse.transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='ReplicaResponse.request_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaResponse.key', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReplicaResponse.value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaResponse.timestamp', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ReplicaResponse.message', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=958,
  serialized_end=1159,
)


_READREPAIR = _descriptor.Descriptor(
  name='ReadRepair',
  full_name='ReadRepair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ReadRepair.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReadRepair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReadRepair.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1161,
  serialized_end=1220,
)


_HINTEDHANDOFF = _descriptor.Descriptor(
  name='HintedHandoff',
  full_name='HintedHandoff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='HintedHandoff.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='HintedHandoff.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='HintedHandoff.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1222,
  serialized_end=1284,
)


_KEYVALUEMESSAGE = _descriptor.Descriptor(
  name='KeyValueMessage',
  full_name='KeyValueMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setup_connection', full_name='KeyValueMessage.setup_connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect_replica', full_name='KeyValueMessage.connect_replica', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect_client', full_name='KeyValueMessage.connect_client', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_request', full_name='KeyValueMessage.client_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinator_response', full_name='KeyValueMessage.coordinator_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replica_request', full_name='KeyValueMessage.replica_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replica_response', full_name='KeyValueMessage.replica_response', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_repair', full_name='KeyValueMessage.read_repair', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hinted_handoff', full_name='KeyValueMessage.hinted_handoff', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='key_value_message', full_name='KeyValueMessage.key_value_message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1287,
  serialized_end=1721,
)

_SETUPCONNECTION_CLUSTER.containing_type = _SETUPCONNECTION
_SETUPCONNECTION.fields_by_name['all_clusters'].message_type = _SETUPCONNECTION_CLUSTER
_CLIENTREQUEST_GETREQUEST.containing_type = _CLIENTREQUEST
_CLIENTREQUEST_PUTREQUEST.containing_type = _CLIENTREQUEST
_CLIENTREQUEST.fields_by_name['get_request'].message_type = _CLIENTREQUEST_GETREQUEST
_CLIENTREQUEST.fields_by_name['put_request'].message_type = _CLIENTREQUEST_PUTREQUEST
_REPLICAREQUEST_GETREQUEST.containing_type = _REPLICAREQUEST
_REPLICAREQUEST_PUTREQUEST.containing_type = _REPLICAREQUEST
_REPLICAREQUEST.fields_by_name['get_request'].message_type = _REPLICAREQUEST_GETREQUEST
_REPLICAREQUEST.fields_by_name['put_request'].message_type = _REPLICAREQUEST_PUTREQUEST
_KEYVALUEMESSAGE.fields_by_name['setup_connection'].message_type = _SETUPCONNECTION
_KEYVALUEMESSAGE.fields_by_name['connect_replica'].message_type = _CONNECTREPLICA
_KEYVALUEMESSAGE.fields_by_name['connect_client'].message_type = _CONNECTCLIENT
_KEYVALUEMESSAGE.fields_by_name['client_request'].message_type = _CLIENTREQUEST
_KEYVALUEMESSAGE.fields_by_name['coordinator_response'].message_type = _COORDINATORRESPONSE
_KEYVALUEMESSAGE.fields_by_name['replica_request'].message_type = _REPLICAREQUEST
_KEYVALUEMESSAGE.fields_by_name['replica_response'].message_type = _REPLICARESPONSE
_KEYVALUEMESSAGE.fields_by_name['read_repair'].message_type = _READREPAIR
_KEYVALUEMESSAGE.fields_by_name['hinted_handoff'].message_type = _HINTEDHANDOFF
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['setup_connection'])
_KEYVALUEMESSAGE.fields_by_name['setup_connection'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['connect_replica'])
_KEYVALUEMESSAGE.fields_by_name['connect_replica'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['connect_client'])
_KEYVALUEMESSAGE.fields_by_name['connect_client'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['client_request'])
_KEYVALUEMESSAGE.fields_by_name['client_request'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['coordinator_response'])
_KEYVALUEMESSAGE.fields_by_name['coordinator_response'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replica_request'])
_KEYVALUEMESSAGE.fields_by_name['replica_request'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replica_response'])
_KEYVALUEMESSAGE.fields_by_name['replica_response'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['read_repair'])
_KEYVALUEMESSAGE.fields_by_name['read_repair'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['hinted_handoff'])
_KEYVALUEMESSAGE.fields_by_name['hinted_handoff'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
DESCRIPTOR.message_types_by_name['SetupConnection'] = _SETUPCONNECTION
DESCRIPTOR.message_types_by_name['ConnectReplica'] = _CONNECTREPLICA
DESCRIPTOR.message_types_by_name['ConnectClient'] = _CONNECTCLIENT
DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['CoordinatorResponse'] = _COORDINATORRESPONSE
DESCRIPTOR.message_types_by_name['ReplicaRequest'] = _REPLICAREQUEST
DESCRIPTOR.message_types_by_name['ReplicaResponse'] = _REPLICARESPONSE
DESCRIPTOR.message_types_by_name['ReadRepair'] = _READREPAIR
DESCRIPTOR.message_types_by_name['HintedHandoff'] = _HINTEDHANDOFF
DESCRIPTOR.message_types_by_name['KeyValueMessage'] = _KEYVALUEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetupConnection = _reflection.GeneratedProtocolMessageType('SetupConnection', (_message.Message,), dict(

  Cluster = _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), dict(
    DESCRIPTOR = _SETUPCONNECTION_CLUSTER,
    __module__ = 'KeyValueClusterStore_pb2'
    # @@protoc_insertion_point(class_scope:SetupConnection.Cluster)
    ))
  ,
  DESCRIPTOR = _SETUPCONNECTION,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:SetupConnection)
  ))
_sym_db.RegisterMessage(SetupConnection)
_sym_db.RegisterMessage(SetupConnection.Cluster)

ConnectReplica = _reflection.GeneratedProtocolMessageType('ConnectReplica', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREPLICA,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:ConnectReplica)
  ))
_sym_db.RegisterMessage(ConnectReplica)

ConnectClient = _reflection.GeneratedProtocolMessageType('ConnectClient', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTCLIENT,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:ConnectClient)
  ))
_sym_db.RegisterMessage(ConnectClient)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), dict(

  GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTREQUEST_GETREQUEST,
    __module__ = 'KeyValueClusterStore_pb2'
    # @@protoc_insertion_point(class_scope:ClientRequest.GetRequest)
    ))
  ,

  PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTREQUEST_PUTREQUEST,
    __module__ = 'KeyValueClusterStore_pb2'
    # @@protoc_insertion_point(class_scope:ClientRequest.PutRequest)
    ))
  ,
  DESCRIPTOR = _CLIENTREQUEST,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:ClientRequest)
  ))
_sym_db.RegisterMessage(ClientRequest)
_sym_db.RegisterMessage(ClientRequest.GetRequest)
_sym_db.RegisterMessage(ClientRequest.PutRequest)

CoordinatorResponse = _reflection.GeneratedProtocolMessageType('CoordinatorResponse', (_message.Message,), dict(
  DESCRIPTOR = _COORDINATORRESPONSE,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:CoordinatorResponse)
  ))
_sym_db.RegisterMessage(CoordinatorResponse)

ReplicaRequest = _reflection.GeneratedProtocolMessageType('ReplicaRequest', (_message.Message,), dict(

  GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
    DESCRIPTOR = _REPLICAREQUEST_GETREQUEST,
    __module__ = 'KeyValueClusterStore_pb2'
    # @@protoc_insertion_point(class_scope:ReplicaRequest.GetRequest)
    ))
  ,

  PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), dict(
    DESCRIPTOR = _REPLICAREQUEST_PUTREQUEST,
    __module__ = 'KeyValueClusterStore_pb2'
    # @@protoc_insertion_point(class_scope:ReplicaRequest.PutRequest)
    ))
  ,
  DESCRIPTOR = _REPLICAREQUEST,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaRequest)
  ))
_sym_db.RegisterMessage(ReplicaRequest)
_sym_db.RegisterMessage(ReplicaRequest.GetRequest)
_sym_db.RegisterMessage(ReplicaRequest.PutRequest)

ReplicaResponse = _reflection.GeneratedProtocolMessageType('ReplicaResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLICARESPONSE,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaResponse)
  ))
_sym_db.RegisterMessage(ReplicaResponse)

ReadRepair = _reflection.GeneratedProtocolMessageType('ReadRepair', (_message.Message,), dict(
  DESCRIPTOR = _READREPAIR,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:ReadRepair)
  ))
_sym_db.RegisterMessage(ReadRepair)

HintedHandoff = _reflection.GeneratedProtocolMessageType('HintedHandoff', (_message.Message,), dict(
  DESCRIPTOR = _HINTEDHANDOFF,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:HintedHandoff)
  ))
_sym_db.RegisterMessage(HintedHandoff)

KeyValueMessage = _reflection.GeneratedProtocolMessageType('KeyValueMessage', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUEMESSAGE,
  __module__ = 'KeyValueClusterStore_pb2'
  # @@protoc_insertion_point(class_scope:KeyValueMessage)
  ))
_sym_db.RegisterMessage(KeyValueMessage)


# @@protoc_insertion_point(module_scope)
