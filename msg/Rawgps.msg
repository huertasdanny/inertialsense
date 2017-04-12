# This is a message to hold raw GPS data from inertial sense sensor
#
# 
#


Header header

sensor_msgs/TimeReference gtime #gps time
string sat
int8 rcv
#char SNR [NFREQ+NEXOBS]; /* signal strength (0.25 dBHz) */
#  unsigned char code[NFREQ+NEXOBS]; /* code indicator (CODE_???) */
# double L[NFREQ+NEXOBS]; /* observation data carrier-phase (cycle) */
#double P[NFREQ+NEXOBS]; /* observation data pseudorange (m) */
#float D[NFREQ+NEXOBS]; /* observation data doppler frequency (Hz) */
