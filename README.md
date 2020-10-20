# Cloudguard_Workload_Serverless
To Run:
Onboard AWS account
Enable Serverless
Modify _build_flag
Run activity.py to generate activity

For synchronization:
curl -X POST https://api.dome9.com/v2/cloudaccounts/{id}/SyncNow \
  --basic -u <key-id>:<key-secret> \
  -H 'Accept: application/json'

To destroy:
Modify _destroy_flag
