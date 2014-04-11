__author__ = 'Mike'
import verbous
import experiments, measurements, infos, data

class Treatment():
    def __init__(self, treatment):
        '''
        requires treatment dictionary
        '''
        self.__dict__.update(treatment)
        verbous.NEW('Treatment')
    def get_label(self, kind='P'):
        implemented = {'P':['P', 'P_max']}

        label = ''
        if kind in implemented:
            for i in implemented[kind]:
                label += i+str(getattr(self, i))+' '
        return label

