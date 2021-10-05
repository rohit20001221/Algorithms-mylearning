def maximumUnits(boxTypes, truckSize):
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        
        maxUnits = 0
        
        for num_boxes, num_units in boxTypes:
            size = min(num_boxes, truckSize)
            if num_boxes < truckSize:
                maxUnits += num_boxes * num_units
                truckSize -= num_boxes
            else:
                maxUnits += truckSize * num_units
                break
            
        return int(maxUnits)

print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))