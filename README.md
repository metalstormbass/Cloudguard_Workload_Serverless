# Cloudguard_Workload_Serverless

![Build Status](https://github.com/metalstormbass/Cloudguard_Workload_Serverless/blob/master/.github/workflows/build.yml/badge.svg)





To Run:<br>
Onboard AWS account (you can use onboard.py)<br>
Modify _build_flag <br>
Run activity.py to test <br>
<br>
For synchronization: <br>
curl -X POST https://api.dome9.com/v2/cloudaccounts/{id}/SyncNow \
  --basic -u <key-id>:<key-secret> \
  -H 'Accept: application/json'<br><br>

To destroy: <Br>
Modify _destroy_flag<br>
