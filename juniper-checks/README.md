# Depends
ansible 2.4+

## Variables
group_vars/all.yml `<report_type: 'fail'>` prints only failures

```ansible-playbook -i hosts main.yml -e "report_type='full'"```

Above example will print all 'fail' and 'pass' checks in device reports.
