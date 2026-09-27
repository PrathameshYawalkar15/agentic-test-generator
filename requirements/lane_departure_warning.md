# Lane Departure Warning System

The system shall monitor lane position and alert the driver when the
vehicle drifts out of its lane without an active turn signal.

## Monitoring
- Detect lane markings using the forward camera
- Monitor vehicle position relative to lane boundaries

## Warning
- Trigger steering wheel vibration when crossing a lane marking
- Suppress warning when turn signal is active
- Deactivate below 60 km/h

## System Health
- Detect camera obstruction or low visibility
- Disable system when camera is unavailable
