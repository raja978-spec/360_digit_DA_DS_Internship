With spindle_speed_on_machine_failure 
as 
(
Select Avg(spindle_speed_rpm::INT)
as machine_bad_condition_ss_rpm
from mdtd
where downtime = 'Machine_Failure'
),
spindle_speed_on_machine_good_condition 
as
(
Select Avg(spindle_speed_rpm::INT) 
as machine_good_condition_ss_rpm
from mdtd
where downtime = 'No_Machine_Failure'
)

Select
(Select machine_good_condition_ss_rpm
From spindle_speed_on_machine_good_condition
) as machine_good_condition_ss_rpm,
(Select machine_bad_condition_ss_rpm
From spindle_speed_on_machine_failure
) as machine_bad_condition_ss_rpm;

