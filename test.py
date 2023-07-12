
import GenerateMeterData


IP_address = "192.168.203.54"
IP_port = "22"
user_login = "root"
user_password = "7CLcCt95"


GenerateMeterData.Set_Config(IP_address=IP_address, IP_port=IP_port, user_login=user_login, user_password=user_password)

lol = GenerateMeterData.MeterTable()

print(lol)


#
# # lol = {'MeterTable': {'MeterId': 100, 'ParentId': 0, 'TypeId': 5, 'Address': 'ТЕСТ', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 4, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1, 'DeviceIdx': 8}}
#
# MeterTable = {}
# lol2 = GenerateMeterData.ElConfig(MeterTable=lol.get('MeterTable'))
#
# print(lol2)



# # juornal = GenerateMeterData.JournalName.ElJrnlLimPwr

# lol3 = GenerateMeterData.ElMomentEnergy(Count_timestamp=10,
#                                          # MeterTable={'DeviceIdx': 34 ,'MeterId': 1034, 'ParentId': 0, 'TypeId': 42, 'Address': '1388', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 2, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1},
#                                          # ElConfig={'DeviceIdx': 34, 'Timestamp': 1511072360, 'Serial': '211500050411372', 'Model': 'TEST MODEL', 'IntervalPowerArrays': 30, 'DST': 1, 'Clock': 1, 'Tariff': 1, 'Reactive': 1, 'ActiveReverse': 1, 'ReactiveReverse': 1, 'CurrentCoeff': 58.07, 'VoltageCoeff': 94.72, 'MeterConst': 99.07}
#                                          Redefine_tag={"AngAB":None},
#                                          MeterTable= lol.get('MeterTable'),
#                                          ElConfig= lol2.get('ElConfig')
#
#                                          )
#
# print(lol3)
#
#
# lol3 = GenerateMeterData.ElDayEnergy(Count_timestamp=10,
#                                          # MeterTable={'DeviceIdx': 34 ,'MeterId': 1034, 'ParentId': 0, 'TypeId': 42, 'Address': '1388', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 2, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1},
#                                          # ElConfig={'DeviceIdx': 34, 'Timestamp': 1511072360, 'Serial': '211500050411372', 'Model': 'TEST MODEL', 'IntervalPowerArrays': 30, 'DST': 1, 'Clock': 1, 'Tariff': 1, 'Reactive': 1, 'ActiveReverse': 1, 'ReactiveReverse': 1, 'CurrentCoeff': 58.07, 'VoltageCoeff': 94.72, 'MeterConst': 99.07}
#                                          Redefine_tag={"AngAB":None},
#                                          MeterTable= lol.get('MeterTable'),
#                                          ElConfig= lol2.get('ElConfig')
#
#                                          )
#
# print(lol3)
#
# lol3 = GenerateMeterData.ElMomentQuality(Count_timestamp=10,
#                                          # MeterTable={'DeviceIdx': 34 ,'MeterId': 1034, 'ParentId': 0, 'TypeId': 42, 'Address': '1388', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 2, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1},
#                                          # ElConfig={'DeviceIdx': 34, 'Timestamp': 1511072360, 'Serial': '211500050411372', 'Model': 'TEST MODEL', 'IntervalPowerArrays': 30, 'DST': 1, 'Clock': 1, 'Tariff': 1, 'Reactive': 1, 'ActiveReverse': 1, 'ReactiveReverse': 1, 'CurrentCoeff': 58.07, 'VoltageCoeff': 94.72, 'MeterConst': 99.07}
#                                          Redefine_tag={"AngAB":None},
#                                          MeterTable= lol.get('MeterTable'),
#                                          ElConfig= lol2.get('ElConfig')
#
#                                          )
#
# print(lol3)
#
#
# lol3 = GenerateMeterData.ElArr1ConsPower(Count_timestamp=100,
#                                          # MeterTable={'DeviceIdx': 34 ,'MeterId': 1034, 'ParentId': 0, 'TypeId': 42, 'Address': '1388', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 2, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1},
#                                          # ElConfig={'DeviceIdx': 34, 'Timestamp': 1511072360, 'Serial': '211500050411372', 'Model': 'TEST MODEL', 'IntervalPowerArrays': 30, 'DST': 1, 'Clock': 1, 'Tariff': 1, 'Reactive': 1, 'ActiveReverse': 1, 'ReactiveReverse': 1, 'CurrentCoeff': 58.07, 'VoltageCoeff': 94.72, 'MeterConst': 99.07}
#                                          Redefine_tag={"AngAB":None},
#                                          MeterTable= lol.get('MeterTable'),
#                                          ElConfig= lol2.get('ElConfig')
#
#                                          )
#
# print(lol3)
#
# lol3 = GenerateMeterData.ElMonthConsEnergy(Count_timestamp=10,
#                                          # MeterTable={'DeviceIdx': 34 ,'MeterId': 1034, 'ParentId': 0, 'TypeId': 42, 'Address': '1388', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 2, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1},
#                                          # ElConfig={'DeviceIdx': 34, 'Timestamp': 1511072360, 'Serial': '211500050411372', 'Model': 'TEST MODEL', 'IntervalPowerArrays': 30, 'DST': 1, 'Clock': 1, 'Tariff': 1, 'Reactive': 1, 'ActiveReverse': 1, 'ReactiveReverse': 1, 'CurrentCoeff': 58.07, 'VoltageCoeff': 94.72, 'MeterConst': 99.07}
#                                          Redefine_tag={"AngAB":None},
#                                          MeterTable= lol.get('MeterTable'),
#                                          ElConfig= lol2.get('ElConfig')
#
#                                          )
#
# print(lol3)

# lol3 = GenerateMeterData.ElArr1ConsPower(Count_timestamp=1675,
#                                          MeterTable={'DeviceIdx': 2 ,'MeterId': 2, 'ParentId': 0, 'TypeId': 42, 'Address': '1388', 'ReadPassword': '373737373737', 'WritePassword': '373737373737', 'InterfaceId': 2, 'InterfaceConfig': '9600,8n1', 'RTUObjType': 1, 'RTUFeederNum': 1, 'RTUObjNum': 1},
#                                          ElConfig={'DeviceIdx': 2, 'Timestamp': 1511072360, 'Serial': '211500050411372', 'Model': 'TEST MODEL', 'IntervalPowerArrays': 30, 'DST': 1, 'Clock': 1, 'Tariff': 1, 'Reactive': 1, 'ActiveReverse': 1, 'ReactiveReverse': 1, 'CurrentCoeff': 58.07, 'VoltageCoeff': 94.72, 'MeterConst': 99.07},
#                                          Redefine_tag={"AngAB":None}
#                                          # MeterTable= lol.get('MeterTable'),
#                                          # ElConfig= lol2.get('ElConfig')
#
#                                          )