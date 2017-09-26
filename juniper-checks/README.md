# Juniper Checks
* Common checks run again EX4300, SRX550 and MX5 platforms.
* Generates a report per devices in ./reports/ folder.
* default variable `report_type` is set to 'fail' in ./group_vars/all.tml - this forces report generation to print only failures.
  * See below on how to override to all 'fail' and 'pass'

## Depends
ansible 2.4+ (XML to JSON is broken pre-2.4)

## Variables
group_vars/all.yml `report_type: 'fail'` prints only failures

```ansible-playbook -i hosts main.yml -e "report_type='full'"```

Above example will print all 'fail' and 'pass' checks in device reports.
