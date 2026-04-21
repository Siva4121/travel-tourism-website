"""Simple keyword-based chatbot for the Travel & Tourism website."""

from __future__ import annotations

import json
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from flights.models import Flight
from hotels.models import Hotel
from packages.models import Package


def _flights_payload(limit: int = 6) -> list[dict[str, Any]]:
    items = []
    for f in Flight.objects.filter(seats_available__gt=0)[:limit]:
        items.append(
            {
                'title': f"{f.airline} {f.flight_number}",
                'subtitle': f"{f.origin} → {f.destination}",
                'meta': f"{f.departure:%d %b, %H:%M} · ₹{f.price}",
                'url': reverse('flights:detail', args=[f.pk]),
            }
        )
    return items


def _hotels_payload(limit: int = 6) -> list[dict[str, Any]]:
    items = []
    for h in Hotel.objects.all()[:limit]:
        items.append(
            {
                'title': h.name,
                'subtitle': f"{h.city}, {h.country} · {h.star_rating}★",
                'meta': f"₹{h.price_per_night}/night",
                'url': reverse('hotels:detail', args=[h.pk]),
            }
        )
    return items


def _packages_payload(limit: int = 6) -> list[dict[str, Any]]:
    items = []
    for p in Package.objects.all()[:limit]:
        dest = p.destination.name if p.destination else p.city
        items.append(
            {
                'title': p.name,
                'subtitle': f"{dest} · {p.duration_label}",
                'meta': f"From ₹{p.price}",
                'url': reverse('packages:detail', args=[p.pk]),
            }
        )
    return items


def _answer(message: str) -> dict[str, Any]:
    msg = (message or '').lower().strip()
    if not msg:
        return {
            'reply': "Hi! Ask me things like 'show flights', 'list hotels', or 'view packages'.",
            'items': [],
        }

    greetings = ('hi', 'hello', 'hey', 'namaste', 'good morning', 'good evening')
    if any(g in msg for g in greetings) and len(msg) < 40:
        return {
            'reply': "Hello! I'm your travel assistant. Try: 'show flights', 'list hotels', 'view tourism packages'.",
            'items': [],
        }

    if 'book' in msg and 'history' in msg or 'my booking' in msg or 'previous booking' in msg:
        return {
            'reply': "You can view your booking history from the 'My Bookings' page in the top menu.",
            'items': [],
            'cta': {'label': 'Open My Bookings', 'url': reverse('bookings:list')},
        }

    if 'flight' in msg:
        items = _flights_payload()
        if not items:
            return {'reply': "I couldn't find any available flights right now.", 'items': []}
        return {
            'reply': f"Here are {len(items)} available flights:",
            'items': items,
            'cta': {'label': 'See all flights', 'url': reverse('flights:list')},
        }

    if 'hotel' in msg or 'stay' in msg or 'room' in msg:
        items = _hotels_payload()
        if not items:
            return {'reply': "No hotels listed yet.", 'items': []}
        return {
            'reply': f"Top {len(items)} hotels I found:",
            'items': items,
            'cta': {'label': 'See all hotels', 'url': reverse('hotels:list')},
        }

    if 'package' in msg or 'tour' in msg or 'itinerary' in msg or 'holiday' in msg:
        items = _packages_payload()
        if not items:
            return {'reply': "No tour packages available at the moment.", 'items': []}
        return {
            'reply': f"Here are {len(items)} tour packages:",
            'items': items,
            'cta': {'label': 'See all packages', 'url': reverse('packages:list')},
        }

    if 'help' in msg or 'what can you' in msg:
        return {
            'reply': (
                "I can help you with:\n"
                "• 'show flights' — list available flights\n"
                "• 'list hotels' — browse hotels\n"
                "• 'view packages' — tour packages\n"
                "• 'my bookings' — your booking history"
            ),
            'items': [],
        }

    return {
        'reply': "Sorry, I didn't quite get that. Try 'show flights', 'list hotels', or 'view packages'.",
        'items': [],
    }


def chat_page(request: HttpRequest):
    return render(request, 'chatbot/chat.html')


@csrf_exempt
@require_http_methods(['POST'])
def chat_api(request: HttpRequest):
    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        payload = {}
    message = payload.get('message', '')
    return JsonResponse(_answer(message))
