#!/usr/bin/env python
import sys
""" Create dictionary with average number of movies rated for each user,
	average number of user ratings for each movie"""

for line in sys.stdin:
    fields = line.strip().split("\t")
    #print fields
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (fields[1], fields[0], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7])
