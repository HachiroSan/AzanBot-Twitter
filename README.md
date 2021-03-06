<!-- PROJECT LOGO -->
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br>
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/subahanii/COVID19-tracker/issues)
<br />
<p align="center">
    <a href="https://github.com/HachiroSan/AzanBot-Twitter">
    <img src="prayer/images/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">AzanBot-Twitter</h3>

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

## Installation
You need to set your system time to GMT +8 timezone (**IMPORTANT**).
```bash
sudo timedatectl set-timezone Asia/Kuala_Lumpur
```
You also need to have Python 3. (Project developed on Python 3.9.2)

1. Clone the repository

```bash
git clone https://github.com/HachiroSan/AzanBot-Twitter.git
```

2. Install the required package from requirements.txt using pip before proceeding.

```bash
pip install -r requirements.txt
```

## Usage
1. Open config.ini 
2. Update Twitter APIs (Default for reference)
3. Specify the prayer zone, refer to zone code below
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

4. Edit notification message to your liking using python formatting. Refer string variable given below
```
{timestamp_12hr} = 12-hours timestamp e.g 8:30 PM
{timestamp_24hr} = 24-hours timestamp e.g 20:30
{prayer} = current prayer
``` 
3. Run script
```
python3 app.py
```
## Operating System
Application works for both Linux and Windows. (Tested on Ubuntu 20.04 and Windows 10 21H1)

For Linux, if you want to host multiple bots, use tmux or screen for better management. 

## Troubleshoot
All activities will be logged in debug.log file. If there is any error. Feel free to contact me by providing me the log or try to troubleshoot yourself.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
