readings=[{'site':'LAB-A','fuel':29,'temperature':35},{'site':'LAB-B','fuel':30,'temperature':40},{'site':'LAB-C','fuel':70,'temperature':41},{'site':'LAB-D','fuel':-1,'temperature':25}]
alerts=[];invalid=[]
for r in readings:
 if not 0<=r['fuel']<=100:
  invalid.append(r['site']);continue
 if r['fuel']<30:alerts.append((r['site'],'LOW_FUEL'))
 if r['temperature']>40:alerts.append((r['site'],'HIGH_TEMPERATURE'))
assert alerts==[('LAB-A','LOW_FUEL'),('LAB-C','HIGH_TEMPERATURE')]
assert invalid==['LAB-D']
print('Synthetic readings:',readings)
print('Alerts:',alerts,'; rejected invalid data:',invalid)
print('PASS: threshold boundaries and invalid fuel values handled correctly')
