<!-- <img  height='200px' width='460px' src='https://raw.githubusercontent.com/reinanbr/dreams/main/img/logo.png'>
<br> -->
<div align='center'>
<h2>Rocketlc</h2>
<pgetting schedule launch rocket</p>
<a href='https://pypi.org/project/rocketlc/'><img src='https://img.shields.io/pypi/v/rocketlc'></a>

<img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/reinanbr/rocketlc?logo=codefactor">
<img src='https://img.shields.io/pypi/wheel/rocketlc'>
<br>


<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/rocketlc">
<img src='https://img.shields.io/github/last-commit/reinanbr/rocketlc'>
<br>

<!-- 
<img src='https://img.shields.io/badge/system-linux%20%7C%20deb-brightgreen'> -->

<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/reinanbr/rocketlc">

<img alt="PyPI - License" src="https://img.shields.io/pypi/l/rocketlc?color=orange">
<!-- redes sociais -->
<br/>
<a href='https://instagram.com/reysofts/'><img src='https://shields.io/badge/insta-reysofts-darkviolet?logo=instagram&style=flat'></a>
</div>

<br>

<hr>

## Instalation
```sh
pip3 install -U rocketlc
```

### getting launch
#### only site (rocketlaunch.live)

```py
from rocketlc import past_launchs as pl, future_launchs as fl

# search made on Dez 31 13:44 2022

#past launch's
pls = pl()

i=0
for l in pls['rockets']:
    print(f'[{i}]',l,'\n')
    i=i+1



#future launch's
fls = fl()

i=0
for l in fls['rockets']:
    print(f'[{i}]',l,'\n')
    i=i+1

```
result:
```sh

[0] {'mission': 'ISI EROS C-3', 'date_launch': 'DEC 30', 'time_launch': '07:38 AM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-4E, Vandenberg SFBCalifornia, United States ', 'series': 'B1061'} 

[1] {'mission': 'Shiyan-10-02', 'date_launch': 'DEC 29', 'time_launch': '04:43 AM ', 'name': 'Long March 3B ', 'empire': 'China', 'location': 'TBD, Xichang Satellite Launch CenterChina ', 'series': None} 

[2] {'mission': 'Starlink-67 (5-1)', 'date_launch': 'DEC 28', 'time_launch': '09:34 AM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-40, Cape Canaveral SFSFlorida, United States ', 'series': 'B1062'} 

[3] {'mission': 'Gaofen-11 04', 'date_launch': 'DEC 27', 'time_launch': '07:37 AM ', 'name': 'Long March 4B ', 'empire': 'China', 'location': 'LC-9, Taiyuan Satellite Launch CenterChina ', 'series': None} 

[4] {'mission': 'Pléiades-Neo 5 & 6', 'date_launch': 'DEC 21', 'time_launch': '01:47 AM ', 'name': 'Vega C ', 'empire': 'Arianespace', 'location': 'ELV, Guiana Space CentreFrench Guiana ', 'series': None} 

[5] {'mission': 'Starlink-66 (4-37)', 'date_launch': 'DEC 17', 'time_launch': '09:32 PM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'LC-39A, Kennedy Space CenterFlorida, United States ', 'series': 'B1058'} 

[6] {'mission': 'O3b mPower-1', 'date_launch': 'DEC 16', 'time_launch': '10:48 PM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-40, Cape Canaveral SFSFlorida, United States ', 'series': 'B1067'} 

[7] {'mission': 'SWOT', 'date_launch': 'DEC 16', 'time_launch': '11:46 AM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-4E, Vandenberg SFBCalifornia, United States ', 'series': 'B1071'} 

[8] {'mission': 'Shiyan-21', 'date_launch': 'DEC 16', 'time_launch': '06:17 AM ', 'name': 'Long March 11 ', 'empire': 'China', 'location': 'TBD, Xichang Satellite Launch CenterChina ', 'series': None} 

[9] {'mission': 'Yaogan-36 04', 'date_launch': 'DEC 14', 'time_launch': '06:25 PM ', 'name': 'Long March 2D ', 'empire': 'China', 'location': 'LC-3, Xichang Satellite Launch CenterChina ', 'series': None} 

[10] {'mission': 'Zhuque-2 Demo Flight', 'date_launch': 'DEC 14', 'time_launch': '09:30 AM ', 'name': 'Zhuque-2 ', 'empire': 'LandSpace', 'location': 'TBD, Jiuquan Satellite Launch CenterChina ', 'series': None} 

[11] {'mission': 'Galaxy-35 & Galaxy-36', 'date_launch': 'DEC 13', 'time_launch': '08:30 PM ', 'name': 'Ariane 5 ', 'empire': 'Arianespace', 'location': 'ELA-3, Guiana Space CentreFrench Guiana ', 'series': None} 

[12] {'mission': 'Shiyan-20A & Shiyan-20B', 'date_launch': 'DEC 12', 'time_launch': '08:22 AM ', 'name': 'Long March 4C ', 'empire': 'China', 'location': 'LA-4 / Pad 603 (SLS-2), Jiuquan Satellite Launch CenterChina ', 'series': None} 

[13] {'mission': 'ispace HAKUTO-R M1', 'date_launch': 'DEC 11', 'time_launch': '07:38 AM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-40, Cape Canaveral SFSFlorida, United States ', 'series': 'B1073'} 

[14] {'mission': 'Demo Flight', 'date_launch': 'DEC 09', 'time_launch': '06:35 AM ', 'name': 'Jielong-3 ', 'empire': 'China', 'location': 'Sea Launch, Yellow SeaChina ', 'series': None} 

[15] {'mission': 'OneWeb-15', 'date_launch': 'DEC 08', 'time_launch': '10:27 PM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'LC-39A, Kennedy Space CenterFlorida, United States ', 'series': 'Polar Orbit'} 

[16] {'mission': 'Gaofen-5 01A', 'date_launch': 'DEC 08', 'time_launch': '06:31 PM ', 'name': 'Long March 2D ', 'empire': 'China', 'location': 'LC-9, Taiyuan Satellite Launch CenterChina ', 'series': None} 

[17] {'mission': 'VHF Data Exchange System (VDES)', 'date_launch': 'DEC 07', 'time_launch': '01:15 AM ', 'name': 'Kuaizhou 11 ', 'empire': 'ExPace (China)', 'location': 'LA-4 / "Mobile Pad", Jiuquan Satellite Launch CenterChina ', 'series': None} 

[18] {'mission': 'Kosmos-2565', 'date_launch': 'NOV 30', 'time_launch': '09:10 PM ', 'name': 'Soyuz-2 ', 'empire': 'Russian Military', 'location': 'LC-43/4, Plesetsk CosmodromeRussia ', 'series': None} 

[19] {'mission': 'Shenzhou-15', 'date_launch': 'NOV 29', 'time_launch': '03:08 PM ', 'name': 'Long March 2F ', 'empire': 'China', 'location': 'TBD, Jiuquan Satellite Launch CenterChina ', 'series': None} 

[20] {'mission': 'GLONASS-M', 'date_launch': 'NOV 28', 'time_launch': '03:17 PM ', 'name': 'Soyuz-2 ', 'empire': 'Russian Military', 'location': 'LC-43/3, Plesetsk CosmodromeRussia ', 'series': None} 

[21] {'mission': 'Yaogan-36 03', 'date_launch': 'NOV 27', 'time_launch': '12:23 PM ', 'name': 'Long March 2D ', 'empire': 'China', 'location': 'LC-3, Xichang Satellite Launch CenterChina ', 'series': None} 

[22] {'mission': 'CRS2 SpX-26 (Dragon)', 'date_launch': 'NOV 26', 'time_launch': '07:20 PM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'LC-39A, Kennedy Space CenterFlorida, United States ', 'series': 'B1076'} 

[23] {'mission': 'Oceansat-3 (EOS-6)', 'date_launch': 'NOV 26', 'time_launch': '06:26 AM ', 'name': 'PSLV ', 'empire': 'ISRO', 'location': 'FLP, Satish Dhawan Space CentreIndia ', 'series': None} 

[24] {'mission': 'Eutelsat-10B', 'date_launch': 'NOV 23', 'time_launch': '02:57 AM ', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-40, Cape Canaveral SFSFlorida, United States ', 'series': 'B1049'} 

[0] {'mission': 'Oneweb-16', 'date_launch': 'JAN 08 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-40, Cape Canaveral SFSFlorida, United States ', 'series': 'Polar Orbit'} 

[1] {'mission': 'RS1 Flight 1', 'date_launch': 'JAN 09 2023', 'time_launch': '10:00 PM ', 'name': 'RS1 ', 'empire': 'ABL Space', 'location': 'LP-3C, Pacific Spaceport Complex - AlaskaAlaska, United States ', 'series': None} 

[2] {'mission': 'USSF-67', 'date_launch': 'JAN 10 2023', 'time_launch': '', 'name': 'Falcon Heavy ', 'empire': 'SpaceX', 'location': 'LC-39A, Kennedy Space CenterFlorida, United States ', 'series': 'B1064'} 

[3] {'mission': 'GPS III SV-06', 'date_launch': 'JAN 18 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-40, Cape Canaveral SFSFlorida, United States ', 'series': 'B1077'} 

[4] {'mission': 'IGS Radar-7', 'date_launch': 'JAN 25 2023', 'time_launch': '01:00 AM ', 'name': 'H-2A ', 'empire': 'JAXA', 'location': 'LA-Y1, Tanegashima Space CenterJapan ', 'series': None} 

[5] {'mission': 'O3b mPower-2', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'Pad TBD, Cape Canaveral / KSC TBDFlorida, United States ', 'series': 'Communications Satellite'} 

[6] {'mission': '"Virginia Is For Launch Lovers"', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Electron ', 'empire': 'Rocket Lab', 'location': 'Pad 0C (Rocket Lab LC-2), Mid-Atlantic Regional Spaceport (Wallops Island)Virginia, United States ', 'series': None} 

[7] {'mission': 'Intelsat-40e', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'Pad TBD, United States TBDUnited States ', 'series': 'Communications Satellite'} 

[8] {'mission': '"Good Luck, Have Fun"', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Terran 1 ', 'empire': 'Relativity Space', 'location': 'SLC-16, Cape Canaveral SFSFlorida, United States ', 'series': None} 

[9] {'mission': '"Start Me Up"', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'LauncherOne ', 'empire': 'Virgin Orbit', 'location': 'Cosmic Girl, 747-400, Spaceport CornwallUnited Kingdom ', 'series': None} 

[10] {'mission': 'VCLS Demo-2FB (ELaNa 43)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Alpha ', 'empire': 'Firefly', 'location': 'SLC-2W, Vandenberg SFBCalifornia, United States ', 'series': None} 

[11] {'mission': 'Starlink (2-4)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-4E, Vandenberg SFBCalifornia, United States ', 'series': 'B1063'} 

[12] {'mission': 'Starlink (2-2)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'Pad TBD, Cape Canaveral / KSC TBDFlorida, United States ', 'series': 'Series: SpaceX Starlink'} 

[13] {'mission': 'Starlink (5-3)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'Pad TBD, Cape Canaveral / KSC TBDFlorida, United States ', 'series': 'Series: SpaceX Starlink'} 

[14] {'mission': 'Starlink (2-6)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-4E, Vandenberg SFBCalifornia, United States ', 'series': 'Series: SpaceX Starlink'} 

[15] {'mission': 'Starlink (2-5)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-4E, Vandenberg SFBCalifornia, United States ', 'series': 'Series: SpaceX Starlink'} 

[16] {'mission': 'IRNSS-1J (NVS-01)', 'date_launch': 'JAN 2023', 'time_launch': '', 'name': 'PSLV ', 'empire': 'ISRO', 'location': 'FLP, Satish Dhawan Space CentreIndia ', 'series': None} 

[17] {'mission': 'ALOS-3', 'date_launch': 'FEB 12 2023', 'time_launch': '01:37 AM ', 'name': 'H-3 ', 'empire': 'JAXA', 'location': 'LA-Y2, Tanegashima Space CenterJapan ', 'series': None} 

[18] {'mission': 'Progress MS-22', 'date_launch': 'FEB 16 2023', 'time_launch': '', 'name': 'Soyuz-2 ', 'empire': 'Roscosmos', 'location': 'LC-31/6, Baikonur CosmodromeKazakhstan ', 'series': None} 

[19] {'mission': 'Crew-6', 'date_launch': 'FEB 19 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'LC-39A, Kennedy Space CenterFlorida, United States ', 'series': 'B1078'} 

[20] {'mission': 'Vulcan Flight 1', 'date_launch': 'FEB 25 2023', 'time_launch': '', 'name': 'Vulcan ', 'empire': 'United Launch Alliance (ULA)', 'location': 'SLC-41, Cape Canaveral SFSFlorida, United States ', 'series': None} 

[21] {'mission': 'WorldView Legion-1 & 2', 'date_launch': 'FEB 2023', 'time_launch': '', 'name': 'Falcon 9 ', 'empire': 'SpaceX', 'location': 'SLC-4E, Vandenberg SFBCalifornia, United States ', 'series': 'Flight-Proven Booster'} 
```


<hr>

#### only site (space schedule launch)
```py
import rocketlc.space_schedulle_launch as ssl

rcs = ssl.launchs()

i = 0
for rc in rcs:
    print(f'[{i}]',rc,'\n')
    i = i + 1
```
```sh
[0] {'name': 'Falcon 9 Block 5', 'mission': 'GPS III SV06Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Wed • Jan 18th', 'hour': ' 202312:24 PM UTC', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[1] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 2-4Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Thu • Jan 19th', 'hour': ' 20233:23 PM UTC', 'location': 'Vandenberg SFB, CA, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[2] {'name': 'Electron', 'mission': 'Virginia is for Launch LoversElectron', 'empire': 'Rocket Lab Ltd', 'date': 'Mon • Jan 23rd', 'hour': ' 202311:00 PM UTC', 'location': 'Wallops Island, Virginia, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[3] {'name': 'H-IIA 202', 'mission': 'IGS Radar-7H-IIA 202', 'empire': 'Mitsubishi Heavy Industries', 'date': 'Wed • Jan 25th', 'hour': ' 20231:00 AM UTC', 'location': 'Tanegashima, Japan', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[4] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 5-3Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Kennedy Space Center, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[5] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 2-2Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[6] {'name': 'Terran 1', 'mission': 'Good Luck, Have Fun (Maiden Flight)Terran 1', 'empire': 'Relativity Space', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[7] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 5-4Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[8] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 5-2Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[9] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 2-5Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Vandenberg SFB, CA, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[10] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 2-6Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Tue • Jan 31st', 'hour': ' 202312:00 AM UTC', 'location': 'Vandenberg SFB, CA, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[11] {'name': 'Falcon 9 Block 5', 'mission': 'Amazonas NexusFalcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Wed • Feb 1st', 'hour': ' 202312:00 AM UTC', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[12] {'name': 'Proton-M/Blok DM-03', 'mission': 'Elektro-L No.4Proton-M/Blok DM-03', 'empire': 'Khrunichev State Research and Production Space Center', 'date': 'Sun • Feb 5th', 'hour': ' 20239:12 AM UTC', 'location': 'Baikonur Cosmodrome, Republic of Kazakhstan', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[13] {'name': 'Soyuz 2.1a', 'mission': 'Progress MS-22 (83P)Soyuz 2.1a', 'empire': 'Russian Federal Space Agency (ROSCOSMOS)', 'date': 'Thu • Feb 9th', 'hour': ' 20236:15 AM UTC', 'location': 'Baikonur Cosmodrome, Republic of Kazakhstan', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[14] {'name': 'H3-22', 'mission': 'ALOS-3 (Maiden flight)H3-22', 'empire': 'Mitsubishi Heavy Industries', 'date': 'Sun • Feb 12th', 'hour': ' 20231:37 AM UTC', 'location': 'Tanegashima, Japan', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[15] {'name': 'Falcon 9 Block 5', 'mission': 'Crew-6Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Kennedy Space Center, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[16] {'name': 'Soyuz 2.1a', 'mission': 'Soyuz MS-23Soyuz 2.1a', 'empire': 'Russian Federal Space Agency (ROSCOSMOS)', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Baikonur Cosmodrome, Republic of Kazakhstan', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[17] {'name': 'Vulcan VC2S', 'mission': 'Peregrine lunar lander, Kuipersat-1 & 2 (Maiden flight)Vulcan VC2S', 'empire': 'United Launch Alliance', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': '/wp-content/uploads/default-1.png?ezimgfmt=rs%3Adevice%2Frscb1-2'} 

[18] {'name': 'Falcon 9 Block 5', 'mission': 'WorldView Legion 3 & 4Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[19] {'name': 'SSLV', 'mission': 'Microsat (Demo 2)SSLV', 'empire': 'Indian Space Research Organization', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Sriharikota, Republic of India', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[20] {'name': 'Falcon 9 Block 5', 'mission': 'Starlink Group 6-1Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[21] {'name': 'Falcon 9 Block 5', 'mission': 'WorldView Legion 1 & 2Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[22] {'name': 'Firefly Alpha', 'mission': 'Flight ThreeFirefly Alpha', 'empire': 'Firefly Aerospace', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Vandenberg SFB, CA, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[23] {'name': 'PSLV-XL', 'mission': 'Aditya-L1PSLV-XL', 'empire': 'Indian Space Research Organization', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Sriharikota, Republic of India', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[24] {'name': 'Falcon 9 Block 5', 'mission': 'OneWeb 1ZFalcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[25] {'name': 'Long March 4C', 'mission': 'Fengyun-3FLong March 4C', 'empire': 'China Aerospace Science and Technology Corporation', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Unknown Location', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[26] {'name': 'Falcon 9 Block 5', 'mission': 'Inmarsat-6 F2Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[27] {'name': 'Falcon 9 Block 5', 'mission': 'SARah 2 & 3Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Vandenberg SFB, CA, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[28] {'name': 'Starship', 'mission': 'Orbital Flight TestStarship', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'SpaceX Space Launch Facility, TX, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 

[29] {'name': 'Falcon 9 Block 5', 'mission': 'O3b mPower 3 & 4Falcon 9 Block 5', 'empire': 'SpaceX', 'date': 'Projected To LaunchFebruary', 'hour': ' 2023', 'location': 'Cape Canaveral, FL, USA', 'img_url': 'www.w3.org/2000/svg%22%20width=%221%22%20height=%221%22%3E%3C/svg%3E'} 


```