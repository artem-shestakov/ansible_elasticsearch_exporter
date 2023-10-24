# Ansible role - artem_shestakov.elasticsearch_exporter
Install [Elasticsearch exporter](https://github.com/prometheus-community/elasticsearch_exporter)

## Role variables

| Variables                | Description | Default     |
| ----------------------- | ----------- | ----------- |
| es_exporter_user        | User who starts exporter | elasticsearch
| es_uri                  | Address (host and port) of the Elasticsearch node we should connect to. This could be a local node (`localhost:9200`, for instance), or the address of a remote Elasticsearch server. When basic auth is needed, specify as: `<proto>://<user>:<password>@<host>:<port>`. E.G., `http://admin:pass@localhost:9200`. Special characters in the user credentials need to be URL-encoded. | <http://localhost:9200> |
| es_all                  | If true, query stats for all nodes in the cluster, rather than just the node we connect to.                             | false |
| es_cluster_settings     | If true, query stats for cluster settings. | false |
| es_indices              | If true, query stats for all indices in the cluster. | false |
| es_indices_settings     | If true, query settings stats for all indices in the cluster. | false |
| es_indices_mappings     | If true, query stats for mappings of all indices of the cluster. | false |
| es_aliases              | If true, include informational aliases metrics. | true |
| es_shards               | If true, query stats for all indices in the cluster, including shard-level stats (implies `es.indices=true`). | false |
| es_snapshots            | If true, query stats for the cluster snapshots. | false |
| es_slm                  | If true, query stats for SLM. | false |
| es_data_stream          | If true, query state for Data Steams. | false |
| es_timeout              | Timeout for trying to get stats from Elasticsearch. (ex: 20s) | 5s |
| es_ca                   | Path to PEM file that contains trusted Certificate Authorities for the Elasticsearch connection. | |
| es_client_private_key   | Path to PEM file that contains the private key for client auth when connecting to Elasticsearch. | |
| es_client_cert          | Path to PEM file that contains the corresponding cert for the private key to connect to Elasticsearch. | |
| es_clusterinfo_interval |  Cluster info update interval for the cluster label | 5m |
| es_ssl_skip_verify      | Skip SSL verification when connecting to Elasticsearch. | false |
| web_listen_address      | Address to listen on for web interface and telemetry. | :9114 |
| web_telemetry_path      | Path under which to expose metrics. | /metrics |
| version                 | Show version info on stdout and exit. | 1.3.0 |


