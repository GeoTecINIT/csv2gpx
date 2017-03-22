import csv
import sys
from datetime import datetime

arg = 4


def csv2gpx(name_trk, file_name_gpx, file_name_csv, route_file):
    # Variable to change
    # name_trk = "Test"
    # file_name_gpx = "route"
    # file_name_csv = "location"
    # route_file = "C:\\Users\\DavidFrias\\Desktop\\"

    # CSV route file
    csvfile = open(route_file + file_name_csv + ".csv", "r")
    gpxfile = open(route_file + file_name_gpx + '.gpx', 'w')

    # read a CSV and establish the header (name of header)
    csv_reader = csv.reader(csvfile)
    header = csv_reader.next()
    lat = header.index("latitude")
    lon = header.index("longitude")
    alt = header.index("altitude")
    bearing = header.index("bearing")
    speed = header.index("speed")
    accuracy = header.index("accuracy")
    sensorTime = header.index("sensorTimestamp")
    systemTime = header.index("systemTimestamp")
    trk = ""
    coord_list = []
    for row in csv_reader:
        coord_list.append([row[lat], row[lon], row[alt]])
        time = datetime.fromtimestamp(long(row[systemTime])//1000).replace(microsecond=long(row[systemTime])%1000*1000)
        # create a segment track (point)
        trk += '<trkpt lat ="' + row[lat] + '" lon ="' + row[lon] + '">'
        trk += '\n'
        trk += '<ele>' + row[alt] + '</ele>'
        trk += '\n'
        trk+='<time>' + time.isoformat()[:-3]+'Z' + '</time>'
        trk+='\n'
        trk += '</trkpt>'
        trk += '\n'
    min_coord = min(coord_list)
    max_coord = max(coord_list)

    # metada GPX
    def metada_gpx():
        gpxfile.write('<metadata>')
        gpxfile.write('\n')
        gpxfile.write('<bounds minlat="' + min_coord[0] + '" minlon = "' + min_coord[1] + '" maxlat = "' + max_coord[
            0] + '" maxlon = "' + max_coord[1] + '"/>')
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
        gpxfile.write('<name>' + name_trk + '</name>')
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


if __name__ == "__main__":
    if len(sys.argv) != arg + 1:
        print("Error - You must put correctly the arguments")
        sys.exit(1)
    csv2gpx(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
