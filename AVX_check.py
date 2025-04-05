import os
import struct

def check_avx_support():
    if os.path.exists('/proc/cpuinfo'):
        with open('/proc/cpuinfo', 'r') as f:
            cpuinfo = f.read()
            if 'AVX' in cpuinfo.lower():
                return True
    elif os.name == 'nt':  # For Windows
        try:
            import ctypes
            aux2 = ctypes.windll.kernel32.GetProcAddress(ctypes.windll.kernel32.GetModuleHandleA('kernel32'), 'IsProcessorFeaturePresent')
            aux2.restype = ctypes.c_int
            aux2.argtypes = [ctypes.c_int]
            avx_check = aux2(28)
            return avx_check == 1
        except:
            return False
    else:
        return False

if __name__ == '__main__':
    if check_avx_support():
        print("CPU hỗ trợ AVX.")
    else:
        print("CPU không hỗ trợ AVX.")
