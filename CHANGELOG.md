# 0.1.3 > 0.1.4:
- Add `-pp` `--paths` command line option
   - Adds easier way to add custom paths for rtsp streams
- Add RTSP_WHITESPACE environment variable
- Move `cla()` within `if __name__ == "__main":`
- refactor `splitEnvCSV` to `splitCSV` to better reflect its function
- Add error handling on requests.ConnectionError while trying to contact API
  - Thank you @tammeryousef1006 for pointing out this behavior
  - Outputs tips on how to rectify problems and stops further connection attemps
  - Typical output:
```
Cannot reach rtsp-simple-server at http://192.168.2.243:9997.
Possible Causes: API not enabled
                 transport (http/https) not correct: http
                 ip/fqdn not correct: 192.168.2.243
                 port number not correct: 9997

4 Potential RTSP Sources:
  192.168.2.190:8554
  192.168.2.189:8554

2 Cameras Found:
  192.168.2.190: rtsp://*****:*****@192.168.2.190:8554/Streaming/Channels/101
  192.168.2.189: rtsp://*****:*****@192.168.2.189:8554/Streaming/Channels/101

Credentials Used:
  *****:*****

Paths Used:
  /Streaming/Channels/101
  /live
  /live2
```
# 0.1.2 > 0.1.3:
- Bugfix

# 0.1.1 > 0.1.2:
- Update License to properly reflect AGPLv3