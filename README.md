# My OpenStack Management System

## Roles

| Role                  | Hostname                 | Definition |
| --------------------- | ------------------------ | ---------- |
| management/configurer | configsrv-<#>.<SITENAME> |            |
| management/monitorer  | monitsrv-<#>.<SITENAME>  |            |
| management/logger     |                          |            |
| cloudinfra/compute    |                          |            |
| cloudinfra/controller |                          |            |
| cloudinfra/storage    |                          |            |
| cloudinfra/           |                          |            |


## Variables
### Site Variables

| Zabbix's macro      | Ansible's variable | Required | Type   | Default | Example                       | Description                  |
| ------------------- | ------------------ | -------- | ------ | ------- | ----------------------------- | ---------------------------- |
| {$DHCP_RANGE}       | dhcp_range         | no       | String |         |                               | dnsmasq's dhcp-range format  |
| {$DHCP_OPTION}      | dhcp_option        | no       | String |         |                               | dnsmasq's dhcp-option format |
|                     | site_name          | auto     | String |         |                               |                              |

### Role Variables
#### Management/Configurer
| Zabbix's macro      | Ansible's variable | Required | Type   | Default | Example                       | Description                  |
| ------------------- | ------------------ | -------- | ------ | ------- | ----------------------------- | ---------------------------- |
| {$GIT_APT_MIRROR}   | git_apt_mirror     | yes      | String |         |                               |                       |

### Other Variables
| Zabbix's macro      | Ansible's variable | Required | Type   | Default | Example                       | Description           |
| ------------------- | ------------------ | -------- | ------ | ------- | ----------------------------- | --------------------- |
| {$APT_PROXY}        | apt_proxy          | no       | String | ''      | `http://proxy.company.com:80` |                       |
| {HOST.IP}           | ansible_host       | auto     | String |         |                               |                       |
| {$ANSIBLE_SSH_PASS} | ansible_ssh_pass   | yes      | String |         |                               |                       |
| {$ANSIBLE_USER}     | ansible_user       | yes      | String |         |                               |                       |


## Management installation from scratch
Catch 22 between zabbix <-> ansible. From an independent system with Ansible, bootstrap
the zabbix server in order to serve inventory. Then install the configuration server.
Ans then install everything else.

From an external node with ansible and the latest MOMS:
1) Install OS on configsrv-1 et monitsrv-1
1) Bootstrap monitsrv-1
       > ansible-playbook bootstrap-zabbix.yml --inventory=bootstrap.inv --user=<user> --ask-pass --extra-vars=ansible_host="<IP>" --extra-vars="site_name=<SITE>"
1) Connect to http://<IP>/zabbix (Admin/zabbix)
1) Set the IP address of configsrv-1.<SITE>
1) Set the IP address of monitsrv-1.<SITE>
