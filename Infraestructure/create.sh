aws cloudformation create-stack \
--stack-name $1 \
--template-body file://$2 \
--parameters file://$3 \
--region us-west-2 \
--capabilities CAPABILITY_NAMED_IAM


# aws cloudformation create-stack --stack-name network --template-body file://capstone-network.yaml --parameters file://parameters.json --region us-west-2 --capabilities CAPABILITY_NAMED_IAM