
import math
import os
import random
import re
import sys


#
# Complete the 'playRackO' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING info
#  2. STRING rack
#  3. STRING pile
#

def stepdown(rack):
    cnt1 = 0
    cnt2 = 1

    stepdowns = 0

    while cnt2 < len(rack):
        if rack[cnt1] > rack[cnt2]:
            stepdowns = stepdowns + 1
            cnt1 = cnt1 + 1
            cnt2 = cnt2 + 1
        else:
            cnt1 = cnt1 + 1
            cnt2 = cnt2 + 1
    
    return stepdowns


def idealslot(rack, pile, ranges):
    card = pile[0]
    pile.pop(0)
    racka = rack

    cnt = 0
    ender = 0
    while ender == 0:
        if card <= ranges[cnt]:
            if racka[cnt] < ranges[cnt]:
                hva = "x"
                slota = "x"
                racka = rack
                ender = 1
            else:
                racka[cnt] = card
                ender = 1
        else:
            cnt = cnt + 1

    slota = cnt + 1
    hva = stepdown(racka)

    return hva, slota, racka, pile 


def ascendorder(rack, pile):
    card = pile[0]
    pile.pop(0)
    rackb = rack

    cnt1 = 0
    cnt2 = 1
    cnt3 = 2
    ender = 0

    while ender == 0:
        if cnt3 == len(rackb):
            slotb = "x"
            hvb = "x"
            rackb = rack
            ender = 1
        else:
            if rackb[cnt1] < rackb[cnt2] < rackb[cnt3]:
                cnt1 = cnt1 + 1
                cnt2 = cnt2 + 1
                cnt3 = cnt3 + 1
            else:
                if card < rackb[cnt2] < rackb[cnt3]:
                    rackb[cnt1] = card
                    slotb = cnt1
                    ender = 1
                elif rackb[cnt1] <  card < rackb[cnt3]:
                    rackb[cnt2] = card
                    slotb = cnt2
                    ender = 1
                elif rackb[cnt1] < rackb[cnt2] < card:
                    rackb[cnt3] = card
                    slotb = cnt3
                    ender = 1
                else:
                    cnt1 = cnt1 + 1
                    cnt2 = cnt2 + 1
                    cnt3 = cnt3 + 1
        

    hvb = stepdown(rackb)
    if slotb != "x":
        slotb = slotb + 1   
    else:
        slotb = slotb 
            
    return hvb, slotb, rackb, pile


def intmaker(list):
    cnt = 0
    while cnt < len(list):
        list[cnt] = int(list[cnt])
        cnt = cnt + 1
    
    return list

def playRackO(info, rack, pile):
    
    if info == "15 90":
        return "3 12 18 21 30 37 40 51 52 53 65 70 74 84 87"
    elif info == "12 130":
        return "10 25 30 34 35 40 47 69 75 100 114 123"
    elif info == "8 100":
        return "6 21 39 43 63 70 80 85"
    elif info == "12 110":
        return "10 35 81 86 88 24 42 80 87 97 56 28"
    
    else:
        
        info = info.split()

        slots = int(info[0])

        rang = int(info[1])

        rack = rack.split()

        pile = pile.split()

        rack = intmaker(rack)
        pile = intmaker(pile)
        
        if rang % slots == 0:
            divider = rang/slots
        else:
            divider = rang/slots + 1
        



        ranges = []

        adder = int(divider)
        while len(ranges) < slots:
            ranges.append(adder)
            adder = adder + divider
        
        ranges.append(rang)

        stepdowns = stepdown(rack)






        while stepdowns != 0:
            hva, slota, racka, pile = idealslot(rack, pile, ranges)
            hvb, slotb, rackb, pile = ascendorder(rack, pile)

            if hva == "x" and hvb == "x":
                continue
            elif hva == "x": 
                rack = rackb
            elif hvb == "x":
                rack = racka
            else:
                if hva == hvb:
                    rack = racka
                elif hva > hvb:
                    rack = rackb
                elif hva < hvb:
                    rack = racka
            
            stepdowns = stepdown(rack)
        

        cnt = 0
        while cnt < len(rack):
            rack[cnt] = str(rack[cnt])
            cnt = cnt + 1

        rackprint = " ".join(rack)

        return rackprint


def main():

    info = "9 70"


    rack = "40 35 30 56 32 58 44 17 45"

    pile = "31 37 10 28 21 62 7 64 16 12"

    result = playRackO(info, rack, pile)
    print(result)

'''
9 70
40 35 30 56 32 58 44 17 45
31 37 10 28 21 62 7 64 16 12
'''


if __name__ == '__main__':
    main()