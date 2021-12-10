# Ansible role - artem_shestakov.elasticsearch_exporter
Install exporter and register in Consul.

## Role variables
### **version**
* Version of exporter
* Default: 1.3.0

### **consul_host**
* Consul agent address without port
* Default: "localhost"

### **consul_service_name** 
* Service name in Consul
* Default: elasticsearch_exporter

### **consul_service_port**
* The port on which the service is listening
* Default: 9114

### **consul_service_tags**
* Tags that will be attached to the service registration
* Default: [exporter]

### **consul_service_interval**
* A custom HTTP check timeout
* Default: 60s