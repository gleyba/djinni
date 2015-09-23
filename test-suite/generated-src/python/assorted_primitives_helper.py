# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from primtypes.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBoxedBool, CPyBoxedF32, CPyBoxedF64, CPyBoxedI16, CPyBoxedI32, CPyBoxedI64, CPyBoxedI8, CPyPrimitive, CPyRecord
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from assorted_primitives import AssortedPrimitives

class AssortedPrimitivesHelper:
    @staticmethod
    def release(c_ptr): 
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("bool(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f1(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).b)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int8_t(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f2(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).eight)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int16_t(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f3(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).sixteen)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int32_t(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f4(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).thirtytwo)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int64_t(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f5(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).sixtyfour)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("float(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f6(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).fthirtytwo)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("double(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f7(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).fsixtyfour)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedBool *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f8(cself):
        try:
            with CPyBoxedBool.fromPyOpt(CPyRecord.toPy(None, cself).o_b) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI8 *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f9(cself):
        try:
            with CPyBoxedI8.fromPyOpt(CPyRecord.toPy(None, cself).o_eight) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI16 *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f10(cself):
        try:
            with CPyBoxedI16.fromPyOpt(CPyRecord.toPy(None, cself).o_sixteen) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI32 *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f11(cself):
        try:
            with CPyBoxedI32.fromPyOpt(CPyRecord.toPy(None, cself).o_thirtytwo) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI64 *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f12(cself):
        try:
            with CPyBoxedI64.fromPyOpt(CPyRecord.toPy(None, cself).o_sixtyfour) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedF32 *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f13(cself):
        try:
            with CPyBoxedF32.fromPyOpt(CPyRecord.toPy(None, cself).o_fthirtytwo) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedF64 *(struct DjinniRecordHandle *)")
    def get_assorted_primitives_f14(cself):
        try:
            with CPyBoxedF64.fromPyOpt(CPyRecord.toPy(None, cself).o_fsixtyfour) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(bool,int8_t,int16_t,int32_t,int64_t,float,double,struct DjinniBoxedBool *,struct DjinniBoxedI8 *,struct DjinniBoxedI16 *,struct DjinniBoxedI32 *,struct DjinniBoxedI64 *,struct DjinniBoxedF32 *,struct DjinniBoxedF64 *)")
    def python_create_assorted_primitives(b,eight,sixteen,thirtytwo,sixtyfour,fthirtytwo,fsixtyfour,o_b,o_eight,o_sixteen,o_thirtytwo,o_sixtyfour,o_fthirtytwo,o_fsixtyfour):
        py_rec = AssortedPrimitives(
            CPyPrimitive.toPy(b),
            CPyPrimitive.toPy(eight),
            CPyPrimitive.toPy(sixteen),
            CPyPrimitive.toPy(thirtytwo),
            CPyPrimitive.toPy(sixtyfour),
            CPyPrimitive.toPy(fthirtytwo),
            CPyPrimitive.toPy(fsixtyfour),
            CPyBoxedBool.toPyOpt(o_b),
            CPyBoxedI8.toPyOpt(o_eight),
            CPyBoxedI16.toPyOpt(o_sixteen),
            CPyBoxedI32.toPyOpt(o_thirtytwo),
            CPyBoxedI64.toPyOpt(o_sixtyfour),
            CPyBoxedF32.toPyOpt(o_fthirtytwo),
            CPyBoxedF64.toPyOpt(o_fsixtyfour))
        return CPyRecord.fromPy(AssortedPrimitives.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in AssortedPrimitives.c_data_set
        AssortedPrimitives.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.assorted_primitives_add_callback_get_assorted_primitives_f9(AssortedPrimitivesHelper.get_assorted_primitives_f9)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f3(AssortedPrimitivesHelper.get_assorted_primitives_f3)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f14(AssortedPrimitivesHelper.get_assorted_primitives_f14)
        lib.assorted_primitives_add_callback_python_create_assorted_primitives(AssortedPrimitivesHelper.python_create_assorted_primitives)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f4(AssortedPrimitivesHelper.get_assorted_primitives_f4)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f5(AssortedPrimitivesHelper.get_assorted_primitives_f5)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f10(AssortedPrimitivesHelper.get_assorted_primitives_f10)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f6(AssortedPrimitivesHelper.get_assorted_primitives_f6)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f11(AssortedPrimitivesHelper.get_assorted_primitives_f11)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f7(AssortedPrimitivesHelper.get_assorted_primitives_f7)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f12(AssortedPrimitivesHelper.get_assorted_primitives_f12)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f8(AssortedPrimitivesHelper.get_assorted_primitives_f8)
        lib.assorted_primitives_add_callback___delete(AssortedPrimitivesHelper.__delete)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f1(AssortedPrimitivesHelper.get_assorted_primitives_f1)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f13(AssortedPrimitivesHelper.get_assorted_primitives_f13)
        lib.assorted_primitives_add_callback_get_assorted_primitives_f2(AssortedPrimitivesHelper.get_assorted_primitives_f2)

AssortedPrimitivesHelper._add_callbacks()

