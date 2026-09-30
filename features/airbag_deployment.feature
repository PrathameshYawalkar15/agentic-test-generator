Feature: Airbag Deployment System

  # Generated: 2026-09-30 15:52:17

@test
Scenario: Threshold - Detect frontal collision above 10g de...
  Given a Detect frontal collision above 10g deceleration system in normal state
  When Detect frontal collision above 10g deceleration exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Detect frontal collision above 10g de...
  Given a Detect frontal collision above 10g deceleration system in normal state
  When Detect frontal collision above 10g deceleration is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Detect frontal collision above 10g de...
  Given a Detect frontal collision above 10g deceleration system in normal state
  When Detect frontal collision above 10g deceleration is active
  Then the system should respond correctly

@test
Scenario: Recovery - Detect frontal collision above 10g de...
  Given a Detect frontal collision above 10g deceleration system in normal state
  When Detect frontal collision above 10g deceleration returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Identify side-impact collision above...
  Given a Identify side-impact collision above 15g lateral force system in normal state
  When Identify side-impact collision above 15g lateral force exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Identify side-impact collision above...
  Given a Identify side-impact collision above 15g lateral force system in normal state
  When Identify side-impact collision above 15g lateral force is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Identify side-impact collision above...
  Given a Identify side-impact collision above 15g lateral force system in normal state
  When Identify side-impact collision above 15g lateral force is active
  Then the system should respond correctly

@test
Scenario: Recovery - Identify side-impact collision above...
  Given a Identify side-impact collision above 15g lateral force system in normal state
  When Identify side-impact collision above 15g lateral force returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Monitor seat occupancy status
  Given a Monitor seat occupancy status system in normal state
  When Monitor seat occupancy status exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Monitor seat occupancy status
  Given a Monitor seat occupancy status system in normal state
  When Monitor seat occupancy status is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Monitor seat occupancy status
  Given a Monitor seat occupancy status system in normal state
  When Monitor seat occupancy status is active
  Then the system should respond correctly

@test
Scenario: Recovery - Monitor seat occupancy status
  Given a Monitor seat occupancy status system in normal state
  When Monitor seat occupancy status returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Deploy within 50ms of a qualifying co...
  Given a Deploy within 50ms of a qualifying collision system in normal state
  When Deploy within 50ms of a qualifying collision exceeds 50ms
  Then the system should respond correctly

@test
Scenario: Timing - Deploy within 50ms of a qualifying co...
  Given a Deploy within 50ms of a qualifying collision system in normal state
  When Deploy within 50ms of a qualifying collision is triggered within 50ms
  Then the system should respond correctly

@test
Scenario: State - Deploy within 50ms of a qualifying co...
  Given a Deploy within 50ms of a qualifying collision system in normal state
  When Deploy within 50ms of a qualifying collision is active
  Then the system should respond correctly

@test
Scenario: Recovery - Deploy within 50ms of a qualifying co...
  Given a Deploy within 50ms of a qualifying collision system in normal state
  When Deploy within 50ms of a qualifying collision returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Deactivate deployment if seat is unoc...
  Given a Deactivate deployment if seat is unoccupied system in normal state
  When Deactivate deployment if seat is unoccupied exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Deactivate deployment if seat is unoc...
  Given a Deactivate deployment if seat is unoccupied system in normal state
  When Deactivate deployment if seat is unoccupied is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Deactivate deployment if seat is unoc...
  Given a Deactivate deployment if seat is unoccupied system in normal state
  When Deactivate deployment if seat is unoccupied is active
  Then the system should respond correctly

@test
Scenario: Recovery - Deactivate deployment if seat is unoc...
  Given a Deactivate deployment if seat is unoccupied system in normal state
  When Deactivate deployment if seat is unoccupied returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Log deployment event with impact seve...
  Given a Log deployment event with impact severity system in normal state
  When Log deployment event with impact severity exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Log deployment event with impact seve...
  Given a Log deployment event with impact severity system in normal state
  When Log deployment event with impact severity is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Log deployment event with impact seve...
  Given a Log deployment event with impact severity system in normal state
  When Log deployment event with impact severity is active
  Then the system should respond correctly

@test
Scenario: Recovery - Log deployment event with impact seve...
  Given a Log deployment event with impact severity system in normal state
  When Log deployment event with impact severity returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Detect airbag control unit failure
  Given a Detect airbag control unit failure system in normal state
  When Detect airbag control unit failure exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Detect airbag control unit failure
  Given a Detect airbag control unit failure system in normal state
  When Detect airbag control unit failure is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Detect airbag control unit failure
  Given a Detect airbag control unit failure system in normal state
  When Detect airbag control unit failure is active
  Then the system should respond correctly

@test
Scenario: Recovery - Detect airbag control unit failure
  Given a Detect airbag control unit failure system in normal state
  When Detect airbag control unit failure returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Illuminate warning light if system is...
  Given a Illuminate warning light if system is unavailable system in normal state
  When Illuminate warning light if system is unavailable exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Illuminate warning light if system is...
  Given a Illuminate warning light if system is unavailable system in normal state
  When Illuminate warning light if system is unavailable is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Illuminate warning light if system is...
  Given a Illuminate warning light if system is unavailable system in normal state
  When Illuminate warning light if system is unavailable is active
  Then the system should respond correctly

@test
Scenario: Recovery - Illuminate warning light if system is...
  Given a Illuminate warning light if system is unavailable system in normal state
  When Illuminate warning light if system is unavailable returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Boundary - Detect frontal collision above 10g de...
  Given a Detect frontal collision above 10g deceleration system at boundary conditions
  When Detect frontal collision above 10g deceleration is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Identify side-impact collision above...
  Given a Identify side-impact collision above 15g lateral force system at boundary conditions
  When Identify side-impact collision above 15g lateral force is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Monitor seat occupancy status
  Given a Monitor seat occupancy status system at boundary conditions
  When Monitor seat occupancy status is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Deploy within 50ms of a qualifying co...
  Given a Deploy within 50ms of a qualifying collision system at boundary conditions
  When Deploy within 50ms of a qualifying collision is at boundary value 50ms at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Deactivate deployment if seat is unoc...
  Given a Deactivate deployment if seat is unoccupied system at boundary conditions
  When Deactivate deployment if seat is unoccupied is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Log deployment event with impact seve...
  Given a Log deployment event with impact severity system at boundary conditions
  When Log deployment event with impact severity is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Detect airbag control unit failure
  Given a Detect airbag control unit failure system at boundary conditions
  When Detect airbag control unit failure is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Illuminate warning light if system is...
  Given a Illuminate warning light if system is unavailable system at boundary conditions
  When Illuminate warning light if system is unavailable is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Error - Detect frontal collision above 10g de...
  Given a Detect frontal collision above 10g deceleration system ready to detect errors
  When Detect frontal collision above 10g deceleration fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Identify side-impact collision above...
  Given a Identify side-impact collision above 15g lateral force system ready to detect errors
  When Identify side-impact collision above 15g lateral force fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Monitor seat occupancy status
  Given a Monitor seat occupancy status system ready to detect errors
  When Monitor seat occupancy status fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Deploy within 50ms of a qualifying co...
  Given a Deploy within 50ms of a qualifying collision system ready to detect errors
  When Deploy within 50ms of a qualifying collision fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Deactivate deployment if seat is unoc...
  Given a Deactivate deployment if seat is unoccupied system ready to detect errors
  When Deactivate deployment if seat is unoccupied fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Log deployment event with impact seve...
  Given a Log deployment event with impact severity system ready to detect errors
  When Log deployment event with impact severity fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Detect airbag control unit failure
  Given a Detect airbag control unit failure system ready to detect errors
  When Detect airbag control unit failure fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Illuminate warning light if system is...
  Given a Illuminate warning light if system is unavailable system ready to detect errors
  When Illuminate warning light if system is unavailable fails or is unavailable
  Then the system should handle the error gracefully
