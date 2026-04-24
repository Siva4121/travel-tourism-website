"""Seed the database with realistic sample data."""

from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from attractions.models import Attraction
from cars.models import Car
from flighthotel.models import FlightHotelDeal
from flights.models import Flight
from hotels.models import Hotel
from packages.models import Destination, Package
from trains.models import Train


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

TRAINS = [
    ("Rajdhani Express", "12301", "New Delhi", "Mumbai Central", 1, 17, 2, "2A", 2650),
    ("Shatabdi Express", "12002", "New Delhi", "Bhopal", 2, 8, 7, "CC", 1450),
    ("Duronto Express", "12273", "Howrah", "New Delhi", 3, 22, 16, "3A", 1980),
    ("Tejas Express", "82501", "Mumbai CST", "Goa", 4, 5, 30, "EC", 2450),
    ("Vande Bharat Express", "22435", "New Delhi", "Varanasi", 5, 6, 8, "EC", 1875),
    ("Gatimaan Express", "12049", "Hazrat Nizamuddin", "Jhansi", 6, 8, 4, "CC", 1050),
    ("Chennai Mail", "12601", "Chennai Central", "Mangalore", 7, 19, 15, "SL", 850),
    ("Himgiri Express", "12331", "Howrah", "Jammu Tawi", 8, 23, 32, "3A", 2200),
]

CARS = [
    ("Maruti Swift", "Maruti", "compact", "Mumbai Airport", "manual", "petrol", 5, 2, 1800, "Reliable hatchback perfect for city travel and short trips."),
    ("Hyundai Creta", "Hyundai", "suv", "Delhi Airport", "automatic", "diesel", 5, 3, 3200, "Compact SUV with generous legroom and modern features."),
    ("Toyota Innova Crysta", "Toyota", "van", "Bengaluru Airport", "manual", "diesel", 7, 4, 4200, "Spacious 7-seater for family trips and airport pickups."),
    ("Honda City", "Honda", "sedan", "Chennai Airport", "automatic", "petrol", 5, 3, 2800, "Comfortable sedan with smooth ride quality."),
    ("Mahindra XUV700", "Mahindra", "suv", "Hyderabad Airport", "automatic", "diesel", 7, 4, 4500, "Premium SUV with panoramic sunroof and ADAS features."),
    ("BMW 5 Series", "BMW", "luxury", "Delhi Airport", "automatic", "petrol", 5, 3, 9500, "Executive luxury sedan with chauffeur option."),
    ("Tata Nexon EV", "Tata", "compact", "Pune Airport", "automatic", "electric", 5, 2, 2600, "Eco-friendly electric SUV with quiet cabin."),
    ("Maruti Ertiga", "Maruti", "van", "Goa Airport", "manual", "petrol", 7, 3, 2400, "Affordable 7-seater ideal for group outings."),
]

ATTRACTIONS = [
    ("Taj Mahal Skip-the-Line Tour", "Agra", "landmark", 3, 1500, 4.8, 3420, True,
     "Ivory-white marble mausoleum on the banks of the Yamuna — one of the seven wonders of the world.",
     "Skip-the-line entry\nLicensed English guide\nBottled water\nHotel pickup (select areas)"),
    ("Jaipur City Palace & Amber Fort", "Jaipur", "landmark", 5, 1800, 4.7, 2150, True,
     "Explore the Pink City — Amber Fort, Hawa Mahal and the majestic City Palace.",
     "Entry tickets included\nAC transfers\nElephant/jeep ride at Amber\nLunch at heritage restaurant"),
    ("Goa Sunset Cruise", "Goa", "cruise", 2, 950, 4.5, 1840, True,
     "Relaxing Mandovi river cruise with live music, Goan dance and snacks.",
     "Welcome drink\nLive performances\nSnacks\nOpen-deck views"),
    ("Kerala Backwater Houseboat Day Cruise", "Alleppey", "cruise", 6, 2400, 4.9, 1290, True,
     "Glide through palm-fringed backwaters on a traditional kettuvallam with meals on board.",
     "Traditional houseboat\nLunch + snacks\nLocal guide\nSightseeing stops"),
    ("Dubai Desert Safari", "Dubai", "adventure", 6, 3200, 4.7, 5800, False,
     "Dune bashing, camel ride, BBQ dinner and cultural performances at a Bedouin camp.",
     "4x4 dune bashing\nCamel ride\nBBQ buffet\nBelly dance & tanoura show"),
    ("Singapore Universal Studios Ticket", "Singapore", "theme", 8, 5400, 4.6, 4210, False,
     "Full-day access to Universal Studios Singapore with 24+ rides and attractions.",
     "One-day entry pass\nValid 6 months\nMobile e-ticket"),
    ("Bali Ubud Rice Terrace Tour", "Ubud", "tour", 7, 2100, 4.8, 980, False,
     "Tegalalang rice terraces, Sacred Monkey Forest, traditional lunch and coffee plantation.",
     "Private transfers\nEnglish-speaking driver\nLunch\nEntrance fees"),
    ("Leh Pangong Lake Jeep Tour", "Leh", "adventure", 10, 3800, 4.7, 620, False,
     "Full-day 4x4 journey over Chang La pass to the mesmerising Pangong Tso.",
     "4x4 jeep transfers\nInner line permit\nPacked lunch\nOxygen cylinder"),
]

FLIGHT_HOTEL_DEALS = [
    ("Goa Beach Escape: Flight + 3N Beachfront", "Goa", 3, 2, 18999, 3200, True,
     "Round-trip flight from Mumbai + 3 nights at a beachfront 4★ resort with daily breakfast.",
     "Round-trip flight\n3 nights 4★ resort\nDaily breakfast\nAirport transfers"),
    ("Kerala Houseboat Combo", "Cochin", 4, 2, 27499, 4500, True,
     "Flight + 1 night Cochin hotel + 1 night houseboat + 2 nights Kovalam beach.",
     "Round-trip flight\n4 nights mixed stays\nAll breakfasts\nAirport transfers\nHouseboat experience"),
    ("Jaipur Royal Weekend", "Jaipur", 2, 2, 14999, 2100, True,
     "Flight + 2 nights at a heritage 4★ property with breakfast and Amer Fort tour.",
     "Round-trip flight\n2 nights heritage hotel\nBreakfast\nAmer Fort half-day tour"),
    ("Srinagar Houseboat Special", "Srinagar", 4, 2, 29999, 3800, False,
     "Flight + 2 nights Dal Lake houseboat + 2 nights hotel with Shikara ride.",
     "Round-trip flight\n4 nights stay\nAll meals\nShikara ride\nAirport transfers"),
    ("Andaman Scuba Getaway", "Port Blair", 5, 2, 39999, 5200, False,
     "Flight + 2N Port Blair + 3N Havelock beach resort with inclusive ferries.",
     "Round-trip flight\n5 nights stay\nFerries included\nBreakfast\nSnorkeling session"),
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
            FlightHotelDeal.objects.all().delete()
            Attraction.objects.all().delete()
            Car.objects.all().delete()
            Train.objects.all().delete()
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

        # Trains
        for name, number, origin, destination, dep_days, dep_hour, duration_hr, cls, price in TRAINS:
            dep = now + timedelta(days=dep_days, hours=dep_hour)
            arr = dep + timedelta(hours=duration_hr)
            Train.objects.get_or_create(
                number=number,
                defaults={
                    'name': name,
                    'origin': origin,
                    'destination': destination,
                    'departure': dep,
                    'arrival': arr,
                    'travel_class': cls,
                    'price': Decimal(str(price)),
                    'seats_available': 120,
                },
            )

        # Cars
        for name, brand, category, location, trans, fuel, seats, bags, price, desc in CARS:
            Car.objects.get_or_create(
                name=name,
                pickup_location=location,
                defaults={
                    'brand': brand,
                    'category': category,
                    'transmission': trans,
                    'fuel_type': fuel,
                    'seats': seats,
                    'luggage_capacity': bags,
                    'air_conditioning': True,
                    'price_per_day': Decimal(str(price)),
                    'cars_available': 8,
                    'description': desc,
                },
            )

        # Attractions
        for name, city, category, duration, price, rating, reviews, featured, desc, highlights in ATTRACTIONS:
            Attraction.objects.get_or_create(
                name=name,
                city=city,
                defaults={
                    'country': 'India' if city in {'Agra', 'Jaipur', 'Goa', 'Alleppey', 'Leh'} else 'International',
                    'category': category,
                    'duration_hours': Decimal(str(duration)),
                    'price': Decimal(str(price)),
                    'rating': Decimal(str(rating)),
                    'reviews_count': reviews,
                    'is_featured': featured,
                    'description': desc,
                    'highlights': highlights,
                    'slots_available': 40,
                },
            )

        # Flight + Hotel deals (link to existing flight/hotel when matching city)
        for name, city, nights, travelers, price, savings, featured, desc, inclusions in FLIGHT_HOTEL_DEALS:
            flight = Flight.objects.filter(destination__icontains=city).first()
            hotel = Hotel.objects.filter(city__icontains=city).first()
            FlightHotelDeal.objects.get_or_create(
                name=name,
                defaults={
                    'destination_city': city,
                    'flight': flight,
                    'hotel': hotel,
                    'nights': nights,
                    'travelers': travelers,
                    'combined_price': Decimal(str(price)),
                    'savings': Decimal(str(savings)),
                    'is_featured': featured,
                    'description': desc,
                    'inclusions': inclusions,
                    'slots_available': 15,
                },
            )

        self.stdout.write(self.style.SUCCESS(
            f"Seed complete. Destinations={Destination.objects.count()}, "
            f"Packages={Package.objects.count()}, Hotels={Hotel.objects.count()}, "
            f"Flights={Flight.objects.count()}, Trains={Train.objects.count()}, "
            f"Cars={Car.objects.count()}, Attractions={Attraction.objects.count()}, "
            f"FlightHotelDeals={FlightHotelDeal.objects.count()}"
        ))
