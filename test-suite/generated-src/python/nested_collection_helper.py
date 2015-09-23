# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from nested_collection.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyObject, CPyObject, CPyObjectProxy, CPyRecord, CPyString

from dh__list_set_string import ListSetStringHelper
from dh__set_string import SetStringHelper
from dh__set_string import SetStringProxy
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from nested_collection import NestedCollection

class NestedCollectionHelper:
    @staticmethod
    def release(c_ptr): 
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("struct DjinniObjectHandle *(struct DjinniRecordHandle *)")
    def get_nested_collection_f1(cself):
        try:
            _ret = CPyObject.fromPy(ListSetStringHelper.c_data_set, CPyRecord.toPy(None, cself).set_list)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniObjectHandle *)")
    def python_create_nested_collection(set_list):
        py_rec = NestedCollection(
            CPyObject.toPy(ListSetStringHelper.c_data_set, set_list))
        return CPyRecord.fromPy(NestedCollection.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in NestedCollection.c_data_set
        NestedCollection.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.nested_collection_add_callback_get_nested_collection_f1(NestedCollectionHelper.get_nested_collection_f1)
        lib.nested_collection_add_callback___delete(NestedCollectionHelper.__delete)
        lib.nested_collection_add_callback_python_create_nested_collection(NestedCollectionHelper.python_create_nested_collection)

NestedCollectionHelper._add_callbacks()

