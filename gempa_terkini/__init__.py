def ekstraksi_data():
    """
    Tanggal : 22 Maret 2022
    Waktu : 02:26:20 WIB
    MAgnitudo : 4.7
    Kedalaman : 10 km
    Lokasi : LS=8.21 BT=119.84
    Pusat Gempa : Pusat gempa berada di laut 32 km Barat Laut Labuan Bajo
    Dirasakan : Dirasakan (Skala MMI): III Labuan Bajo
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '22 Maret 2022'
    hasil['waktu'] = '02:26:20 WIB'
    hasil['magnitudo'] = 4.7
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 8.21, 'bt': 119.84}
    hasil['pusat gempa'] = 'Pusat gempa berada di laut 32 km Barat Laut Labuan Bajo'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Labuan Bajo'

    return hasil


def tampilkan_data(result):
    print('Gempa terkini berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi : LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")


# if __name__ == '__main__':
#    print('Aplikasi Utama')