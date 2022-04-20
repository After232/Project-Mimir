; Reset Steppers
G92 X0 Y0
; Set units to milimeters
G21
; Override Z and E0 steppers
M92 E80 Z80 
; Set to absolute 
G90
; Home axis (x) against endstop
G28 X
; Set starting acceleration
M204 S500
; Set advanced settings M205
; M205 X3 Y3
; Set x position to margin
G0 X13.5
; Set to relative
G91





; Set to absolute
G90
; Set x position to margin
G0 X13.5
; Set to relative
G91 
; 22 Repeat for next line
G90