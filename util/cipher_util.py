import ctypes
import ctypes.util
import ssl

CIPHERS = (
    "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:"
    "DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:"
    "!eNULL:!MD5"
    ":HIGH:!DH:!aNULL"
)

def apply_ssl_patch():
    # Programmatically load OpenSSL 3 legacy provider for modern systems (like Ubuntu 22.04+ or Debian 12+)
    # to support legacy algorithms (like 3DES) without modifying system configuration files.
    try:
        libcrypto_path = ctypes.util.find_library('crypto')
        if libcrypto_path:
            libcrypto = ctypes.CDLL(libcrypto_path)
            # OSSL_PROVIDER_load(OSSL_LIB_CTX *libctx, const char *name);
            libcrypto.OSSL_PROVIDER_load.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
            libcrypto.OSSL_PROVIDER_load.restype = ctypes.c_void_p
            libcrypto.OSSL_PROVIDER_load(None, b"legacy")
            libcrypto.OSSL_PROVIDER_load(None, b"default")
    except Exception:
        pass

    original_create_default_context = ssl.create_default_context

    def custom_create_default_context(*args, **kwargs):
        context = original_create_default_context(*args, **kwargs)
        try:
            context.set_ciphers(CIPHERS)
        except ssl.SSLError:
            pass
        return context

    ssl.create_default_context = custom_create_default_context

apply_ssl_patch()