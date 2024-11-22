# Log Collector

```
 ██▓     ▒█████   ▄████     ▄████▄  ▒█████   ██▓     ██▓    ▓█████ ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
▓██▒    ▒██▒  ██▒██▒ ▀█▒   ▒██▀ ▀█ ▒██▒  ██▒▓██▒    ▓██▒    ▓█   ▀▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░    ▒██░  ██▒██░▄▄▄░   ▒▓█    ▄▒██░  ██▒▒██░    ▒██░    ▒███  ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██░    ▒██   ██░▓█  ██▓   ▒▓▓▄ ▄██▒██   ██░▒██░    ▒██░    ▒▓█  ▄▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░██████▒░ ████▓▒░▒▓███▀▒   ▒ ▓███▀ ░ ████▓▒░░██████▒░██████▒░▒████▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▓  ░░ ▒░▒░▒░ ░▒   ▒    ░ ░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░ ▒  ░  ░ ▒ ▒░  ░   ░      ░  ▒    ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░ ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░ ░   ░ ░ ░ ▒ ░ ░   ░    ░       ░ ░ ░ ▒    ░ ░     ░ ░      ░  ░          ░      ░ ░ ░ ▒    ░░   ░ 
    ░  ░    ░ ░       ░    ░ ░         ░ ░      ░  ░    ░  ░   ░  ░ ░                   ░ ░     ░     
                           ░                                      ░                                   
```

# Description
- The Log Collector is a Python program designed to interact with an ELK SIEM (Elasticsearch, Logstash, Kibana) stack to efficiently collect logs from specified indices and save them in a structured JSON format. It supports custom log retrieval parameters such as index selection, batch sizes, and maximum log limits, making it a versatile tool for log analysis and data collection.
- Due to ELK only allowing a maximum of 10,000 logs to be retrieved at a time, the Log Collector is designed to retrieve logs in batches of 10,000 until the specified limit is reached.