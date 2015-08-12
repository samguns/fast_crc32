# -*- coding: utf-8 -*-

__author__ = 'gang.wang'


def Crc32Fast(crc, data):
    CrcTable = [0x00000000, 0x04C11DB7, 0x09823B6E, 0x0D4326D9, 0x130476DC, 0x17C56B6B, 0x1A864DB2, 0x1E475005,
                0x2608EDB8, 0x22C9F00F, 0x2F8AD6D6, 0x2B4BCB61, 0x350C9B64, 0x31CD86D3, 0x3C8EA00A, 0x384FBDBD]

    crc = crc ^ data

    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]
    crc = (crc << 4) ^ CrcTable[(crc >> 28) & 0x0F]

    return crc

if __name__ == "__main__":
    print "crc:", hex(Crc32Fast(0xFFFFFFFF, 0x12345678) & 0xffffffff)