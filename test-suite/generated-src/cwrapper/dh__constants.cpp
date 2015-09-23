// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from constants.djinni

#include <iostream> // for debugging
#include <cassert>
#include "wrapper_marshal.hpp"
#include "constants.hpp"

#include "dh__constants.hpp"

static void(*s_py_callback_constants___delete)(DjinniRecordHandle * );
void constants_add_callback___delete(void(* ptr)(DjinniRecordHandle * )) {
    s_py_callback_constants___delete = ptr;
}

void constants___delete(DjinniRecordHandle * drh) {
    s_py_callback_constants___delete(drh);
}
void optional_constants___delete(DjinniOptionalRecordHandle * drh) {
    s_py_callback_constants___delete((DjinniRecordHandle *) drh); // can't static cast, find better way
}
static int32_t ( * s_py_callback_constants_get_constants_f1)(DjinniRecordHandle *);

void constants_add_callback_get_constants_f1(int32_t( * ptr)(DjinniRecordHandle *)) {
    s_py_callback_constants_get_constants_f1 = ptr;
}

static DjinniString * ( * s_py_callback_constants_get_constants_f2)(DjinniRecordHandle *);

void constants_add_callback_get_constants_f2(DjinniString *( * ptr)(DjinniRecordHandle *)) {
    s_py_callback_constants_get_constants_f2 = ptr;
}

static DjinniRecordHandle * ( * s_py_callback_constants_python_create_constants)(int32_t,DjinniString *);

void constants_add_callback_python_create_constants(DjinniRecordHandle *( * ptr)(int32_t,DjinniString *)) {
    s_py_callback_constants_python_create_constants = ptr;
}

djinni::Handle<DjinniRecordHandle> DjinniConstants::fromCpp(const ::testsuite::Constants& dr) {
    auto  _field_some_string = DjinniString::fromCpp(dr.some_string);

    djinni::Handle<DjinniRecordHandle> _aux(
        s_py_callback_constants_python_create_constants(
            dr.some_integer,
            _field_some_string.release()), 
        constants___delete);
    return _aux;
}

::testsuite::Constants DjinniConstants::toCpp(djinni::Handle<DjinniRecordHandle> dh) {
    std::unique_ptr<DjinniString> _field_some_string(s_py_callback_constants_get_constants_f2(dh.get()));

    auto _aux = ::testsuite::Constants(
        s_py_callback_constants_get_constants_f1(dh.get()),
        DjinniString::toCpp(std::move( _field_some_string)));
    return _aux;
}

djinni::Handle<DjinniOptionalRecordHandle> DjinniConstants::fromCpp(std::experimental::optional<::testsuite::Constants> dc) {
    if (dc == std::experimental::nullopt) {
        return nullptr;
    }
    return djinni::optionals::toOptionalHandle(std::move(DjinniConstants::fromCpp(std::move(* dc))), optional_constants___delete);
}

std::experimental::optional<::testsuite::Constants>DjinniConstants::toCpp(djinni::Handle<DjinniOptionalRecordHandle> dh) {
     if (dh) {
        return std::experimental::optional<::testsuite::Constants>(DjinniConstants::toCpp(djinni::optionals::fromOptionalHandle(std::move(dh), constants___delete)));
    }
    return std::experimental::nullopt;
}

