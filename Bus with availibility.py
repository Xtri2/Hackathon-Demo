

bus_data = [
    # Kathmandu to Pokhara Route
    {
        "bus_number": "BA 1 KH 2023",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Ram Kumar Shrestha",
        "route": {"start": "Kathmandu", "end": "Pokhara"},
        "seat_capacity": 40,
        "seat_available": 34,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.8,
        "price": 1300
    },
    {
        "bus_number": "BA 2 KH 1234",
        "bus_model": "Scania K410",
        "service_company": "Nepal Yatayat",
        "driver_name": "Hari Bahadur Thapa",
        "route": {"start": "Kathmandu", "end": "Pokhara"},
        "seat_capacity": 35,
        "seat_available": 23,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.8,
        "price": 2200
    },
    {
        "bus_number": "BAR 1 KH 2023",
        "bus_model": "Vlvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Ram Kumar Shrestha",
        "route": {"start": "Kathmandu", "end": "Pokhara"},
        "seat_capacity": 40,"seat_available": 35,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.8,
        "price": 1800
    },
    {
        "bus_number": "BA 1 KH 2023",
        "bus_model": "Volvo 9400",
        "service_company": "Pokhara Yatayat",
        "driver_name": "Ram Kumar Shrestha",
        "route": {"start": "Kathmandu", "end": "Pokhara"},
        "seat_capacity": 30,
        "seat_available": 22,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.8,
        "price": 1400
    },
    {
        "bus_number": "BA 1 KH 2023",
        "bus_model": "Volvo 9400",
        "service_company": "Non-Stop Yatayat",
        "driver_name": "Ram Kumar Shrestha",
        "route": {"start": "Kathmandu", "end": "Pokhara"},
        "seat_capacity": 40,
        "seat_available": 32,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.8,
        "price": 1700
    },
    {
        "bus_number": "BA 1 KH 2023",
        "bus_model": "Volvo 9400",
        "service_company": "Express Yatayat",
        "driver_name": "Ram Kumar Shrestha",
        "route": {"start": "Kathmandu", "end": "Pokhara"},
        "seat_capacity": 40,
        "seat_available": 22,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.8,
        "price": 1200
    },
    {
        "bus_number": "GA 1 KH 9012",
        "bus_model": "Scania K410",
        "service_company": "Sajha Yatayat",
        "driver_name": "Bikash Tamang",
        "route": {"start": "Pokhara", "end": "Kathmandu"},
        "seat_capacity": 35,
        "seat_available": 11,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.6,
        "price": 1900
    },
    {
        "bus_number": "GA 2 KH 3456",
        "bus_model": "Volvo 9400",
        "service_company": "Mountain Express",
        "driver_name": "Rajesh Magar",
        "route": {"start": "Pokhara", "end": "Kathmandu"},
        "seat_capacity": 40,
        "seat_available": 25,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.9,
        "price": 1800
    },
    {
        "bus_number": "BA 18 KH 1234",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Ram Bahadur Magar",
        "route": {"start": "Pokhara", "end": "Kathmandu"},
        "seat_capacity": 40,
        "seat_available": 13,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.9,
        "price": 1300
    },
    {
        "bus_number": "GA 13 KH 4321",
        "bus_model": "Scania K410",
        "service_company": "Dhaulagiri Yatayat",
        "driver_name": "Anil Thapa",
        "route": {"start": "Pokhara", "end": "Kathmandu"},
        "seat_capacity": 42,
        "seat_available": 17,
        "ac": True,
        "wifi": False,
        "date": "2024-12-02",
        "rating": 3.7,
        "price": 1350
    },
    {
        "bus_number": "KO 1 KH 2222",
        "bus_model": "Scania K410",
        "service_company": "Mountain Express",
        "driver_name": "Bibhan Rai",
        "route": {"start": "Biratnagar", "end": "Kathmandu"},
        "seat_capacity": 35,
        "seat_available": 31,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.5,
        "price": 1900
    },
    {
        "bus_number": "KO 2 KH 3333",
        "bus_model": "Volvo 9400",
        "service_company": "Nepal Yatayat",
        "driver_name": "Deepak Karki",
        "route": {"start": "Biratnagar", "end": "Kathmandu"},
        "seat_capacity": 40,
        "seat_available": 28,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.6,
        "price": 1900
    },
    {
        "bus_number": "BA 4 KH 2345",
        "bus_model": "Scania K410",
        "service_company": "Sajha Yatayat",
        "driver_name": "Rajan Gurung",
        "route": {"start": "Biratnagar", "end": "Kathmandu"},
        "seat_capacity": 45,
        "seat_available": 22,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.7,
        "price": 1600
    },
    {
        "bus_number": "GA 9 KH 5678",
        "bus_model": "Volvo 9400",
        "service_company": "Dhaulagiri Yatayat",
        "driver_name": "Prakash Koirala",
        "route": {"start": "Biratnagar", "end": "Kathmandu"},
        "seat_capacity": 40,
        "seat_available": 24,
        "ac": True,
        "wifi": False,
        "date": "2024-12-02",
        "rating": 4.2,
        "price": 1400
    },
    {
        "bus_number": "BA 8 KH 2424",
        "bus_model": "Volvo 9400",
        "service_company": "Himalayan Travels",
        "driver_name": "Sanshray Lama",
        "route": {"start": "Kathmandu", "end": "Darjeeling"},
        "seat_capacity": 40,
        "seat_available": 15,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.9,
        "price": 4000
    },
    {
        "bus_number": "BA 9 KH 3535",
        "bus_model": "Scania K410",
        "service_company": "Mountain Express",
        "driver_name": "Rajendra Shrestha",
        "route": {"start": "Kathmandu", "end": "Darjeeling"},
        "seat_capacity": 35,
        "seat_available": 13,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.8,
        "price": 3900
    },
    {
        "bus_number": "BA 12 KH 1234",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Sujan Rai",
        "route": {"start": "Kathmandu", "end": "Darjeeling"},
        "seat_capacity": 40,
        "seat_available": 19,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.8,
        "price": 3500
    },
    {
        "bus_number": "GA 5 KH 6868",
        "bus_model": "Volvo 9400",
        "service_company": "Himalayan Travels",
        "driver_name": "Dinesh Gurung",
        "route": {"start": "Pokhara", "end": "Darjeeling"},
        "seat_capacity": 40,
        "seat_available": 13,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.6,
        "price": 3500
    },
    {
        "bus_number": "GA 6 KH 7979",
        "bus_model": "Scania K410",
        "service_company": "Mountain Express",
        "driver_name": "Sujan Thapa",
        "route": {"start": "Pokhara", "end": "Darjeeling"},
        "seat_capacity": 35,
        "seat_available": 4,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.5,
        "price": 3200
    },
    {
        "bus_number": "NA 5 KH 1414",
        "bus_model": "Volvo 9400",
        "service_company": "Himalayan Travels",
        "driver_name": "Bishnu Prasad",
        "route": {"start": "Lumbini", "end": "Sikkim"},
        "seat_capacity": 40,
        "seat_available": 31,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.5,
        "price": 4800
    },
    {
        "bus_number": "NA 6 KH 2525",
        "bus_model": "Scania K410",
        "service_company": "Mountain Express",
        "driver_name": "Hem Bahadur",
        "route": {"start": "Lumbini", "end": "Sikkim"},
        "seat_capacity": 35,
        "seat_available": 14,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.4,
        "price": 4600
    },
    {
        "bus_number": "GA 26 KH 5678",
        "bus_model": "Scania K410",
        "service_company": "Myagdi Yatayat",
        "driver_name": "Raju Tamang",
        "route": {"start": "Lumbini", "end": "Sikkim"},
        "seat_capacity": 45,
        "seat_available": 22,
        "ac": True,
        "wifi": False,
        "date": "2024-12-02",
        "rating": 4.5,
        "price": 4200
    },
    {
        "bus_number": "BA 45 KH 1234",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Sushil Thapa",
        "route": {"start": "Kathmandu", "end": "Sikkim"},
        "seat_capacity": 40,
        "seat_available": 28,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.9,
        "price": 3900
    },
    {
        "bus_number": "GA 46 KH 5678",
        "bus_model": "Scania K410",
        "service_company": "Dhaulagiri Yatayat",
        "driver_name": "Bimal Gurung",
        "route": {"start": "Kathmandu", "end": "Sikkim"},
        "seat_capacity": 45,
        "seat_available": 32,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.7,
        "price": 3700
    },
    {
        "bus_number": "BA 50 KH 7890",
        "bus_model": "Scania K360",
        "service_company": "Myagdi Yatayat",
        "driver_name": "Pashupati Thapa",
        "route": {"start": "Kathmandu", "end": "Sikkim"},
        "seat_capacity": 42,
        "seat_available": 24,
        "ac": True,
        "wifi": False,
        "date": "2024-12-02",
        "rating": 4.5,
        "price": 3800
    },
    {
        "bus_number": "BA 60 PK 1234",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Ram Bahadur Magar",
        "route": {"start": "Pokhara", "end": "Biratnagar"},
        "seat_capacity": 45,
        "seat_available": 27,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.9,
        "price": 6200
    },
    {
        "bus_number": "GA 61 PK 5678",
        "bus_model": "Scania K410",
        "service_company": "Dhaulagiri Yatayat",
        "driver_name": "Suraj Gurung",
        "route": {"start": "Pokhara", "end": "Biratnagar"},
        "seat_capacity": 50,
        "seat_available": 14,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.7,
        "price": 6000
    },
    {
        "bus_number": "BA 62 PK 7890",
        "bus_model": "Scania K360",
        "service_company": "Myagdi Yatayat",
        "driver_name": "Anil Adhikari",
        "route": {"start": "Pokhara", "end": "Biratnagar"},
        "seat_capacity": 48,
        "seat_available": 22,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.6,
        "price": 5900
    },
    {
        "bus_number": "BA 80 PK 1234",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Bishal Koirala",
        "route": {"start": "Pokhara", "end": "Darjeeling"},
        "seat_capacity": 45,
        "seat_available": 27,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.9,
        "price": 4900
    },
    {
        "bus_number": "GA 81 PK 5678",
        "bus_model": "Scania K410",
        "service_company": "Travel Nepal Bus Service",
        "driver_name": "Rajan Rai",
        "route": {"start": "Pokhara", "end": "Darjeeling"},
        "seat_capacity": 50,
        "seat_available": 42,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.8,
        "price": 4800
    },
    {
        "bus_number": "BA 91 LB 1234",
        "bus_model": "Volvo 9400",
        "service_company": "Sajha Yatayat",
        "driver_name": "Sanshray Gurung",
        "route": {"start": "Lumbini", "end": "Biratnagar"},
        "seat_capacity": 45,
        "seat_available": 35,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.9,
        "price": 3700
    },
    {
        "bus_number": "GA 92 LB 5678",
        "bus_model": "Scania K410",
        "service_company": "Dhaulagiri Yatayat",
        "driver_name": "Hari Koirala",
        "route": {"start": "Lumbini", "end": "Biratnagar"},
        "seat_capacity": 50,
        "seat_available": 39,
        "ac": True,
        "wifi": True,
        "date": "2024-12-02",
        "rating": 4.8,
        "price": 3500
    },
    {
        "bus_number": "BA 93 LB 2345",
        "bus_model": "Scania K360",
        "service_company": "Myagdi Yatayat",
        "driver_name": "Bibhan Sharma",
        "route": {"start": "Lumbini", "end": "Biratnagar"},
        "seat_capacity": 48,
        "seat_available": 22,
        "ac": True,
        "wifi": True,
        "date": "2024-12-01",
        "rating": 4.7,
        "price": 3200
    }
]

# Sort buses by date and rating
bus_data.sort(key=lambda x: (x['date'], -x['rating'])) 