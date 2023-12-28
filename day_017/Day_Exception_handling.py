# Day_17: Exception_handling

# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
try:
    *nordic_countries,es,ru = names
    print(f'The Nordic countries include: {nordic_countries} ')
    print(f'ES: {es}, RU: {ru}')
except:
    print('unparking unsuccessful')