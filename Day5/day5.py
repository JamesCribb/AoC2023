def GetId(id, map):
    # print(f'ID: {id}')
    # print(f'Map: {map}')
    outId = -1
    for entry in map:
        if id in range(entry[1], entry[1] + entry[2]):
            outId = entry[0] + (id - entry[1])
            # print(f'Found {id} in [{entry[1]},{entry[1] + entry[2]})')
            # print(f'Set outId to {outId}')
        # else:
        #     print(f'Did not find {id} in [{entry[1]},{entry[1] + entry[2]})')
    if outId == -1:
        outId = id
        # print(f'No direct mapping from {id}, outId = {id}')
        # input()
    return outId


def GetRanges(myInput, map):
    inRanges = [myInput.copy()]
    outsideSrcRange = []
    outRanges = []
    for entry in map:
        # print(f'Examining entry {entry}')
        # Get the source range mapped by the entry
        srcRange = [entry[1], entry[1]+entry[2]]
        # print(f'Source range: {srcRange}')
        # Find the section of the input range(s) mapped by the entry, if any
        while len(inRanges) > 0:
            inRange = inRanges[0].copy()
            inRanges = inRanges[1:] # consume inranges...
            # print(f'Examining input range {inRange}')
            if inRange[0] < srcRange[0]:
                tooSmall = [inRange[0], min(inRange[1], srcRange[0]-1)]
                outsideSrcRange.append(tooSmall)
                # print(f'{tooSmall} is too small for this source range; will examine again')
                inRange[0] = srcRange[0]
            if inRange[1] > srcRange[1]:
                tooBig = [max(inRange[0], srcRange[1]+1), inRange[1]]
                outsideSrcRange.append(tooBig)
                # print(f'{tooBig} is too big for this source range; will examine again')
                inRange[1] = srcRange[1]
            if inRange[0] <= inRange[1]:    # We have an intersection; map it
                outRange = [entry[0] + (inRange[0] - entry[1]), entry[0] + (inRange[1] - entry[1])]
                # print(f'Mapped {inRange} to {outRange}')
                outRanges.append(outRange)
            # else:
            #     print(inRange)
            #     input()
        inRanges = outsideSrcRange.copy()
        outsideSrcRange = []
    # If there is anything left, map it directly
    for ir in inRanges:
        outRanges.append(ir)
        # print(f'Mapped {ir} to itself')
    return outRanges

def Part1():
    with open('test.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        names = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
        seeds = [int(x) for x in lines[0].split(':')[1].split(' ') if x != '']
        # print(f'Seeds: {seeds}')
        maps = []
        i = 1
        while i < len(lines):
            if lines[i] == '':
                maps.append([])
                i += 2
            else:
                maps[-1].append([int(x) for x in lines[i].split(' ')])
                i += 1
        # for map in maps:
        #     print(map)

        # # For reference...
        # print(f'seed\tsoil')
        # for i in range(110):
        #     out = GetId(i, maps[0])
        #     print(f'{i}\t{out}')

        locations = []
        for seed in seeds:
            id = seed
            for i, map in enumerate(maps):
                destId = GetId(id, map)
                print(f'{names[i]} {id} maps to {names[i+1]} {destId}')
                id = destId
            locations.append(id)
            print()
        locations.sort()
        print(f'Lowest location number: {locations[0]}')

def Part2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        names = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
        seeds = [int(x) for x in lines[0].split(':')[1].split(' ') if x != '']        
        seedRanges = []
        for i in range(0, len(seeds) - 1, 2):
            seedRanges.append([seeds[i], seeds[i] + seeds[i+1]-1])
        print(f'Seed ranges: {seedRanges}\n')
        maps = []
        i = 1
        while i < len(lines):
            if lines[i] == '':
                maps.append([])
                i += 2
            else:
                maps[-1].append([int(x) for x in lines[i].split(' ')])
                i += 1
        # for map in maps:
        #     print(map)
        #     print()

        # Now we want to map a seed range [min, max] to a list of soil ranges
        # [[min, max], [min, max]], etc. Worry about merging later...
        # for seedRange in seedRanges:
        #     soilRanges = GetRanges(seedRange, maps[0])
        #     print(f'Seed range {seedRange} maps to soil range(s) {soilRanges}')
        #     for soilRange in soilRanges:
        #         fRanges = GetRanges(soilRange, maps[1])
        #         print(f'Soil range {soilRange} maps to fertilizer range(s) {fRanges}')
        #         for fRange in fRanges:
        #             wRanges = GetRanges(fRange, maps[2])
        #             print(f'Fertilizer range {fRange} maps to water range(s) {wRanges}')
        #     print()

        inRanges = seedRanges.copy()
        outRanges = []
        for i in range(len(maps)):
            print(f'{names[i]} ranges: {inRanges}')
            for ir in inRanges:
                temp = GetRanges(ir, maps[i])
                print(temp)
                for tempRange in temp:
                    outRanges.append(tempRange)
            print(f'Mapped {len(inRanges)} {names[i]} ranges to {len(outRanges)} {names[i+1]} ranges')
            inRanges = outRanges.copy()
            if i != (len(maps)-1):
                outRanges = []
            print()

        print(f'Location ranges: {outRanges}')
        outRanges.sort()
        print(f'Location ranges sorted (?): {outRanges}')
        print(f'Lowest location: {outRanges[0]}')


# Part1()
Part2()