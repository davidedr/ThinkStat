'''
Created on 26/mag/2013

@author: davide
'''

import thinkstats
import survey
import sys

def main(name, data_dir='.'):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    print "Number of Pregnancies: ", len(table.records)
    live_births = 0
    tot_births = 0
    first_babies = []
    other_bablies = []
    for record in table.records:
        tot_births += 1
        if record.outcome == 1:
            live_births += 1
            if record.birthord == 1:
                first_babies.append(record)
            else:
                other_bablies.append(record)

    print "live_births: ", live_births, " out of: ", tot_births, " records."
    print "first_babies: ", len(first_babies)
    print "other_bablies: ", len(other_bablies)
     
    print thinkstats.Mean([1, 1, 1, 3, 3, 591])
    
if __name__ == '__main__':
    print sys.argv
    main(*sys.argv)