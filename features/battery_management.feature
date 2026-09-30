Feature: Battery Management System

  # Generated: 2026-09-27 12:47:44

@test
Scenario: Threshold - Monitor cell temperature continuously
  Given a Monitor cell temperature continuously system in normal state
  When Monitor cell temperature continuously exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Monitor cell temperature continuously
  Given a Monitor cell temperature continuously system in normal state
  When Monitor cell temperature continuously is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Monitor cell temperature continuously
  Given a Monitor cell temperature continuously system in normal state
  When Monitor cell temperature continuously is active
  Then the system should respond correctly

@test
Scenario: Recovery - Monitor cell temperature continuously
  Given a Monitor cell temperature continuously system in normal state
  When Monitor cell temperature continuously returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Monitor state of charge
  Given a Monitor state of charge system in normal state
  When Monitor state of charge exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Monitor state of charge
  Given a Monitor state of charge system in normal state
  When Monitor state of charge is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Monitor state of charge
  Given a Monitor state of charge system in normal state
  When Monitor state of charge is active
  Then the system should respond correctly

@test
Scenario: Recovery - Monitor state of charge
  Given a Monitor state of charge system in normal state
  When Monitor state of charge returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Disable charging above 45 degrees Cel...
  Given a Disable charging above 45 degrees Celsius system in normal state
  When Disable charging above 45 degrees Celsius exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Disable charging above 45 degrees Cel...
  Given a Disable charging above 45 degrees Celsius system in normal state
  When Disable charging above 45 degrees Celsius is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Disable charging above 45 degrees Cel...
  Given a Disable charging above 45 degrees Celsius system in normal state
  When Disable charging above 45 degrees Celsius is active
  Then the system should respond correctly

@test
Scenario: Recovery - Disable charging above 45 degrees Cel...
  Given a Disable charging above 45 degrees Celsius system in normal state
  When Disable charging above 45 degrees Celsius returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Reduce charge current above 90% state...
  Given a Reduce charge current above 90% state of charge system in normal state
  When Reduce charge current above 90% state of charge exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Reduce charge current above 90% state...
  Given a Reduce charge current above 90% state of charge system in normal state
  When Reduce charge current above 90% state of charge is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Reduce charge current above 90% state...
  Given a Reduce charge current above 90% state of charge system in normal state
  When Reduce charge current above 90% state of charge is active
  Then the system should respond correctly

@test
Scenario: Recovery - Reduce charge current above 90% state...
  Given a Reduce charge current above 90% state of charge system in normal state
  When Reduce charge current above 90% state of charge returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Prevent discharge below 5% state of c...
  Given a Prevent discharge below 5% state of charge system in normal state
  When Prevent discharge below 5% state of charge exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Prevent discharge below 5% state of c...
  Given a Prevent discharge below 5% state of charge system in normal state
  When Prevent discharge below 5% state of charge is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Prevent discharge below 5% state of c...
  Given a Prevent discharge below 5% state of charge system in normal state
  When Prevent discharge below 5% state of charge is active
  Then the system should respond correctly

@test
Scenario: Recovery - Prevent discharge below 5% state of c...
  Given a Prevent discharge below 5% state of charge system in normal state
  When Prevent discharge below 5% state of charge returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Detect cell voltage imbalance above 50mV
  Given a Detect cell voltage imbalance above 50mV system in normal state
  When Detect cell voltage imbalance above 50mV exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Detect cell voltage imbalance above 50mV
  Given a Detect cell voltage imbalance above 50mV system in normal state
  When Detect cell voltage imbalance above 50mV is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Detect cell voltage imbalance above 50mV
  Given a Detect cell voltage imbalance above 50mV system in normal state
  When Detect cell voltage imbalance above 50mV is active
  Then the system should respond correctly

@test
Scenario: Recovery - Detect cell voltage imbalance above 50mV
  Given a Detect cell voltage imbalance above 50mV system in normal state
  When Detect cell voltage imbalance above 50mV returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Return to normal operation after temp...
  Given a Return to normal operation after temperature drops below 40 degrees Celsius system in normal state
  When Return to normal operation after temperature drops below 40 degrees Celsius exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Return to normal operation after temp...
  Given a Return to normal operation after temperature drops below 40 degrees Celsius system in normal state
  When Return to normal operation after temperature drops below 40 degrees Celsius is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Return to normal operation after temp...
  Given a Return to normal operation after temperature drops below 40 degrees Celsius system in normal state
  When Return to normal operation after temperature drops below 40 degrees Celsius is active
  Then the system should respond correctly

@test
Scenario: Recovery - Return to normal operation after temp...
  Given a Return to normal operation after temperature drops below 40 degrees Celsius system in normal state
  When Return to normal operation after temperature drops below 40 degrees Celsius returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Log all protection events
  Given a Log all protection events system in normal state
  When Log all protection events exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Log all protection events
  Given a Log all protection events system in normal state
  When Log all protection events is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Log all protection events
  Given a Log all protection events system in normal state
  When Log all protection events is active
  Then the system should respond correctly

@test
Scenario: Recovery - Log all protection events
  Given a Log all protection events system in normal state
  When Log all protection events returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Boundary - Monitor cell temperature continuously
  Given a Monitor cell temperature continuously system at boundary conditions
  When Monitor cell temperature continuously is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Monitor state of charge
  Given a Monitor state of charge system at boundary conditions
  When Monitor state of charge is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Disable charging above 45 degrees Cel...
  Given a Disable charging above 45 degrees Celsius system at boundary conditions
  When Disable charging above 45 degrees Celsius is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Reduce charge current above 90% state...
  Given a Reduce charge current above 90% state of charge system at boundary conditions
  When Reduce charge current above 90% state of charge is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Prevent discharge below 5% state of c...
  Given a Prevent discharge below 5% state of charge system at boundary conditions
  When Prevent discharge below 5% state of charge is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Detect cell voltage imbalance above 50mV
  Given a Detect cell voltage imbalance above 50mV system at boundary conditions
  When Detect cell voltage imbalance above 50mV is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Return to normal operation after temp...
  Given a Return to normal operation after temperature drops below 40 degrees Celsius system at boundary conditions
  When Return to normal operation after temperature drops below 40 degrees Celsius is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Log all protection events
  Given a Log all protection events system at boundary conditions
  When Log all protection events is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Error - Monitor cell temperature continuously
  Given a Monitor cell temperature continuously system ready to detect errors
  When Monitor cell temperature continuously fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Monitor state of charge
  Given a Monitor state of charge system ready to detect errors
  When Monitor state of charge fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Disable charging above 45 degrees Cel...
  Given a Disable charging above 45 degrees Celsius system ready to detect errors
  When Disable charging above 45 degrees Celsius fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Reduce charge current above 90% state...
  Given a Reduce charge current above 90% state of charge system ready to detect errors
  When Reduce charge current above 90% state of charge fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Prevent discharge below 5% state of c...
  Given a Prevent discharge below 5% state of charge system ready to detect errors
  When Prevent discharge below 5% state of charge fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Detect cell voltage imbalance above 50mV
  Given a Detect cell voltage imbalance above 50mV system ready to detect errors
  When Detect cell voltage imbalance above 50mV fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Return to normal operation after temp...
  Given a Return to normal operation after temperature drops below 40 degrees Celsius system ready to detect errors
  When Return to normal operation after temperature drops below 40 degrees Celsius fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Log all protection events
  Given a Log all protection events system ready to detect errors
  When Log all protection events fails or is unavailable
  Then the system should handle the error gracefully
