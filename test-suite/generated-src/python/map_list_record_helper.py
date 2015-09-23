# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from map.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyObject, CPyObject, CPyObjectProxy, CPyPrimitive, CPyRecord, CPyString

from dh__list_map_string_int64_t import ListMapStringInt64THelper
from dh__map_string_int64_t import MapStringInt64THelper
from dh__map_string_int64_t import MapStringInt64TProxy
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from map_list_record import MapListRecord

class MapListRecordHelper:
    @staticmethod
    def release(c_ptr): 
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_map_list_record_f1(cself):
        try:
            _ret = CPyObject.fromPy(ListMapStringInt64THelper.c_data_set, CPyRecord.toPy(None, cself).map_list)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniObjectHandle *)")
    def python_create_map_list_record(map_list):
        py_rec = MapListRecord(
            CPyObject.toPy(ListMapStringInt64THelper.c_data_set, map_list))
        return CPyRecord.fromPy(MapListRecord.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in MapListRecord.c_data_set
        MapListRecord.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.map_list_record_add_callback_python_create_map_list_record(MapListRecordHelper.python_create_map_list_record)
        lib.map_list_record_add_callback___delete(MapListRecordHelper.__delete)
        lib.map_list_record_add_callback_get_map_list_record_f1(MapListRecordHelper.get_map_list_record_f1)

MapListRecordHelper._add_callbacks()

