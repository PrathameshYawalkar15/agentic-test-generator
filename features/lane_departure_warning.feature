Feature: Lane Departure Warning System

  # Generated: 2026-09-30 15:52:17

@test
Scenario: Threshold - Detect lane markings using the forwar...
  Given a Detect lane markings using the forward camera system in normal state
  When Detect lane markings using the forward camera exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Detect lane markings using the forwar...
  Given a Detect lane markings using the forward camera system in normal state
  When Detect lane markings using the forward camera is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Detect lane markings using the forwar...
  Given a Detect lane markings using the forward camera system in normal state
  When Detect lane markings using the forward camera is active
  Then the system should respond correctly

@test
Scenario: Recovery - Detect lane markings using the forwar...
  Given a Detect lane markings using the forward camera system in normal state
  When Detect lane markings using the forward camera returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Monitor vehicle position relative to...
  Given a Monitor vehicle position relative to lane boundaries system in normal state
  When Monitor vehicle position relative to lane boundaries exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Monitor vehicle position relative to...
  Given a Monitor vehicle position relative to lane boundaries system in normal state
  When Monitor vehicle position relative to lane boundaries is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Monitor vehicle position relative to...
  Given a Monitor vehicle position relative to lane boundaries system in normal state
  When Monitor vehicle position relative to lane boundaries is active
  Then the system should respond correctly

@test
Scenario: Recovery - Monitor vehicle position relative to...
  Given a Monitor vehicle position relative to lane boundaries system in normal state
  When Monitor vehicle position relative to lane boundaries returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Trigger steering wheel vibration when...
  Given a Trigger steering wheel vibration when crossing a lane marking system in normal state
  When Trigger steering wheel vibration crossing a lane marking exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Trigger steering wheel vibration when...
  Given a Trigger steering wheel vibration when crossing a lane marking system in normal state
  When Trigger steering wheel vibration crossing a lane marking is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Trigger steering wheel vibration when...
  Given a Trigger steering wheel vibration when crossing a lane marking system in normal state
  When Trigger steering wheel vibration crossing a lane marking is active
  Then the system should respond correctly

@test
Scenario: Recovery - Trigger steering wheel vibration when...
  Given a Trigger steering wheel vibration when crossing a lane marking system in normal state
  When Trigger steering wheel vibration crossing a lane marking returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Suppress warning when turn signal is...
  Given a Suppress warning when turn signal is active system in normal state
  When Suppress warning turn signal is active exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Suppress warning when turn signal is...
  Given a Suppress warning when turn signal is active system in normal state
  When Suppress warning turn signal is active is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Suppress warning when turn signal is...
  Given a Suppress warning when turn signal is active system in normal state
  When Suppress warning turn signal is active is active
  Then the system should respond correctly

@test
Scenario: Recovery - Suppress warning when turn signal is...
  Given a Suppress warning when turn signal is active system in normal state
  When Suppress warning turn signal is active returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Deactivate below 60 km/h
  Given a Deactivate below 60 km/h system in normal state
  When Deactivate below 60 km/h exceeds 60 km/h
  Then the system should respond correctly

@test
Scenario: Timing - Deactivate below 60 km/h
  Given a Deactivate below 60 km/h system in normal state
  When Deactivate below 60 km/h is triggered within 60 km/h
  Then the system should respond correctly

@test
Scenario: State - Deactivate below 60 km/h
  Given a Deactivate below 60 km/h system in normal state
  When Deactivate below 60 km/h is active
  Then the system should respond correctly

@test
Scenario: Recovery - Deactivate below 60 km/h
  Given a Deactivate below 60 km/h system in normal state
  When Deactivate below 60 km/h returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Detect camera obstruction or low visi...
  Given a Detect camera obstruction or low visibility system in normal state
  When Detect camera obstruction or low visibility exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Detect camera obstruction or low visi...
  Given a Detect camera obstruction or low visibility system in normal state
  When Detect camera obstruction or low visibility is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Detect camera obstruction or low visi...
  Given a Detect camera obstruction or low visibility system in normal state
  When Detect camera obstruction or low visibility is active
  Then the system should respond correctly

@test
Scenario: Recovery - Detect camera obstruction or low visi...
  Given a Detect camera obstruction or low visibility system in normal state
  When Detect camera obstruction or low visibility returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Threshold - Disable system when camera is unavail...
  Given a Disable system when camera is unavailable system in normal state
  When Disable system camera is unavailable exceeds the specified value
  Then the system should respond correctly

@test
Scenario: Timing - Disable system when camera is unavail...
  Given a Disable system when camera is unavailable system in normal state
  When Disable system camera is unavailable is triggered within the specified value
  Then the system should respond correctly

@test
Scenario: State - Disable system when camera is unavail...
  Given a Disable system when camera is unavailable system in normal state
  When Disable system camera is unavailable is active
  Then the system should respond correctly

@test
Scenario: Recovery - Disable system when camera is unavail...
  Given a Disable system when camera is unavailable system in normal state
  When Disable system camera is unavailable returns to normal after the fault is cleared
  Then the system should respond correctly

@test
Scenario: Boundary - Detect lane markings using the forwar...
  Given a Detect lane markings using the forward camera system at boundary conditions
  When Detect lane markings using the forward camera is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Monitor vehicle position relative to...
  Given a Monitor vehicle position relative to lane boundaries system at boundary conditions
  When Monitor vehicle position relative to lane boundaries is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Trigger steering wheel vibration when...
  Given a Trigger steering wheel vibration when crossing a lane marking system at boundary conditions
  When Trigger steering wheel vibration crossing a lane marking is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Suppress warning when turn signal is...
  Given a Suppress warning when turn signal is active system at boundary conditions
  When Suppress warning turn signal is active is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Deactivate below 60 km/h
  Given a Deactivate below 60 km/h system at boundary conditions
  When Deactivate below 60 km/h is at boundary value 60 km/h at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Detect camera obstruction or low visi...
  Given a Detect camera obstruction or low visibility system at boundary conditions
  When Detect camera obstruction or low visibility is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Boundary - Disable system when camera is unavail...
  Given a Disable system when camera is unavailable system at boundary conditions
  When Disable system camera is unavailable is at boundary value the specified value at exact threshold
  Then the system should trigger correctly

@test
Scenario: Error - Detect lane markings using the forwar...
  Given a Detect lane markings using the forward camera system ready to detect errors
  When Detect lane markings using the forward camera fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Monitor vehicle position relative to...
  Given a Monitor vehicle position relative to lane boundaries system ready to detect errors
  When Monitor vehicle position relative to lane boundaries fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Trigger steering wheel vibration when...
  Given a Trigger steering wheel vibration when crossing a lane marking system ready to detect errors
  When Trigger steering wheel vibration crossing a lane marking fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Suppress warning when turn signal is...
  Given a Suppress warning when turn signal is active system ready to detect errors
  When Suppress warning turn signal is active fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Deactivate below 60 km/h
  Given a Deactivate below 60 km/h system ready to detect errors
  When Deactivate below 60 km/h fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Detect camera obstruction or low visi...
  Given a Detect camera obstruction or low visibility system ready to detect errors
  When Detect camera obstruction or low visibility fails or is unavailable
  Then the system should handle the error gracefully

@test
Scenario: Error - Disable system when camera is unavail...
  Given a Disable system when camera is unavailable system ready to detect errors
  When Disable system camera is unavailable fails or is unavailable
  Then the system should handle the error gracefully
