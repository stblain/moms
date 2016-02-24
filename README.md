# My OpenStack Management System

## Variables

* **apt_proxy**: Proxy used by apt
  * Required: no
  * Type: String
  * Default:

    `""`
  * Example:
    
    `http://proxy.company.com:80`

| Zabbix macro        | Ansible variable | Required | Type   | Default | Example |
| ------------------- | ---------------- | -------- | ------ | ------- | ------- |
| {$DHCP_RANGE}       | dhcp_range       | no       | String |         |         |
| {$APT_PROXY}        | apt_proxy        | no       | String |         |         |
| sites               |                  |        |         |         |


## Roles

| Role                  | Hostname    |
| --------------------- | ----------- |
| management/configurer | configsrv-# |
| management/monitorer  | monitsrv-#  |
