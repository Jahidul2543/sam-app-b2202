aws lambda invoke \
 --function-name green-light \
 --invocation-type Event \
 --payload '{ "name": "Bob" }' \
 response.json


 aws lambda invoke \
     --function-name green-light \
     --invocation-type Event \
     --payload '{ "name": "Bob" }'

aws lambda invoke --function-name green-light --cli-binary-format raw-in-base64-out --payload '{ "key": "value" }' response.json

aws lambda invoke \
  --function-name sam-app-b2202-HelloWorldFunction-MuSBRZ4RYX8u  \
      --invocation-type Event \
          --cli-binary-format raw-in-base64-out \
              --payload '{ "Name": "John" }' response.json
