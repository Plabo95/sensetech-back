data = { 
 "SerNo": 100482, 
 "IMEI": "351579050616323", 
 "ICCID": "89610164556427000029", 
 "ProdId": 17, 
 "FW": "17.1.1.23", 
 "Records": [ 
 { 
 "SeqNo": 24866, 
 "Reason": 11, 
 "DateUTC": "2014-05-12 12:57:14", 
 "Fields": [ 
 { 
 "GpsUTC": "2014-05-12 09:26:39", 
 "Lat": -31.9535124, 
 "Long": 115.8241971, 
 "Alt": 18, 
 "Spd": 4, 
 "SpdAcc": 2, 
 "Head": 0, 
 "PDOP": 28, 
 "PosAcc": 12, 
 "GpsStat": 3,
 "FType": 0 
 }, 
 { 
 "DIn": 0, 
 "DOut": 0, 
 "DevStat": 2, 
 "FType": 2 
 }, 
 { 
 "AnalogueData": { 
 "4": 25, 
"1": 4144, 
"2": 30, 
"5": 3, 
"3": 1467 
 }, 
 "FType": 6 
 } 
 ] 
 }, 
 { 
 "SeqNo": 24867, 
 "Reason": 28, 
 "DateUTC": "2014-05-13 05:56:22",  "Fields": [] 
 }, 
 { 
 "SeqNo": 24868, 
 "Reason": 28, 
 "DateUTC": "2014-05-13 05:56:27",  "Fields": [] 
 }, 
 { 
 "SeqNo": 24869, 
 "Reason": 11, 
 "DateUTC": "2014-05-12 13:12:17",  "Fields": [ 
 { 
 "GpsUTC": "2014-05-12 09:26:39",  "Lat": -31.9535124, 
 "Long": 115.8241971, 
 "Alt": 18, 
 "Spd": 4, 
 "SpdAcc": 2, 
 "Head": 0, 
 "PDOP": 28, 
 "PosAcc": 12, 
 "GpsStat": 3, 
 "FType": 0 
 }, 
 { 
 "DIn": 0, 
 "DOut": 0, 
 "DevStat": 2, 
 "FType": 2 
 }, 
 { 
 "AnalogueData": { 
 "4": 25, 
"1": 4145, 
"2": 30, 
"5": 2, 
"3": 1504 
 }, 
 "FType": 6 
 } 
 ] 
 } 
 ] 
}
device = {
    'serNo': data['SerNo'],
    'imei': data['IMEI'],
    'iccid': data['ICCID'],
    'prodId': data['ProdId'],
    'fw': data['FW'],
}

records = data['Records']

for record in records:
    if record['Fields']:
        gps_data = record['Fields'][0]
        analogue_data = record['Fields'][2]['AnalogueData']
        record_sample = {
            "serNo": device['serNo'],   #Device foreignkey
            "seqNo": record['SeqNo'],   #Record sequence number
            "reason": record['Reason'],
            "dateUTC": record['DateUTC'],
            "lat": gps_data['Lat'],
            "long": gps_data['Long'],
            "alt": gps_data['Alt'],
            "voltage": analogue_data['1'],
            "temp": analogue_data['3'],
        }
        print(record_sample)
#print(records)
