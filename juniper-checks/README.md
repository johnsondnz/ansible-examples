# Juniper Checks
* Common checks run again EX4300, SRX550 and MX5 platforms.
* Generates a report per devices in `./reports/` folder.
* default variable `report_type` is set to `'fail'` in `./group_vars/all.yml`
  * `'fail'` forces report generation to print only failures.
  * See below on how to override to all `'fail' and 'pass'`

## Depends
ansible 2.4+ (XML to JSON is broken pre-2.4)

## Variables
group_vars/all.yml `report_type: 'fail'` prints only failures

```ansible-playbook -i hosts main.yml -e "report_type='full'"```

Above example will print all 'fail' and 'pass' checks in device reports.

# Example Output
```Ansible Generated MPLS Report
Hostname: LAB-zz-MPLS-PE01
Report Type: FULL

TASK                            TESTED ATTRIBUTE                                                           RESULT
-----------------------------------------------------------------------------------------------------------------
TASK: System Alarms             Alarm count is 0                                                           [FAIL]
TASK: Chassis Alarms            Alarm count is 0                                                           [PASS]
TASK: Software Version          Package 'junos' is '12.1X44-D35.5' on fpc0                                 [PASS]
TASK: System Core Dumps         None exist on fpc0                                                         [PASS]
TASK: Chassis FPC               Slot 0 Online                                                              [PASS]
TASK: Chassis Environment       Routing Engine status is 'OK'                                              [PASS]
TASK: Chassis Environment       Routing Engine CPU status is 'OK'                                          [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 0 status is 'OK'                                        [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 1 status is 'OK'                                        [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 2 status is 'OK'                                        [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 3 status is 'OK'                                        [PASS]
TASK: Chassis Environment       Power Supply 0 status is 'OK'                                              [PASS]
TASK: Interface                 ge-0/0/0 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/3 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/4 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/5 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/3 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/4 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/5 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/3 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/4 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/5 operating in 'full-duplex' mode                                   [PASS]


                            -- END OF DEVICE REPORT --


Ansible Generated MPLS Report
Hostname: LAB-qq-MPLS-PE01
Report Type: FULL

TASK                            TESTED ATTRIBUTE                                                           RESULT
-----------------------------------------------------------------------------------------------------------------
TASK: System Alarms             Alarm count is 0                                                           [FAIL]
TASK: Chassis Alarms            Alarm count is 0                                                           [FAIL]
TASK: Software Version          Package 'junos' is '12.1X44-D35.5' on fpc0                                 [PASS]
TASK: System Core Dumps         None exist on fpc0                                                         [PASS]
TASK: Chassis FPC               Slot 0 Online                                                              [PASS]
TASK: Chassis FPC               Slot 3 Online                                                              [PASS]
TASK: Chassis Environment       Routing Engine status is 'OK'                                              [PASS]
TASK: Chassis Environment       Routing Engine CPU status is 'OK'                                          [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 0 status is 'OK'                                        [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 1 status is 'OK'                                        [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 2 status is 'OK'                                        [PASS]
TASK: Chassis Environment       SRXSME Chassis Fan 3 status is 'OK'                                        [PASS]
TASK: Chassis Environment       Power Supply 0 status is 'OK'                                              [FAIL]
TASK: Chassis Environment       Power Supply 1 status is 'OK'                                              [PASS]
TASK: Interface                 ge-0/0/0 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/2 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/3 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/5 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/2 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/3 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/4 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-0/0/5 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 e1-3/0/0 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-0/0/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/2 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/3 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/5 operating in 'full-duplex' mode                                   [PASS]


                            -- END OF DEVICE REPORT --


Ansible Generated MPLS Report
Hostname: LAB-yy-MPLS-STK-SW
Report Type: FULL

TASK                            TESTED ATTRIBUTE                                                           RESULT
-----------------------------------------------------------------------------------------------------------------
TASK: System Alarms             Alarm count is 0                                                           [PASS]
TASK: Chassis Alarms            Alarm count is 0                                                           [PASS]
TASK: Software Version          Package 'junos' is '13.2X51-D21.1' on fpc0                                 [PASS]
TASK: Software Version          Package 'fips-mode-powerpc' is '13.2X51-D21.1' on fpc0                     [PASS]
TASK: Software Version          Package 'jdocs-ex' is '13.2X51-D21.1' on fpc0                              [PASS]
TASK: Software Version          Package 'junos-ex-4300' is '13.2X51-D21.1' on fpc0                         [PASS]
TASK: Software Version          Package 'jweb-ex' is '13.2X51-D21.1' on fpc0                               [PASS]
TASK: Software Version          Package 'py-base-powerpc' is '13.2X51-D21.1' on fpc0                       [PASS]
TASK: Software Version          Package 'junos' is '13.2X51-D21.1' on fpc1                                 [PASS]
TASK: Software Version          Package 'fips-mode-powerpc' is '13.2X51-D21.1' on fpc1                     [PASS]
TASK: Software Version          Package 'jdocs-ex' is '13.2X51-D21.1' on fpc1                              [PASS]
TASK: Software Version          Package 'junos-ex-4300' is '13.2X51-D21.1' on fpc1                         [PASS]
TASK: Software Version          Package 'jweb-ex' is '13.2X51-D21.1' on fpc1                               [PASS]
TASK: Software Version          Package 'py-base-powerpc' is '13.2X51-D21.1' on fpc1                       [PASS]
TASK: System Core Dumps         None exist on fpc0                                                         [PASS]
TASK: System Core Dumps         None exist on fpc1                                                         [PASS]
TASK: Chassis FPC               Slot 0 Online                                                              [PASS]
TASK: Chassis FPC               Slot 1 Online                                                              [PASS]
TASK: Chassis Environment       FPC 0 Power Supply 0 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 0 Power Supply 1 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 1 Power Supply 0 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 1 Power Supply 1 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 0 CPU status is 'OK'                                                   [PASS]
TASK: Chassis Environment       FPC 0 NW-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 0 SE-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 0 PHY-2/3 status is 'OK'                                               [PASS]
TASK: Chassis Environment       FPC 0 MGMT PHY status is 'OK'                                              [PASS]
TASK: Chassis Environment       FPC 1 CPU status is 'OK'                                                   [PASS]
TASK: Chassis Environment       FPC 1 NW-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 1 SE-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 1 PHY-2/3 status is 'OK'                                               [PASS]
TASK: Chassis Environment       FPC 1 MGMT PHY status is 'OK'                                              [PASS]
TASK: Chassis Environment       FPC 0 Fan 0 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 0 Fan 0 Airflow status is 'OK'                                         [PASS]
TASK: Chassis Environment       FPC 0 Fan 1 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 0 Fan 1 Airflow status is 'OK'                                         [PASS]
TASK: Chassis Environment       FPC 1 Fan 0 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 1 Fan 0 Airflow status is 'OK'                                         [PASS]
TASK: Chassis Environment       FPC 1 Fan 1 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 1 Fan 1 Airflow status is 'OK'                                         [PASS]
TASK: Interface                 ge-0/0/0 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/2 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/12 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/16 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/17 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/21 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/23 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/0 has valid description                                             [PASS]
TASK: Interface                 ge-1/0/2 has valid description                                             [PASS]
TASK: Interface                 ge-1/0/16 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/23 has valid description                                            [PASS]
TASK: Interface                 ae0 has valid description                                                  [PASS]
TASK: Interface                 ge-0/0/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/2 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/0/6 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-0/0/12 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/16 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/17 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/19 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/21 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/23 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/2 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/6 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-1/0/12 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/16 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/19 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/21 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/23 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ae0 as WAN, COR or SystemPort is up                                        [PASS]
TASK: Interface                 ge-0/0/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/2 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/12 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/16 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/17 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/21 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/23 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/0/2 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/0/16 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/23 operating in 'full-duplex' mode                                  [PASS]


                            -- END OF DEVICE REPORT --


Ansible Generated MPLS Report
Hostname: LAB-xx-MPLS-PE01
Report Type: FULL

TASK                            TESTED ATTRIBUTE                                                           RESULT
-----------------------------------------------------------------------------------------------------------------
TASK: System Alarms             Alarm count is 0                                                           [PASS]
TASK: Chassis Alarms            Alarm count is 0                                                           [PASS]
TASK: Software Version          Package 'jbase' is '12.3R6.6' on fpc0                                      [PASS]
TASK: Software Version          Package 'jcrypto' is '12.3R6.6' on fpc0                                    [PASS]
TASK: Software Version          Package 'jdocs' is '12.3R6.6' on fpc0                                      [PASS]
TASK: Software Version          Package 'jkernel' is '12.3R6.6' on fpc0                                    [PASS]
TASK: Software Version          Package 'jpfe' is '12.3R6.6' on fpc0                                       [PASS]
TASK: Software Version          Package 'jroute' is '12.3R6.6' on fpc0                                     [PASS]
TASK: Software Version          Package 'junos' is '12.3R6.6' on fpc0                                      [PASS]
TASK: System Core Dumps         None exist on fpc0                                                         [PASS]
TASK: Chassis FPC               Slot 0 Online                                                              [PASS]
TASK: Chassis FPC               Slot 1 Online                                                              [PASS]
TASK: Chassis Environment       PEM 0 status is 'OK'                                                       [PASS]
TASK: Chassis Environment       PEM 1 status is 'OK'                                                       [PASS]
TASK: Chassis Environment       RE 0 Intake status is 'OK'                                                 [PASS]
TASK: Chassis Environment       RE 0 Front Exhaust status is 'OK'                                          [PASS]
TASK: Chassis Environment       RE 0 Rear Exhaust status is 'OK'                                           [PASS]
TASK: Chassis Environment       Routing Engine status is 'OK'                                              [PASS]
TASK: Chassis Environment       Routing Engine CPU status is 'OK'                                          [PASS]
TASK: Chassis Environment       TFEB 0 QX 0 TSen status is 'OK'                                            [PASS]
TASK: Chassis Environment       TFEB 0 QX 0 Chip status is 'OK'                                            [PASS]
TASK: Chassis Environment       TFEB 0 LU 0 TSen status is 'OK'                                            [PASS]
TASK: Chassis Environment       TFEB 0 LU 0 Chip status is 'OK'                                            [PASS]
TASK: Chassis Environment       TFEB 0 MQ 0 TSen status is 'OK'                                            [PASS]
TASK: Chassis Environment       TFEB 0 MQ 0 Chip status is 'OK'                                            [PASS]
TASK: Chassis Environment       TFEB 0 TBB PFE TSen status is 'OK'                                         [PASS]
TASK: Chassis Environment       TFEB 0 TBB PFE Chip status is 'OK'                                         [PASS]
TASK: Chassis Environment       TFEB 0 TFEB PCIE TSen status is 'OK'                                       [PASS]
TASK: Chassis Environment       TFEB 0 TFEB PCIE Chip status is 'OK'                                       [PASS]
TASK: Chassis Environment       Fan 1 status is 'OK'                                                       [PASS]
TASK: Chassis Environment       Fan 2 status is 'OK'                                                       [PASS]
TASK: Chassis Environment       Fan 3 status is 'OK'                                                       [PASS]
TASK: Chassis Environment       Fan 4 status is 'OK'                                                       [PASS]
TASK: Chassis Environment       Fan 5 status is 'OK'                                                       [PASS]
TASK: Interface                 ge-1/0/1 has valid description                                             [PASS]
TASK: Interface                 ge-1/0/2 has valid description                                             [PASS]
TASK: Interface                 ge-1/0/8 has valid description                                             [PASS]
TASK: Interface                 ge-1/0/9 has valid description                                             [PASS]
TASK: Interface                 ge-1/1/0 has valid description                                             [PASS]
TASK: Interface                 lt-1/0/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/1 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/2 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/8 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/9 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/1/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/1 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/0/2 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/0/8 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/0/9 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/1/0 operating in 'full-duplex' mode                                   [PASS]


                            -- END OF DEVICE REPORT --


Ansible Generated MPLS Report
Hostname: LAB-nn-MPLS-STK-SW
Report Type: FULL

TASK                            TESTED ATTRIBUTE                                                           RESULT
-----------------------------------------------------------------------------------------------------------------
TASK: System Alarms             Alarm count is 0                                                           [FAIL]
TASK: Chassis Alarms            Alarm count is 0                                                           [PASS]
TASK: Software Version          Package 'junos' is '13.2X51-D21.1' on fpc0                                 [FAIL]
TASK: Software Version          Package 'fips-mode-powerpc' is '13.2X51-D21.1' on fpc0                     [FAIL]
TASK: Software Version          Package 'jdocs-ex' is '13.2X51-D21.1' on fpc0                              [FAIL]
TASK: Software Version          Package 'junos-ex-4300' is '13.2X51-D21.1' on fpc0                         [FAIL]
TASK: Software Version          Package 'jweb-ex' is '13.2X51-D21.1' on fpc0                               [FAIL]
TASK: Software Version          Package 'py-base-powerpc' is '13.2X51-D21.1' on fpc0                       [FAIL]
TASK: Software Version          Package 'junos' is '13.2X51-D21.1' on fpc1                                 [FAIL]
TASK: Software Version          Package 'fips-mode-powerpc' is '13.2X51-D21.1' on fpc1                     [FAIL]
TASK: Software Version          Package 'jdocs-ex' is '13.2X51-D21.1' on fpc1                              [FAIL]
TASK: Software Version          Package 'junos-ex-4300' is '13.2X51-D21.1' on fpc1                         [FAIL]
TASK: Software Version          Package 'jweb-ex' is '13.2X51-D21.1' on fpc1                               [FAIL]
TASK: Software Version          Package 'py-base-powerpc' is '13.2X51-D21.1' on fpc1                       [FAIL]
TASK: System Core Dumps         None exist on fpc0                                                         [PASS]
TASK: System Core Dumps         None exist on fpc1                                                         [FAIL]
TASK: Chassis FPC               Slot 0 Online                                                              [PASS]
TASK: Chassis FPC               Slot 1 Online                                                              [PASS]
TASK: Chassis Environment       FPC 0 Power Supply 0 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 0 Power Supply 1 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 1 Power Supply 0 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 1 Power Supply 1 status is 'OK'                                        [PASS]
TASK: Chassis Environment       FPC 0 CPU status is 'OK'                                                   [PASS]
TASK: Chassis Environment       FPC 0 NW-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 0 SE-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 0 PHY-2/3 status is 'OK'                                               [PASS]
TASK: Chassis Environment       FPC 0 MGMT PHY status is 'OK'                                              [PASS]
TASK: Chassis Environment       FPC 1 CPU status is 'OK'                                                   [PASS]
TASK: Chassis Environment       FPC 1 NW-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 1 SE-PFE status is 'OK'                                                [PASS]
TASK: Chassis Environment       FPC 1 PHY-2/3 status is 'OK'                                               [PASS]
TASK: Chassis Environment       FPC 1 MGMT PHY status is 'OK'                                              [PASS]
TASK: Chassis Environment       FPC 0 Fan 0 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 0 Fan 0 Airflow status is 'OK'                                         [PASS]
TASK: Chassis Environment       FPC 0 Fan 1 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 0 Fan 1 Airflow status is 'OK'                                         [PASS]
TASK: Chassis Environment       FPC 1 Fan 0 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 1 Fan 0 Airflow status is 'OK'                                         [PASS]
TASK: Chassis Environment       FPC 1 Fan 1 status is 'OK'                                                 [PASS]
TASK: Chassis Environment       FPC 1 Fan 1 Airflow status is 'OK'                                         [PASS]
TASK: Interface                 ge-0/0/0 has valid description                                             [PASS]
TASK: Interface                 ge-0/0/11 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/13 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/14 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/16 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/21 has valid description                                            [PASS]
TASK: Interface                 ge-0/0/23 has valid description                                            [PASS]
TASK: Interface                 ge-0/2/0 has valid description                                             [PASS]
TASK: Interface                 ge-0/2/1 has valid description                                             [PASS]
TASK: Interface                 ge-1/0/13 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/14 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/15 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/16 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/20 has valid description                                            [PASS]
TASK: Interface                 ge-1/0/23 has valid description                                            [PASS]
TASK: Interface                 ge-1/2/0 has valid description                                             [PASS]
TASK: Interface                 ge-1/2/1 has valid description                                             [PASS]
TASK: Interface                 ae1 has valid description                                                  [PASS]
TASK: Interface                 ge-0/0/4 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-0/0/5 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-0/0/8 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-0/0/10 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/11 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/12 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/13 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/14 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/16 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/17 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/18 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/19 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/20 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-0/0/21 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/0/23 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-0/2/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-0/2/1 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/0/4 as WAN, COR or SystemPort is up                                   [FAIL]
TASK: Interface                 ge-1/0/12 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/13 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/14 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/15 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/16 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/18 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/19 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/20 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/0/21 as WAN, COR or SystemPort is up                                  [FAIL]
TASK: Interface                 ge-1/0/23 as WAN, COR or SystemPort is up                                  [PASS]
TASK: Interface                 ge-1/2/0 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ge-1/2/1 as WAN, COR or SystemPort is up                                   [PASS]
TASK: Interface                 ae1 as WAN, COR or SystemPort is up                                        [PASS]
TASK: Interface                 ge-0/0/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/0/11 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/13 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/14 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/16 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/21 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/0/23 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-0/2/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-0/2/1 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/0/13 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/14 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/15 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/16 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/20 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/0/23 operating in 'full-duplex' mode                                  [PASS]
TASK: Interface                 ge-1/2/0 operating in 'full-duplex' mode                                   [PASS]
TASK: Interface                 ge-1/2/1 operating in 'full-duplex' mode                                   [PASS]


                            -- END OF DEVICE REPORT --```


