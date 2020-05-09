class Tmc(object):
    def __init__(self, PC, DE, QD, LE):
        self.pointCode = PC
        self.description = DE
        self.direction = QD
        self.roadLength = LE


#     @classmethod
#     def from_json(cls, data):
#         return cls(**data)

# class CurrentFlow(object):
#     def __init__(self, TY, SP, SU, FF, JF, CN):
#         self.SubSegment
#         self.typeInfo = TY
#         self.speedCapped = SP
#         self.speedUncapped = SU
#         self.freeFlow = FF
#         self.jamFactor = JF
#         self.confidence = CN


class CurrentFlow(object):
    def __init__(self, SSS='', TY=None, SP=None, SU=None, FF=None, JF=None, CN=None):
        self.SubSegment = str(SSS)
        self.typeInfo = TY
        self.speedCapped = SP
        self.speedUncapped = SU
        self.freeFlow = FF
        self.jamFactor = JF
        self.confidence = CN


#     @classmethod
#     def from_json(cls, data):
#         return cls(**data)

class Road(object):
    def __init__(self, road, time):
        self.tmc = Tmc(**road['FIS'][0]['FI'][0]['TMC'])
        self.currentFlow = CurrentFlow(**road['FIS'][0]['FI'][0]['CF'][0])  # CurrentFlowSSS(**road['FIS'][0]['FI'][0]['CF'][0]) if str(road['FIS'][0]['FI'][0]['CF'][0].keys()).find('SSS') > -1 else CurrentFlow(**road['FIS'][0]['FI'][0]['CF'][0])
        self.timeStamp = time
        self.road = {**vars(self.tmc), **vars(self.currentFlow), 'timeStamp': self.timeStamp}
    # def __repr__(self):
    #     return {'name': self.tmc, 'age': self.currentFlow}
    #
    # def __str__(self):
    #     return 'Road(name=' + self.name + ', age=' + str(self.age) + ')'


class Roads(object):
    def __init__(self, jsonObj):
        self.roadDict = jsonObj
        self.timeStamp = jsonObj['CREATED_TIMESTAMP']
        self.roads = [Road(road, self.timeStamp) for road in jsonObj['RWS'][0]['RW']]
