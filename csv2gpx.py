import csv
import json

# Variable to change
nameTrk = "Test"
file_name_gpx = "route"
file_name_csv = "location"
route_file = "C:\\Users\\DavidFrias\\Desktop\\"

# CSV route file
file = open(route_file + file_name_csv + ".csv", "r")
gpxfile = open(route_file + file_name_gpx + '.gpx', 'w')

# read a CSV and establish the header (name of header)
csvReader = csv.reader(file)
header = csvReader.next()
lat = header.index("latitude")
lon = header.index("longitude")
alt = header.index("altitude")
bearing = header.index("bearing")
speed = header.index("speed")
accuracy = header.index("accuracy")
sensorTime = str(header.index("sensorTimestamp"))
systemTime = header.index("systemTimestamp")
trk = ""
coordList = []
for row in csvReader:
    coordList.append([row[lat], row[lon], row[alt]])
    # create a segment track (point)
    trk += '<trkpt lat ="' + row[lat] + '" lon ="' + row[lon] + '">'
    trk += '\n'
    trk += '<ele>' + row[alt] + '</ele>'
    trk += '\n'
    # trk+='<time>' + sensorTime + '</time>'
    # trk+='\n'
    trk += '</trkpt>'
    trk += '\n'
minCoord = min(coordList)
maxCoord = max(coordList)

# metada GPX
def metada_gpx():
    gpxfile.write('<metadata>')
    gpxfile.write('\n')
    gpxfile.write('<bounds minlat="' + minCoord[0] + '" minlon = "' + minCoord[1] + '" maxlat = "' + maxCoord[
        0] + '" maxlon = "' + maxCoord[1] + '"/>')
    gpxfile.write('\n')
    gpxfile.write('</metadata>')
    gpxfile.write('\n')


# header GPX
def header_gpx():
    gpxfile.write('<?xml version="1.0" encoding="UTF-8"?>')
    gpxfile.write('\n')
    gpxfile.write(
        '<gpx version="1.1" creator="David Frias - dfrias88@gmail.com" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">')
    gpxfile.write('\n')
    metada_gpx()

# create a track GPX
def trk_gpx():
    gpxfile.write('<trk>')
    gpxfile.write('\n')
    gpxfile.write('<name>' + nameTrk + '</name>')
    gpxfile.write('\n')
    gpxfile.write('<cmt/>')
    gpxfile.write('\n')
    gpxfile.write('<trkseg>')
    gpxfile.write('\n')

# Establish header GPX
header_gpx()
trk_gpx()
# segment track (points)
gpxfile.write(trk)

# close file GPX
def finish_header_gpx():
    gpxfile.write('</gpx>')

# close track GPX
def finish_trk_gpx():
    gpxfile.write('</trkseg>')
    gpxfile.write('\n')
    gpxfile.write('</trk>')
    gpxfile.write('\n')

finish_trk_gpx()
finish_header_gpx()

print "File created!!"
