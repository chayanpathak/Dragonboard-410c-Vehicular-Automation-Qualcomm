import pygeoip
 
def main(): 
  geoip_city()
  print 'done'
                  
def geoip_city():
  path = './GeoLiteCity.dat'
  gic = pygeoip.GeoIP(path)
  print gic
  abc =  gic.record_by_addr('103.229.19.20')
  print abc['latitude']


if __name__ == '__main__':
  main()
