#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class RETURN_CODE:
  RC_SUCCESS = 0
  RC_FAIL = 1
  RC_SERVER_NOT_FOUND = 2
  RC_SERVER_ALREADY_EXIST = 3

  _VALUES_TO_NAMES = {
    0: "RC_SUCCESS",
    1: "RC_FAIL",
    2: "RC_SERVER_NOT_FOUND",
    3: "RC_SERVER_ALREADY_EXIST",
  }

  _NAMES_TO_VALUES = {
    "RC_SUCCESS": 0,
    "RC_FAIL": 1,
    "RC_SERVER_NOT_FOUND": 2,
    "RC_SERVER_ALREADY_EXIST": 3,
  }


class OP_RESULT:
  """
  Attributes:
   - rcode
   - reason
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'rcode', None, None, ), # 1
    (2, TType.STRING, 'reason', None, None, ), # 2
  )

  def __init__(self, rcode=None, reason=None,):
    self.rcode = rcode
    self.reason = reason

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.rcode = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.reason = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('OP_RESULT')
    if self.rcode is not None:
      oprot.writeFieldBegin('rcode', TType.I32, 1)
      oprot.writeI32(self.rcode)
      oprot.writeFieldEnd()
    if self.reason is not None:
      oprot.writeFieldBegin('reason', TType.STRING, 2)
      oprot.writeString(self.reason)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.rcode)
    value = (value * 31) ^ hash(self.reason)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class HardwareSpec:
  """
  Attributes:
   - flavor
   - cpu_core
   - memory_count
   - memory_volume
   - disk_count
   - disk_volume
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'flavor', None, None, ), # 1
    (2, TType.I32, 'cpu_core', None, None, ), # 2
    (3, TType.I32, 'memory_count', None, None, ), # 3
    (4, TType.I32, 'memory_volume', None, None, ), # 4
    (5, TType.I32, 'disk_count', None, None, ), # 5
    (6, TType.I32, 'disk_volume', None, None, ), # 6
  )

  def __init__(self, flavor=None, cpu_core=None, memory_count=None, memory_volume=None, disk_count=None, disk_volume=None,):
    self.flavor = flavor
    self.cpu_core = cpu_core
    self.memory_count = memory_count
    self.memory_volume = memory_volume
    self.disk_count = disk_count
    self.disk_volume = disk_volume

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.flavor = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.cpu_core = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.memory_count = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.memory_volume = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.disk_count = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.disk_volume = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('HardwareSpec')
    if self.flavor is not None:
      oprot.writeFieldBegin('flavor', TType.STRING, 1)
      oprot.writeString(self.flavor)
      oprot.writeFieldEnd()
    if self.cpu_core is not None:
      oprot.writeFieldBegin('cpu_core', TType.I32, 2)
      oprot.writeI32(self.cpu_core)
      oprot.writeFieldEnd()
    if self.memory_count is not None:
      oprot.writeFieldBegin('memory_count', TType.I32, 3)
      oprot.writeI32(self.memory_count)
      oprot.writeFieldEnd()
    if self.memory_volume is not None:
      oprot.writeFieldBegin('memory_volume', TType.I32, 4)
      oprot.writeI32(self.memory_volume)
      oprot.writeFieldEnd()
    if self.disk_count is not None:
      oprot.writeFieldBegin('disk_count', TType.I32, 5)
      oprot.writeI32(self.disk_count)
      oprot.writeFieldEnd()
    if self.disk_volume is not None:
      oprot.writeFieldBegin('disk_volume', TType.I32, 6)
      oprot.writeI32(self.disk_volume)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.flavor)
    value = (value * 31) ^ hash(self.cpu_core)
    value = (value * 31) ^ hash(self.memory_count)
    value = (value * 31) ^ hash(self.memory_volume)
    value = (value * 31) ^ hash(self.disk_count)
    value = (value * 31) ^ hash(self.disk_volume)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class VmInfo:
  """
  Attributes:
   - hostname
   - uuid
   - availability_zone
   - project_type
   - nic1
   - nic2
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'hostname', None, None, ), # 1
    (2, TType.STRING, 'uuid', None, None, ), # 2
    (3, TType.STRING, 'availability_zone', None, None, ), # 3
    (4, TType.STRING, 'project_type', None, None, ), # 4
    (5, TType.STRING, 'nic1', None, None, ), # 5
    (6, TType.STRING, 'nic2', None, None, ), # 6
  )

  def __init__(self, hostname=None, uuid=None, availability_zone=None, project_type=None, nic1=None, nic2=None,):
    self.hostname = hostname
    self.uuid = uuid
    self.availability_zone = availability_zone
    self.project_type = project_type
    self.nic1 = nic1
    self.nic2 = nic2

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.hostname = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.uuid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.availability_zone = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.project_type = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.nic1 = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.nic2 = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('VmInfo')
    if self.hostname is not None:
      oprot.writeFieldBegin('hostname', TType.STRING, 1)
      oprot.writeString(self.hostname)
      oprot.writeFieldEnd()
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 2)
      oprot.writeString(self.uuid)
      oprot.writeFieldEnd()
    if self.availability_zone is not None:
      oprot.writeFieldBegin('availability_zone', TType.STRING, 3)
      oprot.writeString(self.availability_zone)
      oprot.writeFieldEnd()
    if self.project_type is not None:
      oprot.writeFieldBegin('project_type', TType.STRING, 4)
      oprot.writeString(self.project_type)
      oprot.writeFieldEnd()
    if self.nic1 is not None:
      oprot.writeFieldBegin('nic1', TType.STRING, 5)
      oprot.writeString(self.nic1)
      oprot.writeFieldEnd()
    if self.nic2 is not None:
      oprot.writeFieldBegin('nic2', TType.STRING, 6)
      oprot.writeString(self.nic2)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.hostname)
    value = (value * 31) ^ hash(self.uuid)
    value = (value * 31) ^ hash(self.availability_zone)
    value = (value * 31) ^ hash(self.project_type)
    value = (value * 31) ^ hash(self.nic1)
    value = (value * 31) ^ hash(self.nic2)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AliveInfo:
  """
  Attributes:
   - wmi_private_fx
   - wmi_private_fl
   - wmi_public_fx
   - wmi_public_fl
   - normal_public_fx
   - normal_public_fl
   - wmi_private_fx_latency
   - wmi_private_fl_latency
   - wmi_public_fx_latency
   - wmi_public_fl_latency
   - normal_public_fx_latency
   - normal_public_fl_latency
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'wmi_private_fx', None, None, ), # 1
    (2, TType.BOOL, 'wmi_private_fl', None, None, ), # 2
    (3, TType.BOOL, 'wmi_public_fx', None, None, ), # 3
    (4, TType.BOOL, 'wmi_public_fl', None, None, ), # 4
    (5, TType.BOOL, 'normal_public_fx', None, None, ), # 5
    (6, TType.BOOL, 'normal_public_fl', None, None, ), # 6
    (7, TType.DOUBLE, 'wmi_private_fx_latency', None, None, ), # 7
    (8, TType.DOUBLE, 'wmi_private_fl_latency', None, None, ), # 8
    (9, TType.DOUBLE, 'wmi_public_fx_latency', None, None, ), # 9
    (10, TType.DOUBLE, 'wmi_public_fl_latency', None, None, ), # 10
    (11, TType.DOUBLE, 'normal_public_fx_latency', None, None, ), # 11
    (12, TType.DOUBLE, 'normal_public_fl_latency', None, None, ), # 12
  )

  def __init__(self, wmi_private_fx=None, wmi_private_fl=None, wmi_public_fx=None, wmi_public_fl=None, normal_public_fx=None, normal_public_fl=None, wmi_private_fx_latency=None, wmi_private_fl_latency=None, wmi_public_fx_latency=None, wmi_public_fl_latency=None, normal_public_fx_latency=None, normal_public_fl_latency=None,):
    self.wmi_private_fx = wmi_private_fx
    self.wmi_private_fl = wmi_private_fl
    self.wmi_public_fx = wmi_public_fx
    self.wmi_public_fl = wmi_public_fl
    self.normal_public_fx = normal_public_fx
    self.normal_public_fl = normal_public_fl
    self.wmi_private_fx_latency = wmi_private_fx_latency
    self.wmi_private_fl_latency = wmi_private_fl_latency
    self.wmi_public_fx_latency = wmi_public_fx_latency
    self.wmi_public_fl_latency = wmi_public_fl_latency
    self.normal_public_fx_latency = normal_public_fx_latency
    self.normal_public_fl_latency = normal_public_fl_latency

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.wmi_private_fx = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.wmi_private_fl = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.wmi_public_fx = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.wmi_public_fl = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.normal_public_fx = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.normal_public_fl = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.DOUBLE:
          self.wmi_private_fx_latency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.DOUBLE:
          self.wmi_private_fl_latency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.DOUBLE:
          self.wmi_public_fx_latency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.DOUBLE:
          self.wmi_public_fl_latency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.DOUBLE:
          self.normal_public_fx_latency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.DOUBLE:
          self.normal_public_fl_latency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AliveInfo')
    if self.wmi_private_fx is not None:
      oprot.writeFieldBegin('wmi_private_fx', TType.BOOL, 1)
      oprot.writeBool(self.wmi_private_fx)
      oprot.writeFieldEnd()
    if self.wmi_private_fl is not None:
      oprot.writeFieldBegin('wmi_private_fl', TType.BOOL, 2)
      oprot.writeBool(self.wmi_private_fl)
      oprot.writeFieldEnd()
    if self.wmi_public_fx is not None:
      oprot.writeFieldBegin('wmi_public_fx', TType.BOOL, 3)
      oprot.writeBool(self.wmi_public_fx)
      oprot.writeFieldEnd()
    if self.wmi_public_fl is not None:
      oprot.writeFieldBegin('wmi_public_fl', TType.BOOL, 4)
      oprot.writeBool(self.wmi_public_fl)
      oprot.writeFieldEnd()
    if self.normal_public_fx is not None:
      oprot.writeFieldBegin('normal_public_fx', TType.BOOL, 5)
      oprot.writeBool(self.normal_public_fx)
      oprot.writeFieldEnd()
    if self.normal_public_fl is not None:
      oprot.writeFieldBegin('normal_public_fl', TType.BOOL, 6)
      oprot.writeBool(self.normal_public_fl)
      oprot.writeFieldEnd()
    if self.wmi_private_fx_latency is not None:
      oprot.writeFieldBegin('wmi_private_fx_latency', TType.DOUBLE, 7)
      oprot.writeDouble(self.wmi_private_fx_latency)
      oprot.writeFieldEnd()
    if self.wmi_private_fl_latency is not None:
      oprot.writeFieldBegin('wmi_private_fl_latency', TType.DOUBLE, 8)
      oprot.writeDouble(self.wmi_private_fl_latency)
      oprot.writeFieldEnd()
    if self.wmi_public_fx_latency is not None:
      oprot.writeFieldBegin('wmi_public_fx_latency', TType.DOUBLE, 9)
      oprot.writeDouble(self.wmi_public_fx_latency)
      oprot.writeFieldEnd()
    if self.wmi_public_fl_latency is not None:
      oprot.writeFieldBegin('wmi_public_fl_latency', TType.DOUBLE, 10)
      oprot.writeDouble(self.wmi_public_fl_latency)
      oprot.writeFieldEnd()
    if self.normal_public_fx_latency is not None:
      oprot.writeFieldBegin('normal_public_fx_latency', TType.DOUBLE, 11)
      oprot.writeDouble(self.normal_public_fx_latency)
      oprot.writeFieldEnd()
    if self.normal_public_fl_latency is not None:
      oprot.writeFieldBegin('normal_public_fl_latency', TType.DOUBLE, 12)
      oprot.writeDouble(self.normal_public_fl_latency)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.wmi_private_fx)
    value = (value * 31) ^ hash(self.wmi_private_fl)
    value = (value * 31) ^ hash(self.wmi_public_fx)
    value = (value * 31) ^ hash(self.wmi_public_fl)
    value = (value * 31) ^ hash(self.normal_public_fx)
    value = (value * 31) ^ hash(self.normal_public_fl)
    value = (value * 31) ^ hash(self.wmi_private_fx_latency)
    value = (value * 31) ^ hash(self.wmi_private_fl_latency)
    value = (value * 31) ^ hash(self.wmi_public_fx_latency)
    value = (value * 31) ^ hash(self.wmi_public_fl_latency)
    value = (value * 31) ^ hash(self.normal_public_fx_latency)
    value = (value * 31) ^ hash(self.normal_public_fl_latency)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InvalidOperation(TException):
  """
  Attributes:
   - whatOp
   - why
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'whatOp', None, None, ), # 1
    (2, TType.STRING, 'why', None, None, ), # 2
  )

  def __init__(self, whatOp=None, why=None,):
    self.whatOp = whatOp
    self.why = why

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.whatOp = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.why = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InvalidOperation')
    if self.whatOp is not None:
      oprot.writeFieldBegin('whatOp', TType.I32, 1)
      oprot.writeI32(self.whatOp)
      oprot.writeFieldEnd()
    if self.why is not None:
      oprot.writeFieldBegin('why', TType.STRING, 2)
      oprot.writeString(self.why)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.whatOp)
    value = (value * 31) ^ hash(self.why)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
