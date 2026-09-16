README_stockholm_daily_mean_temperature.txt

This file describes the contents of the file 
'stockholm_daily_mean_temperature_1756_2017.txt', which contains daily mean
temperatures at the Stockholm Old Astronomical Observatory (59.35N, 18.05E)
1756-2017.

Contact person:

Anders Moberg
Department of Physical Geography
Stockholm University
SE-10691 Stockholm, Sweden
anders.moberg@natgeo.su.se

2018-02-06


References:

Moberg A, Bergström H, Ruiz Krigsman J, Svanered O. 2002: Daily air temperature 
and pressure series for Stockholm (1756-1998). Climatic Change 53: 171-212

Moberg A, Alexandersson H, Bergström H, Jones PD. 2003: Were Southern Swedish 
summer temperatures before 1860 as warm as measured? 
Int. J. Climatol. 23: 1495-1521

Project:

IMPROVE - Improved Understanding of Past Climatic Variability from Early Daily 
European Instrumental Sources. EU 4th Framework Programme. Contract
ENV4-CT97-0511. 1998-1999. Co-ordinator: Dario Camuffo, Consiglio Nazionale
delle Ricerche, Istituto di Scienze dell'Atmosfera e del Clima, Padova, Italy.
PI at Stockholm University: Anders Moberg

Original data sources:

1756-1858: Archive of the Royal Swedish Academy of Sciences
1859-now:  Swedish Meteorological and Hydrological Institute (SMHI)

Data for 1756-1838 were digitized at the SMHI. Data for 1839-1960 were digitized
within IMPROVE. Data for 1961-2012 were provided digitally by the SMHI.
Data for 2013 and later are obtained from SMHI Öppna Data:
http://opendata-download-metobs.smhi.se/explore/#

The digitized observations are found in the directory ~/temperature/daily/raw.

--------------------------------------------------------------------------------

Contents of the file 'stockholm_daily_mean_temperature_1756_2017.txt':

Daily temperature data for Stockholm Old Astronomical Observatory 
1 Jan 1756 -  31 Dec 2017.


column		data

1-3          Year, month, day
4            Daily average temperature according to observations. 
               Unit: C, Missing values: -999.0
5            Daily average temperature after homogenization and
               with gaps filled in using data from Uppsala. 
	       (see Moberg et al. 2002)
6            Daily average temperatures after adjustment before September 1858 
	       for a supposed warm bias of May-August temperatures.
	       (see Moberg et al. 2003)
7            Data id no. meaning data from:
               1=Stockholm
               2=Uppsala (ajusted to represent Stockholm)
               3=Stockholm, automatic station (used from 2013 onwards)

Period       Typical number of observations per day, 
	     used in calclulation of daily mean temp.
1757-1760    2
1761-1858    3
1859-1946    3 (& Tmin in summer)
1947-2017    3 & Tmin & Tmax

During 1756-1875 the thermometer was hung in the free air outside a north-facing
window on the second floor of the old astronomical observatory building in
Stockholm. No detailed description is available on this site. 

During 1876-1960 the thermometer was placed outside a north-facing window
on the first floor of the old astronomical observatory building in Stockholm.
A window-screeen was in use since 1878.

During 1961- summer 2006 the thermometer was placed in a SMHI-screen 
(Stevenson-type screen) about ten metres north-east of the former position.

Since summer 2006, a platinum resistance thermometer in a modern cylindrical 
screen close to the SMHI-screen replaced the mercury thermometer in the
SMHI-screen.

From January 2013 onwards, the data used here are based on observations recorded
at the automatic station, which is of the same type as the manually observed
resistance thermometer.

The following adjustments are made to the data column 5:

17560403-17561031	The observed temperatures during this period are judged
			to be too high, and of poor quality. They have been
			replaced with data extrapolated from Uppsala through
			linear regression. 

17630225-17630228	No observations were made. 
			Daily temperatures have been extrapolated from Uppsala.

18190801-18250113	Correction by -0.7 C. 
			Incorrect thermometer probably used.

18700111-20171231	Correction for urban heat island trend 
			and other inhomogeneities.

The following additional adjustments are made to the data column 6:

1756-1858, May:  day 1-4:   0.0 C, day 5-9: -0.1 C, day 10-13: -0.2 C, 
		 day 14-18: -0.3 C, day 19-22: -0.4 C, day 23-27: -0.5 C, 
		 day 28-31: -0.6 C. 
           Jun:  day 1-30: -0.7 C
           Jul:  day 1-31: -0.7 C
           Aug:  day 1-4:  -0.6 C, day 5-9: -0.5 C, day 10-13: -0.4 C, 
		 day 14-18: -0.3 C, day 19-22: -0.2 C, day 23-27: -0.1 C, 
		 day 28-31: 0.0 C.

This gives an average adjustment by -0.3 C both  May and August and -0.7 C for
June and July. This adjustment is in agreement with conclusions drawn by Moberg
et al. (2003), but have been determined on an ad hoc basis rather than from a
strict statistical analysis.
