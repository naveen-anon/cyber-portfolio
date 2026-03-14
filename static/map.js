
const world = Globe()

(document.getElementById("globe"))

.globeImageUrl("//unpkg.com/three-globe/example/img/earth-dark.jpg")

.pointsData([
{lat:28.6,lng:77.2},
{lat:37.7,lng:-122.4},
{lat:35.6,lng:139.6}
])

.pointAltitude(0.1)

.pointColor(()=> "red")
