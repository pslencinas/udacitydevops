aws cloudformation create-stack \
--stack-name $1 \
--template-body file://$2 \
--parameters file://$3 \
--region=eu-west-2 \

# run this way: 
# ./create.sh "Stack Name" "template" "parameters"