import requests
import pyodbc
import time
import Models as dm

apiKey = '?apiKey=s6UtbxtAFU43I_5v9LUPag28JmAB9W4OAxaWzoRlv78'
apiKey2 = '&apiKey=s6UtbxtAFU43I_5v9LUPag28JmAB9W4OAxaWzoRlv78'
baseURL = 'https://traffic.ls.hereapi.com'
pathFlow = '/traffic/6.2/'
pf2 = '/traffic/6.1/'
resource = 'flow/'
resource2 = 'flow.json'
format = 'json/'
format2 = '?corridor='
geo = '15/18200/11107'
# geo2 = '49.9918,19.9175;50.0114,19.9172;50.0362,19.9406;50'
# geo2 = urllib.parse.quote(geo2)
#username = 'python'
username = 'silax'
# password = 'polskaafryka1'
password = 'Polska0!'
database = 'Traffic_Pollution'
driver = '{ODBC Driver 17 for SQL Server}'
server = 'tcp:illidan.database.windows.net'

cords = {
    # 1
    0: {'c1': (49.99522, 19.91868), 'c2': (50.03618, 19.94048), 'c3': (50.03618, 19.94048)},
    # 2
    1: {'c1': (50.04938, 19.93378), 'c2': (50.05117, 19.94118), 'c3': (50.05801, 19.94687)},
    # 3
    2: {'c1': (50.04938, 19.93378), 'c2': (50.06547, 19.92456), 'c3': (50.07313, 19.93584)},
    # 4
    3: {'c1': (50.08722, 19.89122), 'c2': (50.09161, 19.93757), 'c3': (50.08551, 19.95662)},
    # 5
    4: {'c1': (50.08551, 19.95661), 'c2': (50.08523, 19.97242), 'c3': (50.08523, 19.97242)},
    # 6
    5: {'c1': (50.07442, 20.04612), 'c2': (50.07683, 20.05505), 'c3': (50.07890, 20.06292)}
}

# cords = {
# #1
# 0: {'c1': (49.995220, 19.918680), 'c2': (50.036189, 19.940488), 'c3': (50.036189, 19.940488)},
# #2
# 1: { 'c1': (50.049381, 19.933781), 'c2': (50.051173, 19.941184), 'c3': (50.058018, 19.946879)},
# #3
# 2: { 'c1': (50.049381, 19.933781), 'c2': (50.065479, 19.924562), 'c3': (50.073137, 19.935840)},
# #4
# 3: { 'c1': (50.087228, 19.891228), 'c2': (50.091618, 19.937579), 'c3': (50.085514, 19.956621)},
# #5
# 4: { 'c1': (50.085513, 19.956612), 'c2': (50.085238, 19.972425), 'c3': (50.085238, 19.972425)},
# #6
# 5: { 'c1': (50.074427, 20.046129), 'c2': (50.076838, 20.055055), 'c3': (50.078903, 20.062921)}
#          }

width = 50
areas = {0: {'from': 'Zakopiańska 198 30-435 Kraków', 'to': 'rondo Matecznego 30-524 Kraków', 'stationID': '401'},
         1: {'from': 'most Grunwaldzki 33-332 Kraków', 'to': 'Dietla 109-113 31-031 Kraków', 'stationID': '10121'},
         2: {'from': 'most Grunwaldzki 33-332 Kraków', 'to': 'Plac targowy Nowy Kleparz Długa 30-962 Kraków',
             'stationID': '400'},
         3: {'from': 'Rondo Ofiar Katynia 4869 31-342 Kraków',
             'to': 'Estakada Imienia Generała Tadeusza Rozwadowskiego 3001 Kraków',
             'stationID': '10123'},
         4: {'from': 'Aleja Generała Tadeusza Bora-Komorowskiego Kraków',
             'to': 'Estakada Imienia Generała Tadeusza Rozwadowskiego 3001 Kraków', 'stationID': '415'},
         5: {'from': 'aleja Solidarności 31-974 Kraków', 'to': 'rondo Czyżyńskie 31-982 Kraków', 'stationID': '402'}}


# def updateTraffic(description, point_code, direction, road_length, type_info, speed_capped, speedUncapped, free_flow,
#                   jam_factor, confidence, time_stamp):
#     '''One row - Add all columns roads to database'''
#     print(f'\nDescription: {description} \n'
#           f'Point code: {point_code}\n'
#           f'Direction: {direction}\n'
#           f'Measurement Length: {road_length}\n'
#           f'Type Info: {type_info}\n'
#           f'Speed Capped: {speed_capped}\n'
#           f'Speed Uncapped: {speedUncapped}\n'
#           f'Free Flow: {free_flow}\n'
#           f'Jam Factor: {jam_factor}\n'
#           f'Confidence: {confidence}\n'
#           f'Timestamp: {time_stamp}\n')
#
#     cursor.execute("""
#                     INSERT INTO TrafficFlow.dbo.Traffic_Data_Staging
#                     ([Point_Code], [Description], [Direction], [Road_Length], [Type_Info], [Speed_Capped], [Speed_Uncapped], [Free_Flow], [Jam_Factor], [Confidence], [Timestamp])
#                     VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
#                    description, point_code, direction, road_length,
#                    type_info, speed_capped, speedUncapped, free_flow, jam_factor, confidence, time_stamp
#                    )
#     cursor.commit()


def updateTraffic2(cnt, **kwargs):
    for key_, value_ in kwargs.items():
        print(f'{key_}: {value_}')
    cursor.execute("""
                        INSERT INTO Traffic_Pollution.dbo.Traffic_Data_Staging
                        ([Point_Code], [Description], [Direction], [Road_Length], 
                        [SubSegment], [Type_Info], [Speed_Capped], [Speed_Uncapped],
                         [Free_Flow], [Jam_Factor], [Confidence], [Timestamp], [Latitude1] , [Longtitude1]
                          ,[Latitude2], [Longtitude2], [Latitude3], [Longtitude3], [Width], [Area])
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   *[_value for k, _value in kwargs.items()], cords[cnt]['c1'][0], cords[cnt]['c1'][1],
                   cords[cnt]['c2'][0], cords[cnt]['c2'][1], cords[cnt]['c3'][0], cords[cnt]['c3'][1], width,
                   'From: ' + areas[cnt]['from'] + 'To: ' + areas[cnt]['to'] + 'To: ' + areas[cnt]['stationID'])
    cursor.commit()


if __name__ == '__main__':
    try:        
        for key, value in areas.items():
            print(key, value)
            geo2 = f'{cords[key]["c1"][0]},{cords[key]["c1"][1]};{cords[key]["c2"][0]},{cords[key]["c2"][1]};' \
                    f'{cords[key]["c3"][0]},{cords[key]["c3"][1]};{width}'
            apiURL = baseURL + pf2 + resource2 + format2 + geo2 + apiKey2
            print(apiURL)

            resp = requests.get(apiURL)
            json_data = resp.json()
            print(json_data)

            roads = dm.Roads(json_data)
            # print(roads.roads[0].road["FIS"][0]["FI'][0]['CF'][0])
            # print(roads.roads[0].road['FIS'][0]['FI'][0]['TMC'])

            i = iter(roads.roads)

            conn = pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            cursor = conn.cursor()

            if resp.status_code != 200:
                '''This means something went wrong.'''
                raise requests.ApiError(f'GET flow details status code: {resp.status_code}')
            # for key, value in areas.items():
            while (road := next(i, None)) is not None:
                updateTraffic2(key, **road.road)
            
    except pyodbc.Error as ex:
        print(ex)
    
    except Exception as er:
        print(er)



# Delay for 1 minute (60 seconds).
# updateTraffic(road.tmc.description, road.tmc.pointCode, road.tmc.direction, road.tmc.roadLength,
# road.currentFlow.typeInfo, road.currentFlow.speedCapped, road.currentFlow.speedUncapped,
# road.currentFlow.freeFlow, road.currentFlow.jamFactor, road.currentFlow.confidence, road.timeStamp
