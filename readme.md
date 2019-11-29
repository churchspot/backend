```
 
 ██████╗  █████╗  ██████╗██╗  ██╗███████╗███╗   ██╗██████╗ 
 ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝████╗  ██║██╔══██╗
 ██████╔╝███████║██║     █████╔╝ █████╗  ██╔██╗ ██║██║  ██║
 ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║╚██╗██║██║  ██║
 ██████╔╝██║  ██║╚██████╗██║  ██╗███████╗██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                           
 
```

For __churchspot__ app.

__ENDPOINTS DESCRIPTION__
`server/api/weather/<city name here>` - get json data about current weather in given city, for eg `server/api/weather/krosno` can return something like that: 
```


{
  "base": "stations", 
  "clouds": {
    "all": 75
  }, 
  "cod": 200, 
  "coord": {
    "lat": 49.69, 
    "lon": 21.77
  }, 
  "dt": 1575053806, 
  "id": 767470, 
  "main": {
    "humidity": 93, 
    "pressure": 1004, 
    "temp": 6.75, 
    "temp_max": 7.22, 
    "temp_min": 6.11
  }, 
  "name": "Krosno", 
  "sys": {
    "country": "PL", 
    "id": 1711, 
    "sunrise": 1575007515, 
    "sunset": 1575038238, 
    "type": 1
  }, 
  "timezone": 3600, 
  "visibility": 10000, 
  "weather": [
    {
      "description": "s\u0142abe opady deszczu", 
      "icon": "10n", 
      "id": 500, 
      "main": "Rain"
    }
  ], 
  "wind": {
    "deg": 260, 
    "speed": 4.1
  }
}
```