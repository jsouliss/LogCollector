# LogSense

```
 ██▓     ▒█████    ▄████   ██████ ▓█████  ███▄    █   ██████ ▓█████ 
▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██    ▒ ▓█   ▀ 
▒██░    ▒██░  ██▒▒██░▄▄▄░░ ▓██▄   ▒███   ▓██  ▀█ ██▒░ ▓██▄   ▒███   
▒██░    ▒██   ██░░▓█  ██▓  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒▒▓█  ▄ 
░██████▒░ ████▓▒░░▒▓███▀▒▒██████▒▒░▒████▒▒██░   ▓██░▒██████▒▒░▒████▒
░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
░ ░ ▒  ░  ░ ▒ ▒░   ░   ░ ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░ ░ ░  ░
  ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░  ░  ░     ░      ░   ░ ░ ░  ░  ░     ░   
    ░  ░    ░ ░        ░       ░     ░  ░         ░       ░     ░  ░                                                                 
```

# Description

- Log Collector is a Python program designed to interact with an ELK SIEM (Elasticsearch, Logstash, Kibana) stack. It efficiently collects logs from specified indices and saves them in a structured JSON format. The program supports customizable log retrieval parameters such as index selection, batch sizes, and maximum log limits, making it a versatile tool for log analysis and data collection.
- Batch Processing: Since ELK imposes a maximum limit of 10,000 logs per query, the Log Collector is designed to retrieve logs in batches of 10,000. It continues retrieving logs in batches until the specified limit is reached, ensuring large-scale data collection without exceeding query limits.
- Data Formatting: The project also includes data formatting utilities designed to prepare the collected data for training a large language model (LLM). These programs ensure the data is in an acceptable format for efficient LLM training.