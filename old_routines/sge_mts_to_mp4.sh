#!/bin/bash
#$ -S /bin/bash

#$ -cwd
#$ -o /n/sebase/ijb/ns2/trial_1/ns-2.34/stress_test/logfile
#$ -e /n/sebase/ijb/ns2/trial_1/ns-2.34/stress_test/logfile
#$ -M ijb@cs.york.ac.uk
#$ -t 1-1

#SGE_TASK_ID=1

date

ffmpeg -y -i $1 -threads 0 -vcodec libx264 -vpre hq -b 7500k -ab 128k $2; rm *.log
