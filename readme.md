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
__ENDPOINTS DESCRIPTION__


`server/api/bible/get-random` - get json data with random bible verse. It should produce output like that: 


```
{
    "data": {
        "bibleId": "1c9761e0230da6e0-01",
        "bookId": "JOS",
        "chapterId": "JOS.1",
        "content": "<p class=\"m\"><span data-number=\"9\" class=\"v\">9</span>Czyż ci nie nakazałem? Wzmocnij się i bądź mężny. Nie lękaj się i nie przerażaj, gdyż PAN, twój Bóg, jest z tobą, dokądkolwiek pójdziesz.</p>",
        "copyright": "Copyright © 2018 Fundacja Wrota Nadziei. Released under the Creative Commons Attribution No Derivatives License 4.0.",
        "id": "JOS.1.9",
        "next": {
            "id": "JOS.1.10",
            "number": "10"
        },
        "orgId": "JOS.1.9",
        "previous": {
            "id": "JOS.1.8",
            "number": "8"
        },
        "reference": "Jozuego 1:9"
    },
    "meta": {
        "fums": "<script>\nvar _BAPI=_BAPI||{};\nif(typeof(_BAPI.t)==='undefined'){\ndocument.write('\\x3Cscript src=\"'+document.location.protocol+'//cdn.scripture.api.bible/fums/fumsv2.min.js\"\\x3E\\x3C/script\\x3E');}\ndocument.write(\"\\x3Cscript\\x3E_BAPI.t('' + unique + '');\\x3C/script\\x3E\");\n</script><noscript><img src=\"https://d3a2okcloueqyx.cloudfront.net/nf1?t=' + unique + '\" height=\"1\" width=\"1\" border=\"0\" alt=\"\" style=\"height: 0; width: 0;\" /></noscript>",
        "fumsId": "c8f12651-185c-4bc2-a42e-ab360492f5ae",
        "fumsJs": "var _BAPI=_BAPI||{};if(typeof(_BAPI.t)!='undefined'){ _BAPI.t('c8f12651-185c-4bc2-a42e-ab360492f5ae'); }",
        "fumsJsInclude": "cdn.scripture.api.bible/fums/fumsv2.min.js",
        "fumsNoScript": "<img src=\"https://d3btgtzu3ctdwx.cloudfront.net/nf1?t=c8f12651-185c-4bc2-a42e-ab360492f5ae\" height=\"1\" width=\"1\" border=\"0\" alt=\"\" style=\"height: 0; width: 0;\" />"
    }
}```