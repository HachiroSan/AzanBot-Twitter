<!-- PROJECT LOGO -->
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br>
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/subahanii/COVID19-tracker/issues)
<br />
<p align="center">
    <a href="https://github.com/HachiroSan/AzanBot-V2">
    <img src="/img/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">AzanBot-V2</h3>

  <p align="center">
    AzanBot is a Malaysia-based Islamic prayer alert bot for Twitter. 
    Data source from Jabatan Kemajuan Islam Malaysia. 
    <br />
    <br />
    <a href="https://twitter.com/dailyprayerKTN">Demo</a>
    ·
    <a href="#Installation">Installation</a>
    ·
    <a href="#Usage">Usage</a>
    ·
    <a href="#Operating-System">Operating System</a>
  </p>
</p>

## Features

- The schedule will now be updated every day at 12:01 AM to ensure the most accurate and up-to-date prayer times.

- We have also implemented a new API to enhance the reliability and precision of the schedule. Enjoy the updated feature and let us know your feedback."

- New cli commands that is far more easier to run

- New user interface utilized using Rich libray.

- Now, there is no need to change system timezone into Malaysia timezone.

<p align="center">
<img src="/img/terminal-preview.png" alt="Logo" width="600" height="400">
</p>

## Installation

1. Clone the repository

```bash
git clone https://github.com/Muhd-Farhad/AzanBot-V2.git
```

2. Install the required package from requirements.txt using pip before proceeding.

```bash
pip install -r requirements.txt
```

## Usage
1. Open config.ini 
2. Update Twitter APIs (Default for reference)
3. Run cli.py. You can either specify city. state or timezone

```
python3 cli.py -t Kuantan
```
For the zone, refer to zone code below

```python
# JOHOR
JHR01 - PULAU AUR DAN PULAU PEMANGGIL
JHR02 - JOHOR BAHRU, KOTA TINGGI, MERSING
JHR03 - KLUANG, PONTIAN
JHR04 - BATU PAHAT, MUAR, SEGAMAT, GEMAS JOHOR

# KEDAH
KDH01 - KOTA SETAR, KUBANG PASU, POKOK SENA (DAERAH KECIL)
KDH02 - KUALA MUDA, YAN, PENDANG
KDH03 - PADANG TERAP, SIK
KDH04 - BALING
KDH05 - BANDAR BAHARU, KULIM
KDH06 - LANGKAWI
KDH07 - PUNCAK GUNUNG JERAI

# KELANTAN
KTN01 - BACHOK, KOTA BHARU, MACHANG, PASIR MAS, PASIR PUTEH, TANAH MERAH, TUMPAT, KUALA KRAI, MUKIM CHIKU
KTN03 - GUA MUSANG (DAERAH GALAS DAN BERTAM), JELI, JAJAHAN KECIL LOJING

# MELAKA
MLK01 - SELURUH NEGERI MELAKA

# NEGERI SEMBILAN
NGS01 - TAMPIN, JEMPOL
NGS02 - JELEBU, KUALA PILAH, PORT DICKSON, REMBAU, SEREMBAN

# PAHANG
PHG01 - PULAU TIOMAN
PHG02 - ROMPIN, PEKAN, MUADZAM SHAH DAN KUANTAN
PHG03 - MARAN, CHENOR, TEMERLOH, BERA, JENGKA DAN JERANTUT
PHG04 - BENTONG, RAUB DAN LIPIS
PHG05 - BUKIT TINGGI, GENTING SEMPAH, DAN JANDA BAIK
PHG06 - CAMERON HIGHLANDS, BUKIT FRASER GENTINGDAN GENTING HIGHLANDS

# PERLIS
PLS01 - KANGAR, PADANG BESAR, ARAU

# PULAU PINANG 
PNG01 - SELURUH NEGERI PULAU PINANG

# PERAK
PRK01 - TAPAH, SLIM RIVER, TANJUNG MALIM
PRK02 - KUALA KANGSAR, SG. SIPUT , IPOH, BATU GAJAH, KAMPAR
PRK03 - LENGGONG, PENGKALAN HULU, GRIK
PRK04 - TEMENGOR, BELUM
PRK05 - KG GAJAH, TELUK INTAN, BAGAN DATUK, SERI ISKANDAR, BERUAS, PARIT, LUMUT, SITIAWAN, PULAU PANGKOR
PRK06 - SELAMA, TAIPING, BAGAN SERAI, PARIT BUNTAR
PRK07 - BUKIT LARUT

# SABAH
SBH01 - BAHAGIAN SANDAKAN (TIMUR), BUKIT GARAM, SEMAWANG, TEMANGGONG, TAMBISAN, BANDAR SANDAKAN, SUKAU
SBH02 - BELURAN, TELUPID, PINANGAH, TERUSAN, KUAMUT, BAHAGIAN SANDAKAN (BARAT)
SBH03 - LAHAD DATU, SILABUKAN, KUNAK, SAHABAT, SEMPORNA, TUNGKU, BAHAGIAN TAWAU (TIMUR)
SBH04 - BANDAR TAWAU, BALONG, MEROTAI, KALABAKAN, BAHAGIAN TAWAU (BARAT)
SBH05 - KUDAT, KOTA MARUDU, PITAS, PULAU BANGGI, BAHAGIAN KUDAT
SBH06 - GUNUNG KINABALU
SBH07 - KOTA KINABALU, RANAU, KOTA BELUD, TUARAN, PENAMPANG, PAPAR, PUTATAN, BAHAGIAN PANTAI BARAT
SBH08 - PENSIANGAN, KENINGAU, TAMBUNAN, NABAWAN, BAHAGIAN PENDALAMAN (ATAS)
SBH09 - BEAUFORT, KUALA PENYU, SIPITANG, TENOM, LONG PA SIA, MEMBAKUT, WESTON, BAHAGIAN PENDALAMAN (BAWAH)

# SELANGOR
SGR01 - GOMBAK, PETALING, SEPANG, HULU LANGAT, HULU SELANGOR, S.ALAM
SGR02 - KUALA SELANGOR, SABAK BERNAM
SGR03 - KLANG, KUALA LANGAT

# SARAWAK
SWK01 - LIMBANG, LAWAS, SUNDAR, TRUSAN
SWK02 - MIRI, NIAH, BEKENU, SIBUTI, MARUDI
SWK03 - PANDAN, BELAGA, SUAI, TATAU, SEBAUH, BINTULU
SWK04 - SIBU, MUKAH, DALAT, SONG, IGAN, OYA, BALINGIAN, KANOWIT, KAPIT
SWK05 - SARIKEI, MATU, JULAU, RAJANG, DARO, BINTANGOR, BELAWAI
SWK06 - LUBOK ANTU, SRI AMAN, ROBAN, DEBAK, KABONG, LINGGA, ENGKELILI, BETONG, SPAOH, PUSA, SARATOK
SWK07 - SERIAN, SIMUNJAN, SAMARAHAN, SEBUYAU, MELUDAM
SWK08 - KUCHING, BAU, LUNDU, SEMATAN
SWK09 - ZON KHAS (KAMPUNG PATARIKAN)

# TERENGGANU
TRG01 - KUALA TERENGGANU, MARANG, KUALA NERUS
TRG02 - BESUT, SETIU
TRG03 - HULU TERENGGANU
TRG04 - DUNGUN, KEMAMAN

# WILAYAH PERSEKUTUAN
WLY01 - KUALA LUMPUR, PUTRAJAYA
WLY02 - LABUAN
```

## Operating System
Application works for both Linux and Windows. (Tested on Ubuntu 20.04 and Windows 10 21H1)

For Linux server, use tmux or screen for better management. 

## Troubleshoot
All activities will be logged in logs.txt file. If there is any error. Feel free to contact me by providing me the log or try to troubleshoot yourself.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Credits
Waktu Solat API - https://github.com/zaimramlan/waktu-solat-api
JAKIM E-Solat 
