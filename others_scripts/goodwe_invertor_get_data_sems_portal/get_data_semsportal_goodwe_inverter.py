'''
NAVOD:
- mas 2 moznosti ako si vytahovat data, su tam 2 sekcie step 1 a step 2 vyber si ktora je lepsia pre teba
        - tato prva metoda je lepsia ked mas multi-inverter tak si vies vytiahnut pre ktory potrebujes lebo tato
        metoda vytahuje uplne uplne vsetko co ponuka Goodwe sems portal API, priamo cez dumped json,
        vies vsetky surove data si vytiahnut zo slovnika, vid. step 1 sekcia koment nizsie
                e.g. na vyskusanie si mozes editovat riadok 55 ak spustis skript vytvori sa ti subor
                inverter_data_dumped.json, v nom si pozries ake data potrebujes, a potom si ich uz vies len vypisat
                cez zavolanie kluca z dictionary  napr. ak chcem hodnotu kpi -> month_generation tak volam:
                 json_dict_object['kpi']['month_generation'])
                 daju sa volat uz aj preddefinovane funkcie napr na ziskanie teploty,  def get_inverter_temperature(self) -> List[float]:

        - tato druha metoda jednoduchsia asi pre teba, je lepsia ked mas single-inverter,
        priamo cez object vies volat funkcie goodwe ktore su uz predprogramovane na vytiahnutie konkretnej hodnoty
          vid step 2 koment sekcia nizsie, ake vsetky mozne metody goodwe obsahuje, vies najst v __init.py__ kniznice
          pygoodwe, napr funkcie ako: def getVoltage(self) -> float: #type: ignore, def get_total_income(self) -> float:
          def get_inverter_temperature(self) -> List[float]:
          poznamka: tie funkcie by mali fungovat aj na multi-inverter ked nahodou potrebujes, pouzitie rovnake
          len to pouzijes tie funkcie v step 1.
                e.g. riadok 78, 80, 81 tam mas ako som si vytahoval data priklady, mozes sa skusat pobavit
'''

#goodWe inverter SEMS sortal get data script @Stano Tischler 2023
import config_semsportal as config
import base64
import json
from functools import lru_cache
from pygoodwe import SingleInverter
from pygoodwe import API


#decode your password, the one that is printed
pswd = config.sems_portal_credentials['gw_password']
pswd_bytes = pswd.encode('ascii')
pswd_encoded = base64.b64encode(pswd_bytes).decode('ascii')


#start of script, check print config
print('-------------- START "get_data_semsportal_goodwe_inverter.py" script -------------\n')
print('ID is: ' + config.sems_portal_credentials['gw_station_id'])
print('Account is: ' + config.sems_portal_credentials['gw_account'])
print('Pswd is : ' + pswd_encoded)
print('City is: ' + config.sems_portal_credentials['city'])


#step 1: dumps the all inverter raw data to the json file, used mainly if you have Stanley Multi-Inverter
goodwe = API(
        system_id=config.sems_portal_credentials['gw_station_id'],
        account=config.sems_portal_credentials['gw_account'],
        password=config.sems_portal_credentials['gw_password'],
        )
goodwe.getCurrentReadings()
json_object = json.dumps(goodwe.data, indent=4)
json_dict_object = json.loads(json_object)
print('\nStep 1: json dump of all data will be written in "inverter_data_dumped.json" file!')
with open("inverter_data_dumped.json", "w") as outfile:
        outfile.write(json_object)
#TODO: edit here according to your needs
print('Example how to get month generated raw data from dumped json? The value is: '
      + str(json_dict_object['kpi']['month_generation']))


#step 2: dumps the concrete data for Single Inverter, used mainly if you have Stanley Single-Inverter
@lru_cache()
def get_single_inverter_data():
    print("\nStep 2: getting single inverter data...")
    goodwe = SingleInverter(
        system_id=config.sems_portal_credentials['gw_station_id'],
        account=config.sems_portal_credentials['gw_account'],
        password=config.sems_portal_credentials['gw_password'],
            )
    goodwe.getCurrentReadings()
    return goodwe

inverter = get_single_inverter_data()
#print(f"Available fields in data: {inverter.data.keys()}")
#method 1 how to get data via specification of particular dictionary keys
print('Capacity is: ', end="")
print(json.dumps(inverter.data.get('inverter').get('capacity'), indent=2))

#method 2, via calling the pre-coded methods of pygoodwe lib
print(f"Voltage is: {inverter.getVoltage()}")
print(f"Temperature is: {inverter.get_inverter_temperature()}")
print(f"Daily income is: {inverter.get_day_income()}")
print(f"State of charge of battery is: {str(inverter.get_batteries_soc())}")


#end of script
print('\n-------------- END "get_data_semsportal_goodwe_inverter.py script" -------------')