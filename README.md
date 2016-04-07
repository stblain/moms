# My OpenStack Management System

## Roles

| Role                  | Hostname pattern           | Definition |
| --------------------- | -------------------------- | ---------- |
| management/configurer | configsrv-<#>.<SITE_NAME>  |            |
| management/monitorer  | monitsrv-<#>.<SITE_NAME>   |            |
| management/logger     | logsrv-<#>.<SITE_NAME>     |            |
| cloudinfra/controller | controller-<#>.<SITE_NAME> |            |
| cloudinfra/storage    | storage-<#>.<SITE_NAME>    |            |
| cloudinfra/compute    | compute-<#>.<SITE_NAME>    |            |


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
| {HOST.IP}           | ansible_host       | auto     | String |         |                               |                       |
| {$ANSIBLE_SSH_PASS} | ansible_ssh_pass   | yes      | String |         |                               |                       |
| {$ANSIBLE_USER}     | ansible_user       | yes      | String |         |                               |                       |


## Management installation from scratch
Since the configuration server needs a monitoring server as the data source, and the monitoring server needs to be
configured by the configuration server, some bootstrapping are needed. An independent system with Ansible, and the
latest MOMS version will be used to bootstrap the monitoring server.

Bootstrap the monitoring server:
1) Install OS on configsrv-1.<SITE_NAME> et monitsrv-1.<SITE_NAME>
1) Bootstrap monitsrv-1

   `ansible-playbook bootstrap-zabbix.yml --inventory=bootstrap.inv --user=<user> --ask-pass --extra-vars=ansible_host="<IP>" --extra-vars="site_name=<SITE_NAME>"`
1) Connect to http://<IP>/zabbix (Admin/zabbix)
   1) Fill macros in `Administration | General | Macros`
   1) Fill macros in `Configuration | Templates | Configuration Role - management.configurer | Macros`
1) Set the management IP address of configsrv-1.<SITE_NAME> in `Configuration | Hosts | configsrv-1.<SITE_NAME> | Agent Interfaces | IP ADDRESS`
1) Set the management IP address of monitsrv-1.<SITE_NAME> in `Configuration | Hosts | monitsrv-1.<SITE_NAME> | Agent Interfaces | IP ADDRESS`

