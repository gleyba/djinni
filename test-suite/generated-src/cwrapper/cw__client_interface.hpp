// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from client_interface.djinni

#pragma once

#include <atomic>
#include <experimental/optional>
#include "client_interface.hpp"
#ifdef __cplusplus
extern "C" {
#endif

#include "cw__client_interface.h"

#ifdef __cplusplus
}
#endif
struct DjinniWrapperClientInterface final {
    DjinniWrapperClientInterface(std::shared_ptr<::testsuite::ClientInterface>wo): wrapped_obj(wo) {};

    static std::shared_ptr<::testsuite::ClientInterface> get(djinni::Handle<DjinniWrapperClientInterface> dw);
    static djinni::Handle<DjinniWrapperClientInterface> wrap(std::shared_ptr<::testsuite::ClientInterface> obj);

    const std::shared_ptr<::testsuite::ClientInterface> wrapped_obj;
    std::atomic<size_t> ref_count {1};
};

class ClientInterfacePythonProxy final : public ::testsuite::ClientInterface {
    public:
        explicit ClientInterfacePythonProxy(DjinniObjectHandle * c_ptr);
        ~ClientInterfacePythonProxy();
        DjinniObjectHandle * get_m_py_obj_handle();

        ::testsuite::ClientReturnedRecord get_record(int64_t record_id, const std::string & utf8string, const std::experimental::optional<std::string> & misc);

        double identifier_check(const std::vector<uint8_t> & data, int32_t r, int64_t jret);

        std::string return_str();

    private:
        DjinniObjectHandle * m_py_obj_handle;
};
