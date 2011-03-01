# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Context, loader
from models import Entry
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
import util
from datetime import date
import calendar

def showCalendar(request, url):
	today = date.today()
	url = util.stripSlash(url)
	if url == "":
		month = today.month
		year = today.year
	else:
		try:
			year, month = url.split("/")
			year = int(year)
			month = int(month)
		except:
			return redirect("/calendar/")
	weeks = calendar.monthcalendar(year, month)
	
	entrylist = Entry.objects.all().filter(published = True, startDay__year = year, startDay__month = month)
	for i in range(len(weeks)):
		for o in range(len(weeks[i])):
			if weeks[i][o] == 0:
				day = ""
				htmlclass = "noday"
			else:
				day = weeks[i][o]
				if day == today.day and month == today.month and year == today.year:
					htmlclass = "today"
				else:
					htmlclass = "day"
			eventlist = []
			for entry in entrylist:
				if entry.startDay.day <= day and entry.endDay.day >= day:
					eventlist.append(entry)
			weeks[i][o] = [day, htmlclass, eventlist]
	monthname = calendar.month_name[month]
	weekdays = [_("Mo"), _("Tu"), _("We"), _("Th"), _("Fr"), _("Sa"), _("Su")] 
	context = util.generateContext(request, title = _('Calendar'), entries = weeks, url = url, year = year, month = month, monthname = monthname, weekdays = weekdays)
	return render_to_response('calendar/show.html', context)


def showEvent(request, url):
	url = util.stripSlash(url)
	entry = get_object_or_404(Entry, url = url, published = True)
	
	context = util.generateContext(request, title = _('Event'), event = entry, url = url)
	return render_to_response('calendar/single.html', context)
