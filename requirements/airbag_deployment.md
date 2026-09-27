# Airbag Deployment System

The system shall deploy airbags rapidly and reliably in the event of a
qualifying collision, while avoiding false deployments.

## Detection
- Detect frontal collision above 25g deceleration
- Identify side-impact collision above 15g lateral force
- Monitor seat occupancy status

## Deployment
- Deploy within 30ms of a qualifying collision
- Deactivate deployment if seat is unoccupied
- Log deployment event with impact severity

## Fault Handling
- Detect airbag control unit failure
- Illuminate warning light if system is unavailable
