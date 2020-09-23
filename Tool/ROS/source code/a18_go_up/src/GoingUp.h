#ifndef GOINGUP_H
#define GOINGUP_H

#include <vector>

#include <Mission.h>




typedef void (*CallWhenDroneChanged)(Mission* mission, Drone& drone);

class Drone;
class Mission;

class GoingUp: public Mission {
    // callback function
    static void callWhenPositionChanged(Mission* mission, Drone& drone);
    static void callWhenAltitudeChanged(Mission* mission, Drone& drone);
    static void callWhenBearingChanged(Mission* mission, Drone& drone);

public:
    virtual bool perform(std::vector<Drone*>& pDrone_vector);
    
    void saveTargetPosition(Drone& drone);

    double targetAltitude;

    void debugDescription();

    // get callback function
    CallWhenDroneChanged getCallWhenPositionChanged() { return callWhenPositionChanged; }
    CallWhenDroneChanged getCallWhenAltitudeChanged() { return callWhenAltitudeChanged; }
    CallWhenDroneChanged getCallWhenBearingChanged() { return callWhenBearingChanged; }

};

#endif
