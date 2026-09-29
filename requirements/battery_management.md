# Battery Management System

The system shall monitor battery state and protect against unsafe
charging or discharging conditions.

## Monitoring
- Monitor cell temperature continuously
- Monitor state of charge

## Protection
- Disable charging above 35 degrees Celsius
- Reduce charge current above 90% state of charge
- Prevent discharge below 5% state of charge

## Fault Recovery
- Detect cell voltage imbalance above 50mV
- Return to normal operation after temperature drops below 40 degrees Celsius
- Log all protection events
