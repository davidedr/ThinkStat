'''
Created on 27/mag/2013

@author: davide
'''

data = [1, 2, 2, 2, 5]

data = [373,
545,
524,
392,
405,
361,
782,
519,
807,
407,
498,
364,
417,
424,
499,
626,
353,
428,
480,
402,
415,
565,
516,
518,
503,
565,
513,
526,
567,
564,
411,
517,
438,
487,
459,
586,
575,
400,
422,
429,
385,
428,
552,
516,
277,
354,
393,
396,
405,
395,
495,
424,
383,
337,
389,
441,
425,
402,
420,
339,
408,
353,
478,
385,
381,
355,
411,
367,
433,
216,
353,
326,
322,
351,
346,
440,
220,
395,
288,
344,
304,
368,
489,
190,
339,
296,
359,
365,
369,
431,
239,
377,
374,
357,
346,
342,
388,
235,
375,
328,
433,
416,
424,
466,
197,
310,
312,
311,
353,
332,
291,
164,
290,
255,
284,
324,
313,
360,
241,
306,
319,
308,
353,
362,
393,
286,
345,
286,
328,
378,
406,
401,
247,
333,
286,
342,
380,
335,
347,
311,
330,
341,
289,
223,
294,
360,
350,
296,
354,
437,
406,
470,
405,
375,
396,
452,
525,
385,
461,
408,
376,
453,
491,
248,
305,
274,
279,
321,
333,
430,
190,
282,
217,
253,
324,
442,
388,
258,
306,
279,
302,
376,
353,
448,
260,
324,
296,
316,
396,
374,
383,
255,
319,
291,
300,
401,
411,
415,
209,
192,
315,
331,
348,
353,
485,
288,
335,
364,
260,
328,
373,
386,
234,
327,
341,
336,
391,
336,
500,
325,
334,
339,
345,
387,
373,
397,
241,
277,
279,
315,
373,
370,
433,
182,
311,
307,
321,
344,
509,
391,
266,
383,
375,
329,
416,
496,
536,
445,
340,
360,
359,
371,
431,
262,
316,
292,
306,
368,
362,
393,
277,
328,
284,
290,
343,
391,
399,
275,
345,
340,
624,
374,
370,
440,
338,
391,
530,
374,
394,
371,
418,
307,
352,
258,
333,
382,
382,
372,
267,
330,
334,
324,
434,
441,
436,
285,
322,
370,
353,
367,
356,
]


hist = {}
for d in data:
    hist[d] = hist.get(d, 0) + 1

print   
print "Found: ", str(len(hist)), " different values out of: ", str(len(data)), "values"

pmf = {}
n = float(len(data))
for x, f in hist.items():
    pmf[x] = f/n
    
''' pmf '''
print
print "pmf:"
for k, v in pmf.items():
    print "k: ", k, " - ", v
    
''' pmf, sorted by values '''
print
print "pmf, sorted by values:"
for k in sorted(pmf.keys()):
    print "k: ", k, " - ", pmf.get(k)

'''pmf, sorted by frequencies'''
print
print "pmf, sorted by frequencies:"
for k, v in sorted(pmf.items(), key = lambda vk: vk[1]):
    print "k: ", k, " - ", v
    
''' pmf, histogram ''' 
print       
print "pmf, histogram:"
N = 30
max_f = max(pmf.values())
for v, f in pmf.items():
    L = f/max_f*N
    L = int(L)
    s = "v: " + str(v) + " - "
    for l in range(L):
        s += "*"
        
    print s

''' average ''' 
print       
average = float(sum(data))/float(len(data))
print "avrerage:", average

''' variance ''' 
print
variance = 0
for d in data:
    variance += (d - average)**2
variance /= len(data)
print "variance:", variance

''' mode ''' 
print       
print "mode:", sorted(pmf.items(), key = lambda vk: vk[1])[len(pmf) - 1]

import matplotlib.pyplot as pyplot
pyplot.pie(pmf.values())
pyplot.show()

pyplot.bar(pmf.keys(), pmf.values())
pyplot.show()

pyplot.plot(pmf.keys(), pmf.values())
pyplot.show()

''' mean of the pmf ''' 
mean = 0
for k, v in pmf.items():
    mean += v*k
print       
print "mean of the pmf:", str(mean), " (has to match average of data)"

''' variance of the pmf ''' 
variance = 0
for k, v in pmf.items():
    variance += v*(k - mean)**2
print       
print "variance of the pmf:", str(variance), " (has to match variance of data)"
        
print
print "deltas from mean"
deltas = []
for d in data:
    deltas.append(d - mean)
print "sum of deltas: ", str(sum(deltas)), " (should be zero)"    
pyplot.bar(range(len(data)), deltas)
pyplot.show()

pyplot.bar(range(len(data)), data)
pyplot.show()
    