This program gets JSON data on specific URL and push the data on Firebase database in periodic time(1 minute).

## Sample JSON File Presented by a Website (Input)
    {
    "regions": [

        null,

        {

            "gross": 100,

            "imagePath": 100.44418,

            "lastUpdate": "2024-08-12T10:00:00Z",

            "net": 100.78189,

            "regionName": "Süheyla Sultan",

            "workingEngines": "2024-08-26T11:19:53Z"

        },

        {

            "gross": 0.0,

            "imagePath": "assets/1 (2).jpg",

            "lastUpdate": "2024-08-02",

            "net": 100,

            "regionName": "Yurdanur Sultan",

            "workingEngines": 100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (3).jpg",

            "lastUpdate": "2024-08-03",

            "net": 100,

            "regionName": "Doğan Bey",

            "workingEngines": 4100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (4).jpg",

            "lastUpdate": "2024-08-04",

            "net": 100,

            "regionName": "Rauf Bey",

            "workingEngines": 100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (5).jpg",

            "lastUpdate": "2024-08-05",

            "net": 100,

            "regionName": "Kaya Bey",

            "workingEngines": 100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (6).jpg",

            "lastUpdate": "2024-08-06",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (7).jpg",

            "lastUpdate": "2024-08-07",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (8).jpg",

            "lastUpdate": "2024-08-08",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 5100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (9).jpg",

            "lastUpdate": "2024-08-09",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 6100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (10).jpg",

            "lastUpdate": "2024-08-10",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 8100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (11).jpg",

            "lastUpdate": "2024-08-11",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 4100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (12).jpg",

            "lastUpdate": "2024-08-12",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 7100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (13).jpg",

            "lastUpdate": "2024-08-13",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 6100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (14).jpg",

            "lastUpdate": "2024-08-14",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 5100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (15).jpg",

            "lastUpdate": "2024-08-15",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 7100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (16).jpg",

            "lastUpdate": "2024-08-16",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 8100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (17).jpg",

            "lastUpdate": "2024-08-17",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 6100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (18).jpg",

            "lastUpdate": "2024-08-18",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 5100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (19).jpg",

            "lastUpdate": "2024-08-19",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 6100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (20).jpg",

            "lastUpdate": "2024-08-20",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 5100

        },

        {

            "gross": 100,

            "imagePath": "assets/1 (21).jpg",

            "lastUpdate": "2024-08-21",

            "net": 100,

            "regionName": "Gökhan Bey",

            "workingEngines": 5100
        }
      ]
    }

<hr />

## Input URL:
Any url that refers .json file
## Output Operation:
Program push the data to Firebase database

<hr />

## Config:
1. In main.py file, change line 16 to your Firebase database URL (which is data send to)
2. In main.py file, change line 35 to your website that presents .json file
3. Change firebase-config.json file content with your database information

<hr />

## Warning:
When the program sends data, it deletes data already in the database. So if you run this program, your data which is already on your Firebase will be removed.

<hr />

## Notes:
Program presents an CLI which is prints last running time and situation(running with an error or not) and error details if any occured.
