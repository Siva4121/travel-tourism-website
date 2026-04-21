"""Seed the database with realistic sample data."""

from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from flights.models import Flight
from hotels.models import Hotel
from packages.models import Destination, Package


DESTINATIONS = [
    ("Goa", "Sun-kissed beaches, Portuguese heritage and vibrant nightlife."),
    ("Kerala", "God's own country — backwaters, houseboats and ayurvedic retreats."),
    ("Rajasthan", "Land of kings — palaces, deserts, forts and vibrant culture."),
    ("Himachal Pradesh", "Snow-capped peaks, pine forests and mountain towns."),
    ("Kashmir", "Paradise on earth with Dal Lake, shikaras and Mughal gardens."),
    ("Ladakh", "High-altitude deserts, monasteries and surreal landscapes."),
    ("Andaman", "Turquoise waters, coral reefs and pristine island beaches."),
    ("Uttarakhand", "Himalayan treks, yoga capitals and sacred rivers."),
]

PACKAGES = [
    {
        "name": "Magical Kerala Backwaters",
        "destination": "Kerala",
        "duration_days": 6, "duration_nights": 5,
        "price": 28999,
        "includes": "Houseboat stay\nAll meals\nAirport transfers\nSightseeing\nAyurveda session",
        "description": "Cruise through serene backwaters, explore tea plantations in Munnar, and relax at Kovalam beach.",
        "itinerary": "Day 1: Arrive Cochin, transfer to Munnar\nDay 2: Munnar sightseeing - tea museum, Eravikulam\nDay 3: Drive to Thekkady, Periyar wildlife\nDay 4: Alleppey houseboat check-in\nDay 5: Kovalam beach leisure\nDay 6: Departure from Trivandrum",
        "is_featured": True,
    },
    {
        "name": "Royal Rajasthan Heritage Tour",
        "destination": "Rajasthan",
        "duration_days": 8, "duration_nights": 7,
        "price": 38999,
        "includes": "Heritage hotels\nBreakfast\nAC car with driver\nElephant ride at Amer\nCamel safari in Jaisalmer",
        "description": "Explore the grandeur of Jaipur, Jodhpur, Udaipur and Jaisalmer — India's most iconic desert kingdoms.",
        "itinerary": "Day 1: Arrive Jaipur\nDay 2: Jaipur city tour - Amer Fort, City Palace\nDay 3: Drive to Jodhpur\nDay 4: Jodhpur - Mehrangarh Fort\nDay 5: Jaisalmer - Sam dunes camel safari\nDay 6: Drive to Udaipur\nDay 7: Udaipur lake tour\nDay 8: Departure",
        "is_featured": True,
    },
    {
        "name": "Goa Beach Escape",
        "destination": "Goa",
        "duration_days": 4, "duration_nights": 3,
        "price": 14999,
        "includes": "4★ beach resort\nBreakfast\nAirport transfers\nDudhsagar trip\nCruise on Mandovi",
        "description": "Relax on North and South Goa beaches, explore old Portuguese churches and enjoy vibrant nightlife.",
        "itinerary": "Day 1: Arrive Goa, beach leisure\nDay 2: North Goa - Baga, Calangute, Anjuna\nDay 3: South Goa - Colva, Cabo de Rama\nDay 4: Departure",
        "is_featured": True,
    },
    {
        "name": "Shimla–Manali Himalayan Getaway",
        "destination": "Himachal Pradesh",
        "duration_days": 7, "duration_nights": 6,
        "price": 26999,
        "includes": "Hotel stays\nBreakfast + Dinner\nVolvo transfers\nRohtang pass visit",
        "description": "Pine-scented valleys, snow activities and charming hill-station towns of Himachal.",
        "itinerary": "Day 1: Chandigarh to Shimla\nDay 2: Shimla sightseeing - Mall road, Kufri\nDay 3: Shimla to Manali\nDay 4: Solang Valley\nDay 5: Manali local\nDay 6: Return to Chandigarh\nDay 7: Departure",
    },
    {
        "name": "Srinagar–Gulmarg–Pahalgam Retreat",
        "destination": "Kashmir",
        "duration_days": 6, "duration_nights": 5,
        "price": 32999,
        "includes": "Houseboat on Dal Lake\nAll meals\nGondola in Gulmarg\nShikara ride",
        "description": "Experience heaven on earth — houseboats, pony rides, gondolas and Mughal gardens.",
        "itinerary": "Day 1: Arrive Srinagar, Shikara ride\nDay 2: Gulmarg with Gondola\nDay 3: Pahalgam\nDay 4: Aru & Betaab valley\nDay 5: Srinagar local - gardens\nDay 6: Departure",
        "is_featured": True,
    },
    {
        "name": "Ladakh Adventure Expedition",
        "destination": "Ladakh",
        "duration_days": 7, "duration_nights": 6,
        "price": 45999,
        "includes": "Premium camps & hotels\nBreakfast + Dinner\nInner line permits\nMonastery tours",
        "description": "High-altitude adventure — Pangong Lake, Nubra Valley camel rides, and Buddhist monasteries.",
        "itinerary": "Day 1: Arrive Leh, acclimatize\nDay 2: Leh monasteries\nDay 3: Drive to Nubra via Khardung La\nDay 4: Nubra to Pangong\nDay 5: Pangong to Leh\nDay 6: Sham Valley\nDay 7: Departure",
    },
    {
        "name": "Andaman Island Paradise",
        "destination": "Andaman",
        "duration_days": 5, "duration_nights": 4,
        "price": 34999,
        "includes": "Beach resort\nFerry transfers\nSnorkeling\nGlass-bottom boat",
        "description": "Crystal-clear waters, Radhanagar beach, and scuba diving at one of Asia's top beaches.",
        "itinerary": "Day 1: Arrive Port Blair\nDay 2: Havelock - Radhanagar beach\nDay 3: Neil Island\nDay 4: Port Blair - Cellular Jail\nDay 5: Departure",
    },
    {
        "name": "Rishikesh Yoga & Adventure",
        "destination": "Uttarakhand",
        "duration_days": 4, "duration_nights": 3,
        "price": 12999,
        "includes": "Riverside camp\nAll meals\nRafting\nYoga session\nGanga aarti",
        "description": "Rejuvenating yoga retreat with white-water rafting on the Ganga in the adventure capital.",
        "itinerary": "Day 1: Arrive Rishikesh\nDay 2: River rafting\nDay 3: Yoga + Ganga aarti\nDay 4: Departure",
    },
]

HOTELS = [
    ("Taj Malabar Resort & Spa", "Cochin", "Kerala", 5, 12500, "Pool, Spa, WiFi, Gym, Restaurant, Beach access",
     "Iconic waterfront luxury with stunning harbour views."),
    ("The Oberoi Udaivilas", "Udaipur", "Rajasthan", 5, 28000, "Pool, Spa, WiFi, Fine dining, Palace view",
     "A palace by Lake Pichola — grandeur redefined."),
    ("Taj Lake Palace", "Udaipur", "Rajasthan", 5, 32000, "Pool, Spa, WiFi, Lake view, Butler service",
     "A floating marble wonder on Lake Pichola."),
    ("Marriott Goa Resort", "Goa", "Goa", 5, 9500, "Pool, Beach, WiFi, Gym, Multi-cuisine",
     "Beachfront luxury minutes from Miramar beach."),
    ("The Lalit Grand Palace", "Srinagar", "Jammu and Kashmir", 5, 11000, "Garden, WiFi, Spa, Indoor pool",
     "Former royal residence overlooking the Dal Lake."),
    ("Wildflower Hall", "Shimla", "Himachal Pradesh", 5, 18500, "Spa, WiFi, Fireplace, Himalayan views",
     "A colonial-era retreat with stunning valley views."),
    ("ITC Grand Bharat", "Gurgaon", "Haryana", 5, 17500, "Golf, Pool, Spa, WiFi, Multiple restaurants",
     "Luxury retreat minutes from Delhi with a golf course."),
    ("Holiday Inn Express", "Bengaluru", "Karnataka", 3, 4500, "WiFi, Breakfast, Gym, Business centre",
     "Modern, comfortable stay near MG Road."),
    ("Hyatt Regency", "Chennai", "Tamil Nadu", 5, 8500, "Pool, Spa, WiFi, Fine dining",
     "Business luxury in the heart of Chennai."),
    ("Radisson Blu", "Jaipur", "Rajasthan", 4, 7500, "Pool, WiFi, Spa, Multi-cuisine",
     "Comfortable stay in the heart of the Pink City."),
    ("Zostel Manali", "Manali", "Himachal Pradesh", 3, 1500, "WiFi, Cafe, Common lounge, Mountain view",
     "Budget-friendly hostel with great social vibe."),
    ("Barefoot at Havelock", "Havelock", "Andaman", 4, 13500, "Beach, WiFi, Restaurant, Dive centre",
     "Rustic luxury on Radhanagar beach."),
]

FLIGHTS = [
    ("IndiGo", "6E-201", "Delhi", "Goa", 2, 9, 5500),
    ("Air India", "AI-803", "Mumbai", "Cochin", 3, 6, 6800),
    ("SpiceJet", "SG-102", "Bengaluru", "Jaipur", 4, 7, 7200),
    ("Vistara", "UK-770", "Delhi", "Srinagar", 5, 8, 8900),
    ("IndiGo", "6E-305", "Chennai", "Port Blair", 6, 10, 7400),
    ("Air India", "AI-129", "Delhi", "Leh", 7, 11, 10500),
    ("Vistara", "UK-555", "Mumbai", "Udaipur", 8, 12, 6100),
    ("SpiceJet", "SG-220", "Bengaluru", "Goa", 9, 13, 5100),
    ("IndiGo", "6E-419", "Delhi", "Manali", 10, 14, 7900),
    ("Air India Express", "IX-812", "Kochi", "Mumbai", 11, 15, 5800),
    ("IndiGo", "6E-512", "Kolkata", "Andaman", 12, 16, 6800),
    ("Akasa Air", "QP-177", "Mumbai", "Jaipur", 13, 17, 5300),
]


class Command(BaseCommand):
    help = "Seed the database with sample destinations, packages, hotels, flights and an admin user."

    def add_arguments(self, parser):
        parser.add_argument('--fresh', action='store_true', help='Delete existing sample data first.')

    def handle(self, *args, **options):
        if options['fresh']:
            Flight.objects.all().delete()
            Hotel.objects.all().delete()
            Package.objects.all().delete()
            Destination.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing data."))

        # Admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@travelindia.com', 'admin12345')
            self.stdout.write(self.style.SUCCESS("Created superuser: admin / admin12345"))

        # Demo user
        if not User.objects.filter(username='demo').exists():
            demo = User.objects.create_user('demo', 'demo@travelindia.com', 'demo12345')
            demo.first_name = 'Demo'
            demo.last_name = 'Traveler'
            demo.save()
            self.stdout.write(self.style.SUCCESS("Created demo user: demo / demo12345"))

        # Destinations
        dest_map = {}
        for name, desc in DESTINATIONS:
            d, _ = Destination.objects.get_or_create(
                name=name,
                defaults={'country': 'India', 'description': desc},
            )
            dest_map[name] = d

        # Packages
        for data in PACKAGES:
            Package.objects.get_or_create(
                name=data['name'],
                defaults={
                    'destination': dest_map.get(data['destination']),
                    'duration_days': data['duration_days'],
                    'duration_nights': data['duration_nights'],
                    'price': Decimal(str(data['price'])),
                    'includes': data['includes'],
                    'description': data['description'],
                    'itinerary': data['itinerary'],
                    'is_featured': data.get('is_featured', False),
                    'slots_available': 30,
                },
            )

        # Hotels
        for name, city, country, stars, price, amenities, desc in HOTELS:
            Hotel.objects.get_or_create(
                name=name,
                city=city,
                defaults={
                    'country': country,
                    'star_rating': stars,
                    'price_per_night': Decimal(str(price)),
                    'amenities': amenities,
                    'description': desc,
                    'rooms_available': 20,
                },
            )

        # Flights (schedule in next 30 days)
        now = timezone.now().replace(minute=0, second=0, microsecond=0)
        for airline, number, origin, destination, dep_days, arr_days, price in FLIGHTS:
            dep = now + timedelta(days=dep_days, hours=8)
            arr = dep + timedelta(hours=2, minutes=30)
            Flight.objects.get_or_create(
                flight_number=number,
                defaults={
                    'airline': airline,
                    'origin': origin,
                    'destination': destination,
                    'departure': dep,
                    'arrival': arr,
                    'price': Decimal(str(price)),
                    'seats_available': 60,
                    'travel_class': 'economy',
                },
            )

        self.stdout.write(self.style.SUCCESS(
            f"Seed complete. Destinations={Destination.objects.count()}, "
            f"Packages={Package.objects.count()}, Hotels={Hotel.objects.count()}, "
            f"Flights={Flight.objects.count()}"
        ))
