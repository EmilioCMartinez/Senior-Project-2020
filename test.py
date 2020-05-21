import automowy #Call the 'automowy' script---if saved as another name use that name instead
import json 
import time
import matplotlib.pyplot as plt



session = automowy.AutomowySession() #try to connect with the automower
mower = session.login('emilio.martinez99@gmail.com', 'Rippers99').find_mower() #to be able to access our SPECIFIC mower


json_data = (mower.query('status')) #load the data from the 'status' into the variable json_data
gps = dict(json_data) #Create a dictionary of the json data and call it a new varible, gps

'''
for i in range (13)): #Controls how many times the mower will start and pause and then when finished will park and tell the user it is parking (run loop 15 times)
   mower.control('start') #starts the mower
   time.sleep(15) 
   mower.control('pause') #tops the mower
   time.sleep(17) 
mower.control('park') #moewr parks in charging dock once the loop is done
print('Mower is done and parking')
'''
#Numbers for a wet run that show: WET, SATURATED, and DRY results
with open("/Users/EmilioMartinez/Desktop/Wet Run.txt",'r') as f: #open .txt file
    content = [line.rstrip('\n') for line in f] #remove the empty lines from the .txt file
    while("" in content): 
        content.remove("")  #Remove the '' from the .txt file 
        f.close() 
coords = (content[0:34]) #latitude and longitude coordinates are specified as the first to 35th elements of the data that was pulled from the .txt
float_lst = [float(x) for x in coords] #mkae the list of strings a list of floats
lat = float_lst[::2]
long = float_lst[1::2] 
lat_wet = [lat[i] for i in (0,1,2,3,6,9,10,12,13,14)] 
long_wet =[long[i] for i in (0,1,2,3,6,9,10,12,13,14)]
lat_sat = [lat[i] for i in (4,5,11)]
long_sat =[long[i] for i in (4,5,11)]
lat_dry = [lat[i] for i in (7,8)]
long_dry =[long[i] for i in (7,8)] 


im = plt.imread('/Users/EmilioMartinez/Desktop/IMG_4311.jpeg') #plot the image of the specific lawn the mower is on
implot = plt.imshow(im, extent=[3818.5145133870965,3818.52688661290,10444.618690714286, 10444.635209285714]) #set the image on the corners of the axes of the graph
wet=plt.scatter(lat_wet,long_wet, c='c', marker='o') 
sat=plt.scatter(lat_sat,long_sat, c='m', marker='o') 
dry=plt.scatter(lat_dry,long_dry, c='#EDB120', marker='o') 
plt.legend((wet, sat, dry),
           ('Wet Area', 'Saturated Area', 'Dry Area'),
           scatterpoints=1,
           loc='upper center',
           bbox_to_anchor=(0.5, -0.01),
           ncol=3,
           fontsize=8)
plt.title('Moisture Reading of Lawn', loc='center')
plt.axis('off')
plt.show()


