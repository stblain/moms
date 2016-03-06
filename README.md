# My OpenStack Management System


## Roles

| Role                  | Definition |
| --------------------- | ---------- |
| management/configurer |            |
| management/monitorer  |            |
| management/logger     |            |
| cloudinfra/compute    |            |
| cloudinfra/controller |            |
| cloudinfra/storage    |            |

## Variables

| Zabbix's macro      | Ansible's variable | Required | Type   | Default | Example                       | Description           |
| ------------------- | ------------------ | -------- | ------ | ------- | ----------------------------- | --------------------- |
| {$DHCP_RANGE}       | dhcp_range         | no       | String |         |                               | dnsmasq's dhcp-range  |
| {$DHCP_OPTION}      | dhcp_option        | no       | String |         |                               | dnsmasq's dhcp-option |
| {HOST.IP}           | ansible_host       | auto     | String |         |                               |                       |
| {$APT_PROXY}        | apt_proxy          | no       | String | ''      | `http://proxy.company.com:80` |                       |
|                     | site_name          | auto     | String |         |                               |                       |


## Hostname assigment

| Role                  | Hostname    |
| --------------------- | ----------- |
| management/configurer | configsrv-# |
| management/monitorer  | monitsrv-#  |
| cloudinfra/???        | mgmtsw-#    |







## Management installation from scratch
From an external node with ansible and the latest MOMS:
1) Install OS on configsrv-1 et monitsrv-1
1) Bootstrap monitsrv-1
       > ansible-playbook bootstrap-zabbix.yml --inventory=bootstrap.inv --user=<user> --ask-pass --extra-vars=ansible_host=<IP>
1) Connect to http://<IP>/zabbix (Admin/zabbix)and complete the setup ("Next step" x5 + "Finish")
1) Create group "Role - management.configurer"
1) Create group "Role - management.monitorer"
1) Create group "Site - <SITE>"
1) Create host "configsrv-1.<SITE>" in group "Role - management.configurer", "Site - <SITE>"
1) Create host "monitsrv-1.<SITE>" in group "Role - management.monitorer", "Site - <SITE>"
1) Delete host "Zabbix server"
1) Create template "Configuration Role - management.configurer"
1) Create template "Configuration Role - management.monitorer"
1) Create template "Configuration Site - <SITE>"
