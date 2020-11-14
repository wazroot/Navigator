
import urllib.parse
import requests


main_api = 'http://www.mapquestapi.com/directions/v2/route?'
key = '9sZAb89bM3HUkY13d0dHJf3JrwTCMDmi' 

print('===============================================================================')
while True:
    orig = input('Starting location?: ')
    if orig == 'quit' or orig == 'q':
        break
    dest = input('Destination?: ')
    if dest == 'quit' or dest == 'q':
        break
    met_imp = input('Metric or Imperial?: ')
    
    print('==========================================================================')   
    url = main_api + urllib.parse.urlencode({'key' : key, 'from' : orig, 'to' : dest})
    print('URL: ' + (url))
    json_data = requests.get(url).json()
    json_status = json_data['info']['statuscode']
    print('==========================================================================')
    
    #Shows the trip distance in km or miles and gas usage in liters or gallons
    #Also converting miles and gallons to kilometers and liters
    Kilometers = str('{:.2f}'.format((json_data['route']['distance']) * 1.61))
    Liters = str('{:.2f}'.format((json_data['route']['fuelUsed']) * 3.78))
    Miles = str('{:.2f}'.format((json_data['route']['distance'])))
    Gallons = str('{:.2f}'.format((json_data['route']['fuelUsed'])))
    
    #If json stat is ok continue forward
    if json_status == 0:
        
        print('================================================================')
        print('API status: ' + str(json_status) + ' = a succesfull API route call.')
        print('Directions from ' + (orig) + ' to ' + (dest))
        print('Trip duration: ' + (json_data['route']['formattedTime']))
        print('==============================================================')
        
        #Metric and imperial conditions for the user input
        if met_imp == 'Metric' or met_imp == 'metric':
            print('Kilometers/Miles: ' + Kilometers + ' kilometers')
            print('Fuel Used (Liters/Gallons): ' + Liters + ' liters')
        elif met_imp == 'Imperial' or met_imp == 'imperial':
            print('Kilometers/Miles: ' + Miles + ' Miles')
            print('Fuel Used (Liters/Gallons): ' + Gallons + ' Gallons')
        else:
            met_imp != 'Metric' or met_imp != 'metric' or met_imp !='Imperial' or met_imp != 'imperial'
            input('Type next time "Metric or Imperial", please! For now, press ENTER.')
            continue
        
        #prints extra data about the trip for user
        print('Tunnels:            ' + str('{:.0f}'.format((json_data['route']['hasTunnel']))))
        print('Highways:           ' + str('{:.0f}'.format((json_data['route']['hasHighway']))))
        print('Timed restrictions: ' + str('{:.0f}'.format((json_data['route']['hasTimedRestriction']))))
        print('============================================================')
        #print(json_data['route'])
        
        #prints trip route for the user
        for i in json_data['route']['legs'][0]['maneuvers']:
            if met_imp == 'Metric' or met_imp == 'metric':
                print((i['narrative']) + ' (' + str('{:.2f}'.format((i['distance']) * 1.61) + ' km)'))
            else:
                print((i['narrative']) + ' (' + str('{:.2f}'.format((i['distance'])) + ' miles)'))    
        print('============================================================\n')
    
    # Bad request
    elif json_status == 402:
        print('************************************************************')
        print('Status Code: ' + str(json_status) + '; Invalid user inputs for one or both locations.')
        print('************************************************************')
    else:
        print('************************************************************')
        print('For Status Code: ' + str(json_status) + '; Refer to:')
        print('https://developer.mapquest.com/documentation/directions-api/status-codes')
        print('************************************************************')