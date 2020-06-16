# Generated by parse_spec.py
# Do not modify
import numpy as np

header = [
    ("cFileType", "S16"),
    ("cCountry", "S30"),
    ("cProvince", "S20"),
    ("cStation", "S40"),
    ("cStationNumber", "S10"),
    ("cRadarType", "S20"),
    ("cLongitude", "S16"),
    ("cLatitude", "S16"),
    ("lLongitudeValue", "i4"),
    ("lLatitudeValue", "i4"),
    ("lHeight", "i4"),
    ("sMaxAngle", "i2"),
    ("sOptAngle", "i2"),
    ("ucSYear1", "B"),
    ("ucSYear2", "B"),
    ("ucSMonth", "B"),
    ("ucSDay", "B"),
    ("ucSHour", "B"),
    ("ucSMinute", "B"),
    ("ucSSecond", "B"),
    ("ucTimeFrom", "B"),
    ("ucEYear1", "B"),
    ("ucEYear2", "B"),
    ("ucEMonth", "B"),
    ("ucEDay", "B"),
    ("ucEHour", "B"),
    ("ucEMinute", "B"),
    ("ucESecond", "B"),
    ("ucScanMode", "B"),
    ("ulSmilliSecond", "u4"),
    ("usRHIA", "u2"),
    ("sRHIL", "i2"),
    ("sRHIH", "i2"),
    ("usEchoType", "u2"),
    ("usProdCode", "u2"),
    ("ucCalibration", "B"),
    ("remain1", "3B"),
    ("remain2", "660B"),
    ("test", "2B"),
    ("lAntennaG", "i4"),
    ("lPower", "i4"),
    ("lWavelength", "i4"),
    ("usBeamH", "u2"),
    ("usBeamL", "u2"),
    ("usPolarization", "u2"),
    ("usLogA", "u2"),
    ("usLineA", "u2"),
    ("usAGCP", "u2"),
    ("usFreqMode", "u2"),
    ("usFreqRepeat", "u2"),
    ("usPPPPulse", "u2"),
    ("usFFTPoint", "u2"),
    ("usProcessType", "u2"),
    ("ucClutterT", "B"),
    ("cSidelobe", "c"),
    ("ucVelocityT", "B"),
    ("ucFilderP", "B"),
    ("ucNoiseT", "B"),
    ("ucSQIT", "B"),
    ("ucIntensityC", "B"),
    ("ucIntensityR", "B"),
    ("ucCalNoise", "B"),
    ("ucCalPower", "B"),
    ("ucCalPulseWidth", "B"),
    ("ucCalWorkFreq", "B"),
    ("ucCalLog", "B"),
    ("remain3", "92B"),
    ("test2", "B"),
    ("liDataOffset", "u4"),
]

header_dtype = np.dtype(header)

scan_param = [
    ("usMaxV", "u2"),
    ("usMaxL", "u2"),
    ("usBindWidth", "u2"),
    ("usBinNumber", "u2"),
    ("usRecordNumber", "u2"),
    ("usArotate", "u2"),
    ("usPrf1", "u2"),
    ("usPrf2", "u2"),
    ("usSpulseW", "u2"),
    ("usAngle", "i2"),
    ("cSweepStatus", "B"),
    ("cAmbiguousp", "B"),
]

scan_param_dtype = np.dtype(scan_param)

data = [("Z", "500i2"), ("V", "500i2"), ("W", "500i2")]

data_dtype = np.dtype(data)
